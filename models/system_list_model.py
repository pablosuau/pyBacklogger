import bisect

class SystemList():    
    def __init__(self):
        self.system_list = []
        self.system_filtered = []

    def add_system(self, system):
        # System names are sorted
        if not system in self.system_list:
            index = bisect.bisect_left(self.system_list, system)
            self.system_list.insert(index, system)
            self.system_filtered.insert(index, False)        
        
    def remove_system(self, system):
        if system in self.system_list:
            index = self.system_list.index(system)
            del self.system_list[index]
            del self.system_filtered[index]
            
    def modify_status(self, system, status):
        index = self.system_list.index(system)
        self.system_filtered[index] = status
            