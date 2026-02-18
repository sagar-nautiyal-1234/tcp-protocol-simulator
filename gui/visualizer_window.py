import tkinter as tk

class VisualizerWindow(tk.Toplevel):
    def __init__(self, engine):
        super().__init__()
        self.title("Protocol Visualizer")

        self.text = tk.Text(self, height=20, width=60)
        self.text.pack()

        engine.bus.subscribe("packet_sent", self.sent)
        engine.bus.subscribe("packet_received", self.recv)

    def sent(self, pkt):
        self.text.insert(tk.END, f"→ {pkt}\n")

    def recv(self, pkt):
        self.text.insert(tk.END, f"← {pkt}\n")
