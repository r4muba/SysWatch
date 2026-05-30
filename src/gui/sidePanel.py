import ttkbootstrap as tb

class SidePanel (tb.Frame):
    def __init__(self, frame, controller):
        super().__init__(
            frame,
            bootstyle="info"
        )

        self._ctrl = controller
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
            text="Option 1",
            command=None
        )
        b1.pack(fill="x", padx=40, pady=20)

        b2 = tb.Button (
            self, 
            bootstyle="danger",
            text="Option 2",
            command=None
        )
        b2.pack(fill="x", padx=40, pady=20)

        b3 = tb.Button (
            self, 
            bootstyle="danger",
            text="Option 3",
            command=None
        )
        b3.pack(fill="x", padx=40, pady=20)

