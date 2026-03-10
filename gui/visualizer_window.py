import tkinter as tk
from core.constants import *

class VisualizerWindow(tk.Toplevel):

    def __init__(self, engine):
        super().__init__()

        self.configure(bg=BG)
        self.title("VISUALIZER")
        self.geometry("650x350")
        # self.resizable(False, False)

        self.canvas = tk.Canvas(
            self,
            width=650,
            height=350,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack()

        # Client node
        self.canvas.create_rectangle(50,130,150,190,outline=FG,width=2)
        self.canvas.create_text(100,160,text="CLIENT",fill=FG,font=("Consolas",12,"bold"))

        # Server node
        self.canvas.create_rectangle(500,130,600,190,outline=FG,width=2)
        self.canvas.create_text(550,160,text="SERVER",fill=FG,font=("Consolas",12,"bold"))

        # Network line
        self.canvas.create_line(150,160,500,160,fill=FG,width=2)

        self.lane = 0

        engine.bus.subscribe("packet_sent", self.send)
        engine.bus.subscribe("packet_received", self.recv)
        engine.bus.subscribe("timeout", self.timeout)

    def send(self, p):
        self.animate(p, 150, 500, "→", "yellow")

    def recv(self, p):
        self.animate(p, 500, 150, "←", "green")

    def timeout(self, p):
        self.animate(p, 150, 500, "T", "orange")

    def animate(self, p, start, end, sym, color):

        y = 120 + (self.lane * 20)
        self.lane = (self.lane + 1) % 5

        obj = self.canvas.create_text(
            start,
            y,
            text=f"{sym} {p.pkt_type}",
            fill=color,
            font=("Consolas",11)
        )

        step = 3 if end > start else -3

        def move():
            x,_ = self.canvas.coords(obj)

            if (step > 0 and x < end) or (step < 0 and x > end):
                self.canvas.move(obj, step, 0)
                self.after(15, move)
            else:
                self.canvas.delete(obj)

        move()