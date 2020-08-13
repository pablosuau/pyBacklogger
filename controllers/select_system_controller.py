'''
Code to control the system selection interface. It allows to select the game's
specific system among all the options provided by rawg's api
'''
from PyQt5 import QtGui, QtCore, QtWidgets
from views.select_system_dialog import Ui_SelectSystemDialog

class SearchResultsController(QtWidgets.QDialog):
    '''
    Controller of the dialog to select a game system
    '''
    def __init__(self, systems, parent = None):
        '''
        Initialises the user interface and sets up the signals

        parameters:
            - parent: the controller which is the parent of the search results dialog
            - systems: a list with the systems to display
        '''
        super(SearchResultsController, self).__init__(parent)

        self.view = Ui_SearchResultsDialog()
        self.view.setupUi(self)

        self.systems = systems
        self.canceled = False

        self.initialize_ui()
        self.setup_signals()

    def initialize_ui(self):
        '''
        Fills the view with the elements of the system list
        '''
        model = QtGui.QStandardItemModel()
        for system in self.systems:
        	item = QtGui.QStandardItem(system)
        	item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setData(QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)
            model.appendRow(item)
        self.view.listViewSystems.setModel(model)

        self.view.pushButtonOk.setEnabled(False)

    def setup_signals(self):
        '''
        Connects the user interface control events to the corresponding signals
        '''
        self.view.pushButtonOk.clicked.connect(self.ok_clicked)
        self.view.pushButtonCancel.clicked.connect(self.cancel_clicked)

    def ok_clicked(self):
        '''
        Signal slot for the event of pressing the ok button
        '''
        self.hide()

    def cancel_clicked(self):
        '''
        Signal slot for the event of pressing the cancel button
        '''
        self.hide()
        self.canceled = True

    def closeEvent(self, _event):
        '''
        Signal slot for the event of closing the window. The event parameter is unused.
        '''
        # pylint: disable=invalid-name
        # pylint: disable=unused-argument
        self.canceled = True

    def on_item_changed(self, item):
        '''
        Modifies the behaviour of the items in the list so they behave like radio buttons
        '''
        if item.checkState() == QtCore.Qt.Checked:
            self.checked = self.checked + 1
            if self.checked == 1:
                self.view.pushButtonOk.setEnabled(True)
        else:
            self.checked = self.checked - 1
            if self.checked == 0:
                self.view.pushButtonOk.setEnabled(False)
