import ttkbootstrap as tb
import threading

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

        totalText = tb.Label(
            self,
            text="TOTAL",
            font=("Helvetica", 24, "bold"),
            bootstyle="warning"
        )
        totalText.place(x=100, y=100)

        memoryData = self._systemData.getMemoryData()

        self.memory_available = tb.Meter(
            master=self,
            metersize=200,
            amountused=0,           # Empezamos en 0%
            amounttotal=memoryData.total/self._MB,        # El total
            metertype="semi",       # Estilo velocímetro
            textright="MB",    
            subtext="uso RAM",    
            bootstyle="success",    
            interactive=False       # El usuario no lo puede mover con el mouse
        )
        self.memory_available.place(x=100,y=200)

        self.memory_available = tb.Meter(
            master=self,
            metersize=200,
            amountused=0,           # Empezamos en 0%
            amounttotal=memoryData.total/self._MB,        # El total
            metertype="semi",       # Estilo velocímetro
            textright="MB",    
            subtext="uso RAM",    
            bootstyle="success",    
            interactive=False       # El usuario no lo puede mover con el mouse
        )
        self.memory_available.place(x=100,y=200)

        self._threadController.createThread(self.actualizar_ram)

    # 2. Función para actualizar el valor dinámicamente
    def actualizar_ram(self):
        memoryData = self._systemData.getMemoryData()

        used_mb = memoryData.used / self._MB

        self.memory_available.configure(amountused=used_mb)