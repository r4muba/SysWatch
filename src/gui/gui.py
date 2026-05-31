import ttkbootstrap as tb
from .sideFrame import SideFrame
from .mainFrame import MainFrame

class GUI:
    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, systemData, threadController):
        self._systemData = systemData
        self._threadController = threadController

        self._root = tb.Window (themename="litera")
        self._root.geometry (f"{GUI.WIDTH}x{GUI.HEIGHT}")

        self._root.rowconfigure (0, weight=1)
        self._root.columnconfigure (0, weight=4, uniform="M")
        self._root.columnconfigure (1, weight=11, uniform="M")

        self._sideFrame = SideFrame(self._root, self._threadController, self)
        self._mainFrame = MainFrame(self._root, self._threadController)

        self._sideFrame.grid(row=0, column=0, sticky="nsew")
        self._mainFrame.grid(row=0, column=1, sticky="nsew")
    
    
    def packMemoryPanel(self):
        self._mainFrame._memPanel.pack(fill="both", expand=True)

    def packProcessPanel(self):
        self._mainFrame._proccessPanel.pack(fill="both", expand=True)

    def packGeneralPanel(self):
        self._mainFrame._generalPanel.pack(fill="both", expand=True)

    def packDebugPanel(self):
        self._mainFrame._debugPanel.pack(fill="both", expand=True)

    
    def run(self):
        self._root.mainloop()
