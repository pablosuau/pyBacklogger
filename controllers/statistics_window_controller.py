from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from views.statistics_dialog import Ui_StatisticsWindow

class StatisticsWindowController(QtGui.QDialog):
    # UI and signal setup
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
       
        self.ui = Ui_StatisticsWindow()
        self.ui.setupUi(self)
   
        self.initializeUi()     
        self.setupSignals()
    
    def initializeUi(self):
        self.buttons = [self.ui.pushButtonSystem, self.ui.pushButtonYear, self.ui.pushButtonLabel, self.ui.pushButtonStatus]
        # Make buttons checkable
        for b in self.buttons:
            b.setCheckable(True)
        
    def setupSignals(self):
        self.ui.pushButtonClose.clicked.connect(self.close_clicked)
        for b in self.buttons:
            b.clicked.connect(self.option_clicked)
        
    def close_clicked(self):
        self.close()
        
    def option_clicked(self):
        checked = 0
        for b in self.buttons:
            if b.isChecked():
                checked = checked + 1
                
        self.ui.plainTextEdit.clear()
        
        if checked > 2:
           self.ui.plainTextEdit.appendPlainText('Only two criteria can be selected')