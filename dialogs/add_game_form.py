from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class AddGameForm(QtGui.QDialog):
    def __init__(self, parent=None):
        super(AddGameForm, self).__init__(parent)
        self.setWindowTitle('Add game')
        self.main_frame = QWidget()
        
        radio_group = QtGui.QButtonGroup(self.main_frame) 
        self.radio_url = QtGui.QRadioButton("GameFAQs' url")
        radio_group.addButton(self.radio_url)
        self.radio_url.setChecked(True)
        self.radio_name = QtGui.QRadioButton("GameFAQs' name search")
        radio_group.addButton(self.radio_name)
        self.line_edit = QtGui.QLineEdit()
        self.line_edit.textChanged.connect(self.textChanged)
        self.button_ok = QtGui.QPushButton('Ok')
        self.button_ok.setEnabled(False)
        self.button_cancel = QtGui.QPushButton('Cancel')
        layout_buttons = QtGui.QHBoxLayout()
        layout_buttons.addWidget(self.button_ok)        
        layout_buttons.addWidget(self.button_cancel)        
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(QLabel("Add by:"))
        layout.addWidget(self.radio_url)
        layout.addWidget(self.radio_name)
        layout.addWidget(self.line_edit)
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
        
    def textChanged(self):
        if len(str(self.line_edit.text()))>0:
            self.button_ok.setEnabled(True)
        else:
            self.button_ok.setEnabled(False)
        