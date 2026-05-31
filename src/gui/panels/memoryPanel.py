import ttkbootstrap as tb
import threading

class MemoryPanel(tb.Frame):
    _GB = 1024 * 1024 * 1024
    def __init__(self, frame, systemData):
        super().__init__(
            frame,
            style="success"
        )
        self._systemData = systemData
        self.build()

    def build(self):
        title = tb.Label(
            self,
            text="Gestión de Memoria: Páginas, Marcos y Fallos",
            font=("Helvetica", 24, "bold"),
            bootstyle="warning"
        )
        title.pack(anchor="w", padx=30, pady=20)

        memoryData = self._systemData.getMemoryData()

        self.memory_available = tb.Meter(
            master=self,
            metersize=200,
            amountused=0,           # Empezamos en 0%
            amounttotal=memoryData.total/self._GB,        # El límite es 100%
            metertype="semi",       # Estilo velocímetro
            subtext="% Uso RAM",    
            bootstyle="success",    
            interactive=False       # El usuario no lo puede mover con el mouse
        )
        self.memory_available.pack(pady=100)

        thread = threading.Thread(target=self.actualizar_ram)
        thread.start()

    # 2. Función para actualizar el valor dinámicamente
    def actualizar_ram(self):
        while True:
            memoryData = self._systemData.getMemoryData()
            self.memory_available.configure(amountused=memoryData.used/self._GB)