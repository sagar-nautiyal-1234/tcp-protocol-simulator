import tkinter as tk
from core.constants import *

class ClientWindow(tk.Toplevel):

    def __init__(self, engine):
        super().__init__()

        self.engine = engine
        self.configure(bg=BG)
        self.title("CLIENT")
        self.geometry("420x500")
        
        # Header
        header = tk.Label(self, text="CLIENT", bg=BG, fg=FG,
                          font=("Consolas", 18, "bold"))
        header.pack(pady=10)

        # State
        self.state = tk.Label(self, text="State: CLOSED",
                              bg=BG, fg=FG, font=FONT)
        self.state.pack(pady=(0, 10))

        # Log Frame
        log_frame = tk.Frame(self, bg=BG)
        log_frame.pack(padx=10, pady=5, fill="both", expand=True)

        tk.Label(log_frame, text="Packet Log",
                 bg=BG, fg=FG, font=FONT).pack(anchor="w")

        scrollbar = tk.Scrollbar(log_frame)
        scrollbar.pack(side="right", fill="y")

        self.log = tk.Text(
            log_frame,
            height=15,
            bg=BG,
            fg=FG,
            insertbackground=FG,
            yscrollcommand=scrollbar.set
        )

        self.log.pack(fill="both", expand=True)
        scrollbar.config(command=self.log.yview)

        # Input Frame
        input_frame = tk.Frame(self, bg=BG)
        input_frame.pack(padx=10, pady=10, fill="x")

        self.entry = tk.Entry(
            input_frame,
            bg=BG,
            fg=FG,
            insertbackground=FG
        )
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        send_btn = tk.Button(
            input_frame,
            text="Send",
            command=self.send,
            bg="black",
            fg=FG
        )
        send_btn.pack(side="right")

        # Close Button
        close_btn = tk.Button(
            self,
            text="Close Connection",
            command=engine.close,
            bg="black",
            fg=FG
        )
        close_btn.pack(pady=10)

        engine.bus.subscribe("packet_sent", self.show)
        engine.bus.subscribe("client_state", self.update)
        engine.bus.subscribe("window_full", self.full)

    def send(self):
        msg = self.entry.get()
        if msg.strip():
            self.engine.send_data(msg)
            self.entry.delete(0, tk.END)

    def show(self, p):
        self.log.insert(tk.END, str(p) + "\n")
        self.log.see(tk.END)

    def update(self, s):
        self.state.config(text="State: " + s)

    def full(self, _):
        self.log.insert(tk.END, "WINDOW FULL\n")