import ttkbootstrap as tb
from .sidePanel import SidePanel
from .mainPanel import MainPanel

class GUI:
    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, controller):
        self._ctrl = controller

        self._root = tb.Window (themename="litera")
        self._root.geometry (f"{GUI.WIDTH}x{GUI.HEIGHT}")

        self._root.rowconfigure (0, weight=1)
        self._root.columnconfigure (0, weight=4, uniform="M")
        self._root.columnconfigure (1, weight=11, uniform="M")

        self._sidePanel = SidePanel(self._root, self._ctrl)
        self._mainPanel = MainPanel(self._root, self._ctrl)

        self._sidePanel.grid(row=0, column=0, sticky="nsew")
        self._mainPanel.grid(row=0, column=1, sticky="nsew")
    
    def run(self):
        self._root.mainloop()
