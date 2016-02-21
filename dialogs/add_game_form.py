from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class AddGameForm(QtGui.QDialog):
    def __init__(self, parent=None):
        super(AddGameForm, self).__init__(parent)
        self.setWindowTitle('Add game')
        self.main_frame = QWidget()
        
        self.url = QtGui.QLineEdit()
        self.button_ok = QtGui.QPushButton('Ok')
        self.button_cancel = QtGui.QPushButton('Cancel')
        layout_buttons = QtGui.QHBoxLayout()
        layout_buttons.addWidget(self.button_ok)        
        layout_buttons.addWidget(self.button_cancel)        
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(QLabel("GameFAQs' url:"))
        layout.addWidget(self.url)
        layout.addLayout(layout_buttons)
        
        self.setLayout(layout)
        
        self.ok = False
        
        self.button_ok.clicked.connect(self.okClicked)
        self.button_cancel.clicked.connect(self.cancelClicked)
        
    def okClicked(self):
        self.ok = True
        self.close()
    
    def cancelClicked(self):
        self.ok = False
        self.close()
        