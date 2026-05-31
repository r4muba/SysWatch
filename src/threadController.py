import threading
from time import sleep

class ThreadController:
    _stop_event = threading.Event()
    _threads = []

    def __init__(self):
        ...

    def createThread(self, function):
        def loopingFunction():
            while True:
                function()
                sleep(0.2)
            

        thread = threading.Thread(daemon=True, target=loopingFunction)
        thread.start()
        self._threads.append(thread)
