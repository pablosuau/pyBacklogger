FILTERED = 'filtered'
COUNT = 'count'

class StatusListModel():    
    def __init__(self):
        self.system_list = dict()
        
    def clear(self):
        self.system_list = dict()

    def add_status(self, system):
        if not system in self.system_list:
            self.system_list[system] = dict()
            self.system_list[system][FILTERED] = False
            self.system_list[system][COUNT] = 1
        else:
            self.system_list[system][COUNT] = self.system_list[system][COUNT] + 1
        
    def remove_status(self, system):
        if system in self.system_list:
            if self.system_list[system][COUNT] > 1:
                self.system_list[system][COUNT] = self.system_list[system][COUNT] - 1
            else:
                del self.system_list[system]
        
    def get_status_list(self):
        return sorted(list(self.system_list.keys()))
            
    def set_filtered(self, system, filtered):
        self.system_list[system][FILTERED] = filtered
        
    def get_filtered(self, system):
        return (self.system_list[system][FILTERED])
        
    def is_any_filtered(self):
        return True in [self.system_list[k][FILTERED] for k in self.system_list.keys()]
            