import ttkbootstrap as tb

class SideFrame (tb.Frame):
    def __init__(self, frame, systemData, gui):
        super().__init__(
            frame,
            bootstyle="info"
        )

        self._gui = gui
        self._sysData = systemData
        self._build()

    def _build(self):

        title = tb.Label (
            self,
            bootstyle="dark",
            text="SYSWATCH",
            font=("Helvetica", 20, "bold")
        )
        title.pack(anchor="w", padx=30, pady=30)

        b1 = tb.Button (
            self, 
            bootstyle="danger",
            text="General",
            command=self._gui.packGeneralPanel
        )
        b1.pack(fill="x", padx=40, pady=20)

        b2 = tb.Button (
            self, 
            bootstyle="danger",
            text="Proccess",
            command=self._gui.packProcessPanel
        )
        b2.pack(fill="x", padx=40, pady=20)

        b3 = tb.Button (
            self, 
            bootstyle="danger",
            text="Memory",
            command=self._gui.packMemoryPanel
        )
        b3.pack(fill="x", padx=40, pady=20)

        b4 = tb.Button (
            self, 
            bootstyle="danger",
            text="Debug",
            command=self._gui.packDebugPanel
        )
        b4.pack(fill="x", padx=40, pady=20)

