import psutil

class SystemData:
    def __init__(self):
        self.getRamData()
    
    def getRamData(self):
        '''
        https://psutil.readthedocs.io/stable/#psutil.virtual_memory
        '''
        return psutil.virtual_memory()
        