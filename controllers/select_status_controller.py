from PyQt4 import QtGui, QtCore
from views.status_dialog import Ui_StatusDialog
from models.status_model import StatusModel

class SelectStatusController(QtGui.QDialog):
    # UI and signal setup
    def __init__(self, status, parent):
        QtGui.QWidget.__init__(self, parent)

        self.previous_status = status  
        self.canceled = False
        
        self.ui = Ui_StatusDialog()
        self.ui.setupUi(self)
        
        self.initializeUi()
        
        self.setupSignals()
        
    def initializeUi(self):
        model = StatusModel()
        self.ui.comboBoxStatus.setModel(model)
        if self.previous_status != None:
            index = self.ui.comboBoxStatus.findText(self.previous_status, QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.ui.comboBoxStatus.setCurrentIndex(index)
    
    def setupSignals(self):
        self.ui.pushButtonOk.clicked.connect(self.pushButtonOkClicked)
        self.ui.pushButtonCancel.clicked.connect(self.pushButtonCancelClicked)
        
    def pushButtonOkClicked(self):
        self.canceled = False
        self.hide()
                
    def pushButtonCancelClicked(self):
        self.canceled = True
        self.hide()
    
    def getStatus(self):
        if self.canceled == True:
            return None
        else:
            return self.ui.comboBoxStatus.itemText(self.ui.comboBoxStatus.currentIndex())

    def getPreviousStatus(self):
        return self.previous_status