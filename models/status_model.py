from PyQt5 import QtGui
from models.constants import OPTIONS_STATUS

class StatusModel(QtGui.QStandardItemModel):
    def __init__(self):
        super(StatusModel, self).__init__()

        for k in OPTIONS_STATUS.keys():
            item = QtGui.QStandardItem(k)
            self.appendRow(item)

    def getColor(self, key):
        return OPTIONS_STATUS[key]
