import tkinter as tk
from core.constants import *

class ServerWindow(tk.Toplevel):

    def __init__(self, engine):
        super().__init__()

        self.configure(bg=BG)
        self.title("SERVER")
        self.geometry("420x450")
        # self.resizable(False, False)

        # Header
        header = tk.Label(
            self,
            text="SERVER",
            bg=BG,
            fg=FG,
            font=("Consolas", 18, "bold")
        )
        header.pack(pady=10)

        # State label
        self.state = tk.Label(
            self,
            text="State: LISTEN",
            bg=BG,
            fg=FG,
            font=FONT
        )
        self.state.pack(pady=(0, 10))

        # Log frame
        log_frame = tk.Frame(self, bg=BG)
        log_frame.pack(padx=10, pady=5, fill="both", expand=True)

        tk.Label(
            log_frame,
            text="Server Activity Log",
            bg=BG,
            fg=FG,
            font=FONT
        ).pack(anchor="w")

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

        engine.bus.subscribe("packet_received", self.show)
        engine.bus.subscribe("message", self.msg)
        engine.bus.subscribe("server_state", self.update)

    def show(self, p):
        self.log.insert(tk.END, "[PACKET] " + str(p) + "\n")
        self.log.see(tk.END)

    def msg(self, m):
        self.log.insert(tk.END, "[MESSAGE] " + str(m) + "\n")
        self.log.see(tk.END)

    def update(self, s):
        self.state.config(text="State: " + s)