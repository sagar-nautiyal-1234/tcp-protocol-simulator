import tkinter as tk

class ClientWindow(tk.Toplevel):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.title("Client")

        tk.Label(self, text="CLIENT", font=("Arial",14,"bold")).pack()

        self.state_label = tk.Label(self, text="State: CLOSED", font=("Arial", 12))
        self.state_label.pack(pady=5)

        self.log = tk.Text(self, height=15, width=40)
        self.log.pack()

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        tk.Button(self, text="Send", command=self.send).pack()

        engine.bus.subscribe("packet_sent", self.show)
        engine.bus.subscribe("client_state", self.update_state)

    def send(self):
        msg = self.entry.get()
        self.engine.send_data(msg)

    def show(self, pkt):
        self.log.insert(tk.END, str(pkt) + "\n")

    def update_state(self, state):
        self.state_label.config(text=f"State: {state}")
