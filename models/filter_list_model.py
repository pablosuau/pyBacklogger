FILTERED = 'filtered'
COUNT = 'count'

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

    def add(self, item):
        if not item in self.list:
            self.list[item] = dict()
            self.list[item][FILTERED] = False
            self.list[item][COUNT] = 1
        else:
            self.list[item][COUNT] = self.list[item][COUNT] + 1
        
    def remove(self, item):
        if item in self.list:
            if self.list[item][COUNT] > 1:
                self.list[item][COUNT] = self.list[item][COUNT] - 1
            else:
                del self.list[item]
        
    def get_list(self):
        return sorted(list(self.list.keys()))
            
    def set_filtered(self, item, filtered):
        self.list[item][FILTERED] = filtered
        
    def get_filtered(self, item):
        return (self.list[item][FILTERED])
        
    def is_any_filtered(self):
        return True in [self.list[k][FILTERED] for k in self.list.keys()]
            