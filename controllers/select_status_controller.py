'''
Code to control the select status interface. It lets the user
set the status of a game as played, playing, completed, etc.
'''

from PyQt5 import QtCore, QtWidgets
from views.status_dialog import Ui_StatusDialog
from models.status_model import StatusModel

class SelectStatusController(QtWidgets.QDialog):
    '''
    Controller for the select status dialog
    '''
    def __init__(self, status, parent):
        '''
        Initialises the user interface and sets up the signals

        parameters:
            - status: the current status value of the selected cell
            - parent: the controller which is the parent of the search results dialog
        '''
        QtWidgets.QDialog.__init__(self, parent)

        self.previous_status = status
        self.canceled = False

        self.user_interface = Ui_StatusDialog()
        self.user_interface.setupUi(self)

        self.initialize_ui()

        self.setup_signals()

    def initialize_ui(self):
        '''
        Populates the interface and selects the current status
        '''
        model = StatusModel()
        self.user_interface.comboBoxStatus.setModel(model)
        if self.previous_status != None:
            index = self.user_interface.comboBoxStatus.findText(
                self.previous_status, QtCore.Qt.MatchFixedString
            )
            if index >= 0:
                self.user_interface.comboBoxStatus.setCurrentIndex(index)

    def setup_signals(self):
        '''
        Connects the user interface control events to the corresponding signals
        '''
        self.user_interface.pushButtonOk.clicked.connect(self.push_button_ok_clicked)
        self.user_interface.pushButtonCancel.clicked.connect(self.push_button_cancel_clicked)

    def push_button_ok_clicked(self):
        '''
        Signal slot for the event of pressing the ok button
        '''
        self.canceled = False
        self.hide()

    def push_button_cancel_clicked(self):
        '''
        Signal slot for the event of pressing the cancel button
        '''
        self.canceled = True
        self.hide()

    def closeEvent(self, event):
        '''
        Signal slot for the event of closing the window. The event parameter is unused.
        '''
        # pylint: disable=invalid-name
        # pylint: disable=unused-argument
        self.canceled = True

    def get_status(self):
        '''
        Returns the selected status value
        '''
        ret = None

        if not self.canceled:
            ret = self.user_interface.comboBoxStatus.itemText(
                self.user_interface.comboBoxStatus.currentIndex())

        return ret

    def get_previous_status(self):
        '''
        Returns the previous selected status value
        '''
        return self.previous_status
