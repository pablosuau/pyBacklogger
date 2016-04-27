from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *

options = [
            'unplayed', 
            'playing',
            'played',
            'completed',
            'shelved'
          ]
          
colors = [
            QtGui.QColor(155,0,0),
            QtGui.QColor(0,0,155),
            QtGui.QColor(255,155,0),
            QtGui.QColor(0,155,0),
            QtGui.QColor(0,155,0)
         ]

class StatusDialog(QDialog):
    def __init__(self, option, parent = None):
        super(StatusDialog, self).__init__(parent)

        layout = QtGui.QVBoxLayout(self)
        
        self.options = QtGui.QComboBox()
        for o in options:
            self.options.addItem(o)
        self.options.setCurrentIndex(options.index(option))
        
        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        
        self.accepted = False        
        
        layout.addWidget(self.options)
        layout.addWidget(buttons)
        self.setLayout(layout)

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getStatus(status, parent = None):
        dialog = StatusDialog(status, parent)
        result = dialog.exec_()
        status = dialog.options.currentText()
        color = colors[dialog.options.currentIndex()]
                      
        return (status, color, result == QDialog.Accepted)        