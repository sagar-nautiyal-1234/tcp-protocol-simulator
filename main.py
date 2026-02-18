from core.engine import ProtocolEngine
from gui.client_window import ClientWindow
from gui.server_window import ServerWindow
from gui.visualizer_window import VisualizerWindow
import tkinter as tk

root = tk.Tk()
root.withdraw()

engine = ProtocolEngine()

ClientWindow(engine)
ServerWindow(engine)
VisualizerWindow(engine)

engine.start()
root.mainloop()
