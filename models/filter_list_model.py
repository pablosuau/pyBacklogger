from models.constants import FILTERED, COUNT

class FilterListModel():    
    def __init__(self, initial_entries=None):
        self.initial_entries = initial_entries
        self.clear()
        
    def clear(self):
        self.list = dict()
        if self.initial_entries != None:
            if type(self.initial_entries) == list:
                for i in self.initial_entries:
                    self.add(i)
            else:
                self.add(self.initial_entries)
                
    def clear_filtered(self):
        for k in self.list.keys():
            self.list[k][FILTERED] = False

    def add(self, item):
        item = str(item)
        if not item in self.list.keys():
            self.list[item] = dict()
            self.list[item][FILTERED] = False
            self.list[item][COUNT] = 1
        else:
            self.list[item][COUNT] = self.list[item][COUNT] + 1
        
    def remove(self, item):
        item = str(item)
        if item in self.list.keys():
            if self.list[item][COUNT] > 1:
                self.list[item][COUNT] = self.list[item][COUNT] - 1
            else:
                del self.list[item]
        
    def get_list(self):
        return sorted(list(self.list.keys()))
            
    def set_filtered(self, item, filtered):
        item = str(item)
        self.list[item][FILTERED] = filtered
        
    def get_filtered(self, item):
        item = str(item)
        return (self.list[item][FILTERED])
        
    def is_any_filtered(self):
        return True in [self.list[k][FILTERED] for k in self.list.keys()]
            