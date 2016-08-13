from PyQt4 import QtGui

OPTIONS = {
            'unplayed':  QtGui.QColor(155,0,0),
            'playing':   QtGui.QColor(0,0,155),
            'played':    QtGui.QColor(255,155,0),
            'completed': QtGui.QColor(0,155,0),
            'shelved':   QtGui.QColor(0,155,0)
}

class StatusModel(QtGui.QStandardItemModel):
    def __init__(self):
        super(StatusModel, self).__init__()

        for k in OPTIONS.keys():
            item = QtGui.QStandardItem(k)
            self.appendRow(item)

        
    def getColor(self, key):
        return OPTIONS[key]