from PyQt4 import QtGui, QtCore
from views.select_date_dialog import Ui_SelectDateDialog

class SelectDateController(QtGui.QDialog):
    # UI and signal setup
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_SelectDateDialog()
        self.ui.setupUi(self)
        
        self.importing = None
        
        self.setupSignals()
