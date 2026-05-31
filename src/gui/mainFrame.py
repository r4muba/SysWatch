import ttkbootstrap as tb
from .panels import MemoryPanel, ProcessPanel, GeneralPanel, DebugPanel

class MainFrame (tb.Frame):
    def __init__(self, frame, systemData, threadController):
        super().__init__(
            frame,
            bootstyle="danger"
        )

        self._systemData = systemData
        self._threadController = threadController

        self._memPanel = MemoryPanel(self, self._systemData, self._threadController)
        self._proccessPanel = ProcessPanel(self, self._systemData)
        self._generalPanel = GeneralPanel(self, self._systemData, self._threadController)
        self._debugPanel = DebugPanel(self, self._systemData, self._threadController)

        self._build()

    def _build(self):
        ...
        # title = tb.Label (
        #     self,
        #     bootstyle="dark",
        #     text="HERE GOES \nYOUR INFO",
        #     font=("Helvetica", 60, "bold")
        # )
        # title.pack(anchor="w", padx=30, pady=30)
