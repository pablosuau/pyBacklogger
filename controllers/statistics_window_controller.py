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
        pass        
        
    def setupSignals(self):
        pass