from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *

options = [
            'Darkadia'
          ]

class ImportSourceDialog(QDialog):
    def __init__(self, parent = None):
        super(ImportSourceDialog, self).__init__(parent)

        layout = QtGui.QVBoxLayout(self)
        
        self.options = QtGui.QComboBox()
        for o in options:
            self.options.addItem(o)
        
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
    def getImportSource(parent = None):
        dialog = ImportSourceDialog(parent)
        result = dialog.exec_()
        source = dialog.options.currentText()
                      
        return (source, result == QDialog.Accepted)        