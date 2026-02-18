import tkinter as tk
from core.constants import *

class ClientWindow(tk.Toplevel):
    def __init__(self,engine):
        super().__init__()
        self.engine=engine
        self.configure(bg=BG)
        self.title("CLIENT")

        tk.Label(self,text="CLIENT",bg=BG,fg=FG,font=("Consolas",16,"bold")).pack()

        self.state=tk.Label(self,text="State:CLOSED",bg=BG,fg=FG,font=FONT)
        self.state.pack()

        self.log=tk.Text(self,height=15,width=45,bg=BG,fg=FG,insertbackground=FG)
        self.log.pack()

        self.entry=tk.Entry(self,bg=BG,fg=FG,insertbackground=FG)
        self.entry.pack()

        tk.Button(self,text="Send",command=self.send,bg="black",fg=FG).pack()
        tk.Button(self,text="Close",command=engine.close,bg="black",fg=FG).pack()

        engine.bus.subscribe("packet_sent",self.show)
        engine.bus.subscribe("client_state",self.update)
        engine.bus.subscribe("window_full",self.full)

    def send(self):
        self.engine.send_data(self.entry.get())

    def show(self,p):
        self.log.insert(tk.END,str(p)+"\n")

    def update(self,s):
        self.state.config(text="State:"+s)

    def full(self,_):
        self.log.insert(tk.END,"WINDOW FULL\n")
