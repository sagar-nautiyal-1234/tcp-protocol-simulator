import tkinter as tk

class ServerWindow(tk.Toplevel):
    def __init__(self, engine):
        super().__init__()
        self.title("Server")

        tk.Label(self, text="SERVER", font=("Arial",14,"bold")).pack()

        self.state = tk.Label(self, text="State: LISTEN", font=("Arial",12))
        self.state.pack(pady=5)

        self.log = tk.Text(self, height=15, width=40)
        self.log.pack()

        engine.bus.subscribe("packet_received", self.show)
        engine.bus.subscribe("message", self.msg)
        engine.bus.subscribe("server_state", self.update)

    def show(self, pkt):
        self.log.insert(tk.END, str(pkt) + "\n")

    def msg(self, text):
        self.log.insert(tk.END, f"Message: {text}\n")

    def update(self, s):
        self.state.config(text=f"State: {s}")
