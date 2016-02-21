from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from dialogs.date_dialog import DateDialog

class DateWidget(QtGui.QWidget):
    def __init__(self, text, father):
        super(DateWidget, self).__init__()
        layout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel()
        self.label.setText(text)
        layout.addWidget(self.label)
        layout.setAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(layout)
        self.father = father
        
    def mousePressEvent(self, event):
        # Creating and displaying the dialog
        (date, result) = DateDialog.getDate(self.label.text())
        if result:
            self.label.setText(date)
            
    def toString(self):
        return(self.label.text())
     