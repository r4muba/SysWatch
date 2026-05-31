import threading

class ThreadController:
    def __init__(self):
        ...

    def createThread(self, function):
        thread = threading.Thread(target=function)
        thread.start()