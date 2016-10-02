from constants import headers
from PyQt4.QtGui import *

class SortListModel():
    def __init__(self):
        self.clear()
        
    def clear(self):
        self.sort = QStandardItemModel()
        self.available = QStandardItemModel()
        for h in headers:
            item = QStandardItem(h)
            self.available.appendRow(item)
        self.in_sort = []
            
    def to_sort(self, list_indexes):
        for index in list_indexes:
            item = self.available.itemFromIndex(index).text()
            self.sort.appendRow(QStandardItem(item))
            self.available.removeRows(index.row(),1)
            
    def to_available(self, list_indexes): # A bit different, because I'd like the elements to be 
                                          # inserted back in the original order
        for index in list_indexes:
            item = self.sort.itemFromIndex(index).text()
            placed = False
            i = 0
            while not placed and i < self.available.rowCount():
                item_i = self.available.item(i).text()
                if headers.index(item_i)>headers.index(item):
                    placed = True
                else:
                    i = i + 1
            self.available.insertRow(i, QStandardItem(item))
            self.sort.removeRows(index.row(),1)
            
    def sort_up_down(self, index, mod):
        item = self.sort.itemFromIndex(index).text()
        row = index.row()
        self.sort.removeRows(row,1)
        self.sort.insertRow(row+mod, QStandardItem(item))
        index = self.sort.index(row+mod,0)
        return index
            
    def sort_down(self, index):
        return self.sort_up_down(index, 1)
    
    def sort_up(self, index):
        return self.sort_up_down(index, -1)
        
    def get_sort_fields(self):
        fields = []
        for r in range(0, self.sort.rowCount()):
            fields.append(self.sort.item(r).text())
        return fields        
    
    
            
    
            
        