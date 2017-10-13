import constants
from PyQt5.QtGui import *

class SortListModel():
    def __init__(self):
        self.clear()
        
    def clear(self):
        self.sort = QStandardItemModel()
        self.available = QStandardItemModel()
        for h in constants.headers:
            item = QStandardItem(h)
            item.setEditable(False)
            self.available.appendRow(item)
        self.in_sort = []
        
    def save_model(self):
        self.saved_sort = self.copy_model(self.sort)
        self.saved_available = self.copy_model(self.available)
        
    def restore_model(self):
        self.sort = self.copy_model(self.saved_sort)
        self.available = self.copy_model(self.saved_available)
        
    def copy_model(self, original):
        res = QStandardItemModel()
        for i in range(0,original.rowCount()):
            item = QStandardItem(str(original.item(i).text()))
            item.setEditable(False)
            res.appendRow(item)
        return res
            
    def to_sort(self, list_indexes):
        for index in list_indexes:
            item = str(self.available.itemFromIndex(index).text()) + ' (' + constants.ORDER_ASCENDING + ')'
            item = QStandardItem(item)
            item.setEditable(False)
            self.sort.appendRow(item)
            self.available.removeRows(index.row(),1)
            
    def to_available(self, list_indexes): # A bit different, because I'd like the elements to be 
                                          # inserted back in the original order
        for index in list_indexes:
            item = ' '.join(str(self.sort.itemFromIndex(index).text()).split(' ')[:-1])
            placed = False
            i = 0
            while not placed and i < self.available.rowCount():
                item_i = str(self.available.item(i).text())
                if constants.headers.index(item_i)>constants.headers.index(item):
                    placed = True
                else:
                    i = i + 1
            item = QStandardItem(item)
            item.setEditable(False)
            self.available.insertRow(i, item)
            self.sort.removeRows(index.row(),1)
            
    def sort_up_down(self, index, mod):
        item = str(self.sort.itemFromIndex(index).text())
        row = index.row()
        self.sort.removeRows(row,1)
        item = QStandardItem(item)
        item.setEditable(False)
        self.sort.insertRow(row+mod, item)
        index = self.sort.index(row+mod,0)
        return index
            
    def sort_down(self, index):
        return self.sort_up_down(index, 1)
    
    def sort_up(self, index):
        return self.sort_up_down(index, -1)
        
    def get_sort_order(self, list_indexes):
        item = str(self.sort.itemFromIndex(list_indexes[0]).text()).split(' ')
        return item[-1].split('(')[1].split(')')[0]
    
    def set_sort_order(self, list_indexes, order):
        item = str(self.sort.itemFromIndex(list_indexes[0]).text()).split(' ')
        item_text = ' '.join(item[:-1]) + ' (' + order + ')'
        new_item = QStandardItem(item_text)
        new_item.setEditable(False)
        row = list_indexes[0].row()
        self.sort.setItem(row, new_item)
        
    def get_sort_fields(self):
        fields = []
        order = []
        for r in range(0, self.sort.rowCount()):
            item = str(self.sort.item(r).text()).split(' ')
            fields.append(' '.join(item[:-1]))
            order.append(item[-1].split('(')[1].split(')')[0])
        return (fields, order)        
    
    
            
    
            
        
