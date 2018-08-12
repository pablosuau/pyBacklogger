'''
Code for the filter model, which is used to determine
which elements of the backlog to show
'''
from models.constants import FILTERED, COUNT

class FilterListModel():
    '''
    Model for filtering data
    '''
    def __init__(self, initial_entries=None):
        '''
        Initialises the model

        parameters:
            -initial_entries: default values for the model
        '''
        self.initial_entries = initial_entries
        self.clear()

    def clear(self):
        '''
        Auxiliar function to initalise the model and assign
        the default values
        '''
        self.list = dict()
        if self.initial_entries != None:
            if isinstance(self.initial_entries, list):
                for i in self.initial_entries:
                    self.add(i)
            else:
                self.add(self.initial_entries)

    def clear_filtered(self):
        '''
        Sets all the elements in the model as unfiltered
        '''
        for k in self.list:
            self.list[k][FILTERED] = False

    def add(self, item):
        '''
        Adds an element to the model

        parameters:
            - item: the element to add to the mdoel
        '''
        item = str(item)
        if item not in self.list.keys():
            self.list[item] = dict()
            self.list[item][FILTERED] = False
            self.list[item][COUNT] = 1
        else:
            self.list[item][COUNT] = self.list[item][COUNT] + 1

    def remove(self, item):
        '''
        Removes an element from the model

        parameters:
            - item: the element to remove from the model
        '''
        item = str(item)
        if item in self.list.keys():
            if self.list[item][COUNT] > 1:
                self.list[item][COUNT] = self.list[item][COUNT] - 1
            else:
                del self.list[item]

    def get_list(self):
        '''
        Extracts a list of the elements in the model

        returns:
            - a list which contains all the elements included in themodel
        '''
        return sorted(list(self.list.keys()))

    def set_filtered(self, item, filtered):
        '''
        Modifies the status of one element in the model

        parameters:
            - item: the element for which we are modifying the status
            - filtered: a boolean which indicates whether the element
              is filtered or note
        '''
        item = str(item)
        self.list[item][FILTERED] = filtered

    def get_filtered(self, item):
        '''
        Retrieves the status of one element

        parameters:
            - item: the queried element
        returns:
            - A boolean value which indicates whether the element is filtered
              or not
        '''
        item = str(item)
        return self.list[item][FILTERED]

    def is_any_filtered(self):
        '''
        Determines whether any of the elements in the model is filtered

        returns:
            - True if any of the elements in the model is filtered, False
              otherwise
        '''
        return True in [self.list[k][FILTERED] for k in self.list]
            