import ttkbootstrap as tb

class ProcessPanel(tb.Frame):
    def __init__(self, frame, systemData, threadController):
        super().__init__(
            frame,
            style="success"
        )
        self._systemData = systemData
        self._threadController = threadController

        self._build()

    def _build(self):
        title = tb.Label (
            self,
            bootstyle="dark",
            text="Procesos",
            font=("Helvetica", 60, "bold")
        )
        title.pack(anchor="center", padx=30, pady=30)

        aux_frame = tb.Frame(self, bootstyle="danger")
        aux_frame.pack(fill="both", expand =True)

        aux_frame.columnconfigure(0, weight=2)
        aux_frame.columnconfigure(1, weight=6)
        aux_frame.rowconfigure(0, weight=1)

        left_frame = tb.Frame(aux_frame, bootstyle="primary")
        left_frame.columnconfigure(0, weight=1)
        
        for i in range(4):  
            left_frame.rowconfigure(i, weight=1)


        right_frame = tb.Frame(aux_frame, bootstyle="secondary")

        right_frame.grid(row=0, column=1, sticky="nsew")
        left_frame.grid(row=0, column=0, sticky="nsew")

        table_btn = tb.Button(left_frame, text="Tabla", bootstyle="success")
        table_btn.grid(row=1, column=0, sticky="nsew")

        graph_btn = tb.Button(left_frame, text="Grafica", bootstyle="danger")
        graph_btn.grid(row=2, column=0, sticky="nsew")





    
    
