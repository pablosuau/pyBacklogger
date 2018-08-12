'''
Code for the sort model, which is used to determine the games
sorting criteria
'''
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from models.constants import HEADERS, ORDER_ASCENDING

class SortListModel():
    '''
    Model to store sorting criteria
    '''
    def __init__(self):
        '''
        Initialises the model
        '''
        self.sort = QStandardItemModel()
        self.available = QStandardItemModel()
        for header in HEADERS:
            item = QStandardItem(header)
            item.setEditable(False)
            self.available.appendRow(item)
        self.in_sort = []
        self.saved_sort = None
        self.saved_available = None

    def save_model(self):
        '''
        Saves the current state of the model
        '''
        self.saved_sort = self.copy_model(self.sort)
        self.saved_available = self.copy_model(self.available)

    def restore_model(self):
        '''
        Restores the previous state of the model
        '''
        self.sort = self.copy_model(self.saved_sort)
        self.available = self.copy_model(self.saved_available)

    @staticmethod
    def copy_model(original):
        '''
        Auxiliar function to copy data between elements of the class
        by replicating all the elements of a list

        parameters:
            - original: the element of the model to be copied
        returns:
            - a copy of the original element of the model
        '''
        res = QStandardItemModel()
        for i in range(0, original.rowCount()):
            item = QStandardItem(str(original.item(i).text()))
            item.setEditable(False)
            res.appendRow(item)
        return res

    def to_sort(self, list_indexes):
        '''
        Moves a list of sorting criteria from the list of available
        sorting criteria to the list of selected sorting criteria

        parameters:
            - list_indexes: the index of the elements to be added
              to the list of selected sorting crtieria
        '''
        for index in list_indexes:
            item = str(self.available.itemFromIndex(index).text()) + \
                   ' (' + ORDER_ASCENDING + ')'
            item = QStandardItem(item)
            item.setEditable(False)
            self.sort.appendRow(item)
            self.available.removeRows(index.row(), 1)

    def to_available(self, list_indexes):
        '''
        Moves a list of sorting criteria from the list of selected sorting
        criteria to the list of available sorting criteria. The criteria
        are inserted in the list of available sorting criteria in the
        original order

        parameters:
            - list_indexes: the index of the elements to be added
              to the list of available sorting criteria
        '''
        for index in list_indexes:
            item = ' '.join(str(self.sort.itemFromIndex(index).text()).split(' ')[:-1])
            placed = False
            i = 0
            while not placed and i < self.available.rowCount():
                item_i = str(self.available.item(i).text())
                if HEADERS.index(item_i) > HEADERS.index(item):
                    placed = True
                else:
                    i = i + 1
            item = QStandardItem(item)
            item.setEditable(False)
            self.available.insertRow(i, item)
            self.sort.removeRows(index.row(), 1)

    def sort_up_down(self, index, mod):
        '''
        Modifies the position of an element in the list of selected
        sorting criteria

        parameters:
            - index: the index of the criterium in the list of
              selected criteria to be modified
            - mod: number of rows to move down (positive) or
              up (negative)
        returns:
            - the new index of the modified criterium
        '''
        item = str(self.sort.itemFromIndex(index).text())
        row = index.row()
        self.sort.removeRows(row, 1)
        item = QStandardItem(item)
        item.setEditable(False)
        self.sort.insertRow(row + mod, item)
        index = self.sort.index(row + mod, 0)
        return index

    def sort_down(self, index):
        '''
        Moves the position of an element in the selected sorting
        criteria one row down

        parameters:
            - index: the index of the criterium in the list of
              selected criteria to be modified
        returns:
            - the new index of the modified criterium
        '''
        return self.sort_up_down(index, 1)

    def sort_up(self, index):
        '''
        Moves the position of an element in the selected sorting
        criteria one row up

        parameters:
            - index: the index of the criterium in the list of
              selected criteria to be modified
        returns:
            - the new index of the modified criterium
        '''
        return self.sort_up_down(index, -1)

    def get_sort_order(self, list_indexes):
        '''
        Gets the sorting order for a sorting criterium

        parameters:
            - list_indexes: a list of elements in the selected
              sorting criteria list
        returns:
            - the sorting order (ascending/descending) of the first
              element in list_indexes
        '''
        item = str(self.sort.itemFromIndex(list_indexes[0]).text()).split(' ')
        return item[-1].split('(')[1].split(')')[0]

    def set_sort_order(self, list_indexes, order):
        '''
        Modifies the sorting order of a sorting criterium

        parameters:
            - list_indexes: a list of elements in the sorting criteria
              list
            - order: the sorting order (ascending/descending) to be assigned
              to the first element in the list of indexes
        '''
        item = str(self.sort.itemFromIndex(list_indexes[0]).text()).split(' ')
        item_text = ' '.join(item[:-1]) + ' (' + order + ')'
        new_item = QStandardItem(item_text)
        new_item.setEditable(False)
        row = list_indexes[0].row()
        self.sort.setItem(row, new_item)

    def get_sort_fields(self):
        '''
        Returns the currently selected sorting criteria

        returns:
            - a list of the fields which are currently selected
              as sorting criteria
            - for each of these fields, wheter the sorting order
              is ascending or descending
        '''
        fields = []
        order = []
        for row in range(0, self.sort.rowCount()):
            item = str(self.sort.item(row).text()).split(' ')
            fields.append(' '.join(item[:-1]))
            order.append(item[-1].split('(')[1].split(')')[0])
        return (fields, order)
