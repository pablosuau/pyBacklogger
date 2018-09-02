'''
Code for the status model
'''
from PyQt5 import QtGui
from models.constants import OPTIONS_STATUS

class StatusModel(QtGui.QStandardItemModel):
    '''
    Model to store games' progress
    '''
    def __init__(self):
        '''
	    Initialises the model
        '''
        super(StatusModel, self).__init__()

        for k in OPTIONS_STATUS:
            item = QtGui.QStandardItem(k)
            self.appendRow(item)
