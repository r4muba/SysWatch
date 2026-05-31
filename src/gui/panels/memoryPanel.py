import ttkbootstrap as tb
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MemoryPanel(tb.Frame):
    
    _MB = 1024 * 1024

    def __init__(self, frame, systemData, threadController):
        super().__init__(
            frame,
            style="success"
        )
        self._systemData = systemData
        self._threadController = threadController

        self.build()

    def build(self):
        title = tb.Label(
            self,
            text="Gestión de Memoria: Páginas, Marcos y Fallos",
            font=("Helvetica", 24, "bold"),
            bootstyle="warning"
        )
        title.pack(anchor="w", padx=30, pady=20)

################ RAM var #################33333
        memoryData = self._systemData.getMemoryData()
        self.total_mb = memoryData.total / self._MB

        totalText = tb.Label(
            self,
            text=f"TOTAL: {round(self.total_mb)} MB", # <-- Aquí está la magia
            font=("Helvetica", 24, "bold"),
            bootstyle="warning"
        )
        totalText.place(x=100, y=100)
        self.memory_in_use = tb.Meter(
            master=self,
            metersize=150,
            amountused=0,           # Empezamos en 0%
            amounttotal=100,        # <--- FIJO EN 100 para que la barra se mida en porcentaje
            metertype="semi",       # Estilo velocímetro
            textright="%",          # Añade el símbolo de % al lado del número
            subtext="uso RAM",    
            bootstyle="success",    
            interactive=False       # El usuario no lo puede mover con el mouse
        )
        self.memory_in_use.place(x=100, y=200)

        self.memory_available = tb.Meter(
            master=self,
            metersize=150,
            amountused=0,           # Empezamos en 0%
            amounttotal=self.total_mb,        # El total
            metertype="semi",       # Estilo velocímetro
            textright="MB",    
            subtext="de RAM libre",    
            bootstyle="success",    
            interactive=False       # El usuario no lo puede mover con el mouse
        )
        self.memory_available.place(x=300,y=200)

######################### swap var ###############################

        swapData = self._systemData.getSwapData()

        self.swap_var = tb.Meter(
            master=self,
            metersize=150,
            amountused=0,           # Empezamos en 0%
            amounttotal=swapData.total / self._MB,        # El total
            metertype="semi",       # Estilo velocímetro
            textright="MB",    
            subtext="memoria para swaps",    
            bootstyle="success",    
            interactive=False       # El usuario no lo puede mover con el mouse
        )
        self.swap_var.place(x=500,y=200)

################# hilos ############################################################

        self._threadController.createThread(self.actualizar_ram)

    # 2. Función para actualizar el valor dinámicamente
    def actualizar_ram(self):
        try:
            memoryData = self._systemData.getMemoryData()
            swapData = self._systemData.getSwapData() # <-- Traemos los datos frescos del swap

            used_mb = memoryData.used / self._MB
            free_mb = memoryData.free / self._MB

            num_swaps = swapData.used / self._MB

            porcentaje_uso = (used_mb / self.total_mb) * 100

            self.memory_in_use.configure(amountused=porcentaje_uso)
            self.memory_available.configure(amountused=free_mb)
            self.swap_var.configure(amountused=num_swaps)

        except Exception as e:
            print("Err")