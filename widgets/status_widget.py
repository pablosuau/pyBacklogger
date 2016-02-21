from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from dialogs.status_dialog import StatusDialog

class StatusWidget(QtGui.QWidget):
    def __init__(self, text, father):
        super(StatusWidget, self).__init__()
        layout = QtGui.QHBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignLeft)
        self.label = QtGui.QLabel()
        self.label.setText(text)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.father = father

    def toString(self):
        return self.label.text()
        
    def mousePressEvent(self, event):
        (status, accepted) = StatusDialog.getStatus(self.label.text())
        if accepted:
            self.label.setText(status)
            self.father.hide_rows_already()
            self.father.resizeColumnsToContents()
            