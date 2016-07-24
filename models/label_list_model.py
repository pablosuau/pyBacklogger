FILTERED = 'filtered'
COUNT = 'count'

class LabelListModel():    
    def __init__(self):
        self.label_list = dict()
        self.add_label('---None---')
        
    def clear(self):
        self.label_list = dict()
        self.add_label('---None---')

    def add_label(self, label):
        if not label in self.label_list:
            self.label_list[label] = dict()
            self.label_list[label][FILTERED] = False
            self.label_list[label][COUNT] = 1
        else:
            self.label_list[label][COUNT] = self.label_list[label][COUNT] + 1
        
    def remove_label(self, label):
        if label in self.label_list:
            if self.label_list[label][COUNT] > 1:
                self.label_list[label][COUNT] = self.label_list[label][COUNT] - 1
            else:
                del self.label_list[label]
        
    def get_label_list(self):
        return sorted(list(self.label_list.keys()))
            
    def set_filtered(self, label, filtered):
        self.label_list[label][FILTERED] = filtered
        
    def get_filtered(self, label):
        return (self.label_list[label][FILTERED])
        
    def is_any_filtered(self):
        return True in [self.label_list[k][FILTERED] for k in self.label_list.keys()]
            