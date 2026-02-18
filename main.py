from core.engine import ProtocolEngine
from gui.client_window import ClientWindow
from gui.server_window import ServerWindow
from gui.visualizer_window import VisualizerWindow
import tkinter as tk

root = tk.Tk()
root.withdraw()

engine = ProtocolEngine()

client = ClientWindow(engine)
server = ServerWindow(engine)
visual = VisualizerWindow(engine)

engine.start()

client.mainloop()
