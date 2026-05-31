import psutil

class SystemData:
    def __init__(self):
        ...
    
    def getMemoryData(self):
        '''
        https://psutil.readthedocs.io/stable/#psutil.virtual_memory
        '''
        
        return psutil.virtual_memory()
    
    def getSwapData(self):
        '''
        https://psutil.readthedocs.io/stable/#psutil.swap_memory
        '''
        
        return psutil.swap_memory()
        
    def getProcessesData(self):
        '''
        https://psutil.readthedocs.io/stable/#processes
        '''
        
        processes = []

        for proc in psutil.process_iter(['pid', 'name', 'status', 'nice', 'cpu_percent', 'memory_info']):
            process = dict()
            process['pid'] = proc.info['pid']
            process['name'] = proc.info['name']
            process['status'] = proc.info['status']
            process['nice'] = proc.info['nice']
            process['cpu_percent'] = proc.info['cpu_percent']
            process['memory_usage'] = proc.info['memory_info'].rss
            processes.append(process)

        return processes