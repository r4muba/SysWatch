import ttkbootstrap as tb

class MainFrame (tb.Frame):
    def __init__(self, frame, systemData):
        super().__init__(
            frame,
            bootstyle="success"
        )

        self._sysData = systemData

        panel_one = None
        panel_two = None
        panel_three = None

        self._build()

    def _build(self):
        title = tb.Label (
            self,
            bootstyle="dark",
            text="HERE GOES \nYOUR INFO",
            font=("Helvetica", 60, "bold")
        )
        title.pack(anchor="w", padx=30, pady=30)
