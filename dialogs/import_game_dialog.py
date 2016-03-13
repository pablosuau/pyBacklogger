from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *

IMPORT = 0
IGNORE = 1
KEEP = 2
STOP = 3

class ImportGameDialog(QDialog):
    def __init__(self, text, parent = None):
        super(ImportGameDialog, self).__init__(parent)

        layout = QtGui.QVBoxLayout(self)

        text = QtGui.QLabel(text)
                
        # Options
        self.options = QtGui.QButtonGroup(self) 
        self.importGame = QtGui.QRadioButton("Import")
        self.importGame.setChecked(True)
        self.options.addButton(self.importGame)
        self.ignoreGame = QtGui.QRadioButton("Ignore")
        self.options.addButton(self.ignoreGame)
        self.keepGame = QtGui.QRadioButton("Keep")
        self.options.addButton(self.keepGame)
        self.stopGame = QtGui.QRadioButton("Stop")
        self.options.addButton(self.stopGame)

        layout.addWidget(self.importGame)
        layout.addWidget(self.ignoreGame)
        layout.addWidget(self.keepGame)
        layout.addWidget(self.stopGame)
    
        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        
        layout.addWidget(buttons)
        self.setLayout(layout)

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getImportGame(text, parent = None):
        dialog = ImportGameDialog(text, parent)
        result = dialog.exec_()
        checked = dialog.options.checkedId()
                      
        return (checked, result == QDialog.Accepted)        