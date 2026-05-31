import threading
from time import sleep

class ThreadController:
    def __init__(self):
        ...

    def createThread(self, function):
        def loopingFunction():
            while True:
                function()
                sleep(1)

        thread = threading.Thread(target=loopingFunction)
        thread.start()