import ttkbootstrap as tb

class GeneralPanel(tb.Frame):
    def __init__(self, frame, controller):
        super().__init__(
            frame,
            style="success"
        )
        self._ctrl = controller
