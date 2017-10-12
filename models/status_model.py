from PyQt5 import QtGui
from models.constants import OPTIONS

class StatusModel(QtGui.QStandardItemModel):
    def __init__(self):
        super(StatusModel, self).__init__()

        for k in OPTIONS.keys():
            item = QtGui.QStandardItem(k)
            self.appendRow(item)

        
    def getColor(self, key):
        return OPTIONS[key]
