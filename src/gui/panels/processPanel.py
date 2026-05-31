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

    def change(self, frame_1, frame_2):
        frame_1.pack_forget()
        frame_2.pack_forget()

        frame_1.pack(fill="both", expand =True)

    def _build(self):
        title = tb.Label (
            self,
            bootstyle="dark",
            text="Procesos",
            font=("Helvetica", 60, "bold")
        )
        title.pack(anchor="center", padx=30, pady=30)

        # Declaration

        aux_frame = tb.Frame(self, bootstyle="danger")
        aux_frame.pack(fill="both", expand =True)

        left_frame = tb.Frame(aux_frame, bootstyle="primary")
        right_frame = tb.Frame(aux_frame, bootstyle="secondary")

        table_frame = tb.Frame(right_frame,bootstyle="dark")
        graph_frame = tb.Frame(right_frame,bootstyle="light")

        table_btn = tb.Button(
            left_frame, 
            text="Tabla", 
            bootstyle="success", 
            command=lambda: self.change(table_frame,graph_frame)
        )

        graph_btn = tb.Button(
            left_frame, 
            text="Grafica", 
            bootstyle="danger",
            command=lambda: self.change(graph_frame,table_frame)
        )

        # Column configure

        aux_frame.columnconfigure(0, weight=2)
        aux_frame.columnconfigure(1, weight=6)
        aux_frame.rowconfigure(0, weight=1)

        left_frame.columnconfigure(0, weight=1)
        
        for i in range(4):  
            left_frame.rowconfigure(i, weight=1)



        right_frame.grid(row=0, column=1, sticky="nsew")
        left_frame.grid(row=0, column=0, sticky="nsew")

        table_btn.grid(row=1, column=0, sticky="nsew")
        graph_btn.grid(row=2, column=0, sticky="nsew")





    
    
