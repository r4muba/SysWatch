import ttkbootstrap as tb

class MemoryPanel(tb.Frame):
    def __init__(self, frame, controller):
        super().__init__(
            frame,
            style="success"
        )
        self._ctrl = controller
