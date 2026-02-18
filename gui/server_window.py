import tkinter as tk
from core.constants import *

class ServerWindow(tk.Toplevel):
    def __init__(self,engine):
        super().__init__()
        self.configure(bg=BG)
        self.title("SERVER")

        tk.Label(self,text="SERVER",bg=BG,fg=FG,font=("Consolas",16,"bold")).pack()

        self.state=tk.Label(self,text="State:LISTEN",bg=BG,fg=FG,font=FONT)
        self.state.pack()

        self.log=tk.Text(self,height=15,width=45,bg=BG,fg=FG,insertbackground=FG)
        self.log.pack()

        engine.bus.subscribe("packet_received",self.show)
        engine.bus.subscribe("message",self.msg)
        engine.bus.subscribe("server_state",self.update)

    def show(self,p):
        self.log.insert(tk.END,str(p)+"\n")

    def msg(self,m):
        self.log.insert(tk.END,"Message:"+str(m)+"\n")

    def update(self,s):
        self.state.config(text="State:"+s)
