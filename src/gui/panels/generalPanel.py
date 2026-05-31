import ttkbootstrap as tb

class GeneralPanel(tb.Frame):
    def __init__(self, frame, systemData, threadController):
        super().__init__(
            frame,
            style="success"
        )
        self._systemData = systemData
        self._threadController = threadController
