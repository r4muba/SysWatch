import ttkbootstrap as tb
from .sideFrame import SideFrame
from .mainFrame import MainFrame

class GUI:
    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, systemData):
        self._sysData = systemData

        self._root = tb.Window (themename="litera")
        self._root.geometry (f"{GUI.WIDTH}x{GUI.HEIGHT}")

        self._root.rowconfigure (0, weight=1)
        self._root.columnconfigure (0, weight=4, uniform="M")
        self._root.columnconfigure (1, weight=11, uniform="M")

        self._sidePanel = SideFrame(self._root, self._sysData)
        self._mainPanel = MainFrame(self._root, self._sysData)

        self._sidePanel.grid(row=0, column=0, sticky="nsew")
        self._mainPanel.grid(row=0, column=1, sticky="nsew")
    
    def run(self):
        self._root.mainloop()
