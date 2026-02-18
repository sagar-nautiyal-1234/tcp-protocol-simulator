import tkinter as tk
from core.constants import *

class VisualizerWindow(tk.Toplevel):
    def __init__(self,engine):
        super().__init__()
        self.configure(bg=BG)
        self.title("VISUALIZER")

        self.canvas=tk.Canvas(self,width=600,height=300,bg="black",highlightthickness=0)
        self.canvas.pack()

        self.canvas.create_text(100,50,text="CLIENT",fill=FG,font=("Consolas",14,"bold"))
        self.canvas.create_text(500,50,text="SERVER",fill=FG,font=("Consolas",14,"bold"))

        engine.bus.subscribe("packet_sent",self.send)
        engine.bus.subscribe("packet_received",self.recv)
        engine.bus.subscribe("timeout",self.timeout)

    def send(self,p):
        self.animate(p,100,500,"→")

    def recv(self,p):
        self.animate(p,500,100,"←")

    def timeout(self,p):
        self.animate(p,100,500,"T")

    def animate(self,p,start,end,sym):
        y=150
        obj=self.canvas.create_text(start,y,text=f"{sym} {p.pkt_type}",fill=FG,font=("Consolas",12))
        step=5 if end>start else -5

        def move():
            x,_=self.canvas.coords(obj)
            if (step>0 and x<end) or (step<0 and x>end):
                self.canvas.move(obj,step,0)
                self.after(20,move)
            else:
                self.canvas.delete(obj)
        move()
