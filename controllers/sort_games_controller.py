from PyQt4 import QtGui
from views.sort_dialog import Ui_SortDialog

class SelectStatusController(QtGui.QDialog):
    # UI and signal setup
    def __init__(self, status, parent):
        QtGui.QWidget.__init__(self, parent)

        
        self.ui = Ui_SortDialog()
        self.ui.setupUi(self)
        
        self.initializeUi()
        
        self.setupSignals()