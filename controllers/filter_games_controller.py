'''
This module controls the dialog to set filter criteria
'''

from PyQt5 import QtCore, Qt, QtWidgets
from views.filter_dialog import Ui_FilterDialog

class FilterGamesController(QtWidgets.QDialog):
    '''
    Controller object for the filter games dialog.
    '''
    def __init__(self, table, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.user_interface = Ui_FilterDialog()
        self.user_interface.setupUi(self)

        self.table = table
        self.canceled = False
        self.filtering_all = True

        self.initialize_ui()
        self.setup_signals()

    def initialize_ui(self):
        '''
        Connects interface's sections with their corresponding models
        '''
        def assign_model(model, list_widget):
            '''
            Private function to populate a specific section in the
            dialog with the values stored in a model

            parameters:
                - model: the model assigned to the dialog section
                - list_widget: the list widget to be populated
            '''
            model_qt = Qt.QStandardItemModel()
            values_list = model.get_list()
            for value in values_list:
                item = Qt.QStandardItem(value)
                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setData(QtCore.Qt.Checked, QtCore.Qt.CheckStateRole)
                if model.get_filtered(value):
                    item.setCheckState(QtCore.Qt.Unchecked)
                model_qt.appendRow(item)
            list_widget.setModel(model_qt)

        assign_model(self.table.models['system_list_model'], self.user_interface.listSystem)
        assign_model(self.table.models['status_list_model'], self.user_interface.listStatus)
        assign_model(self.table.models['label_list_model'], self.user_interface.listLabel)
        assign_model(self.table.models['difficulty_list_model'], self.user_interface.listDifficulty)

    def setup_signals(self):
        '''
        Connects interface's widgets signals to the corresponding slots
        '''
        def select_all(list_view):
            '''
            Generic callback for a 'select all' button

            parameters:
                -list_view: the list affected when the user clicks 'select all'
            '''
            model_qt = list_view.model()
            for index in range(model_qt.rowCount()):
                item = model_qt.item(index)
                if item.isCheckable() and item.checkState() == QtCore.Qt.Unchecked:
                    item.setCheckState(QtCore.Qt.Checked)

        def deselect_all(list_view):
            '''
            Generic callback for a 'deselect all' button

            parameters:
                - list_view: the list affected when the user clicks 'deselect all'
            '''
            model_qt = list_view.model()
            for index in range(model_qt.rowCount()):
                item = model_qt.item(index)
                if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                    item.setCheckState(QtCore.Qt.Unchecked)

        self.user_interface.pushButtonSelectAllSystem.clicked.connect(
            lambda: select_all(self.user_interface.listSystem))
        self.user_interface.pushButtonDeselectAllSystem.clicked.connect(
            lambda: deselect_all(self.user_interface.listSystem))
        self.user_interface.pushButtonSelectAllStatus.clicked.connect(
            lambda: select_all(self.user_interface.listStatus))
        self.user_interface.pushButtonDeselectAllStatus.clicked.connect(
            lambda: deselect_all(self.user_interface.listStatus))
        self.user_interface.pushButtonSelectAllLabel.clicked.connect(
            lambda: select_all(self.user_interface.listLabel))
        self.user_interface.pushButtonDeselectAllLabel.clicked.connect(
            lambda: deselect_all(self.user_interface.listLabel))
        self.user_interface.pushButtonSelectAllDifficulty.clicked.connect(
            lambda: select_all(self.user_interface.listDifficulty))
        self.user_interface.pushButtonDeselectAllDifficulty.clicked.connect(
            lambda: deselect_all(self.user_interface.listDifficulty))
        self.user_interface.pushButtonOk.clicked.connect(self.ok_clicked)
        self.user_interface.pushButtonCancel.clicked.connect(self.cancel_clicked)

    def ok_clicked(self):
        '''
        Callback for when the user clicks the 'ok' button. The dialog is closed and
        the parent is informed by means of an attribute that the changes have to
        take effect
        '''
        self.canceled = False
        self.hide()

    def cancel_clicked(self):
        '''
        Callback for when the user clicks the 'cancel' button. The dialog is closed
        and the parent is informed by means of an attribute that changes shouldn't
        take effect
        '''
        self.canceled = True
        self.hide()

    def closeEvent(self, event):
        '''
        Overriding the closeEvent from the QDialog class. This tells the main window
        controller to behave as if the Cancel button was pressed.

        parameters:
            - event: the passed event (not used in this overriden version)
        '''
        # pylint: disable=invalid-name
        # pylint: disable=unused-argument
        self.canceled = True

    def apply_filtering(self):
        '''
        Updates the models with information about which values to be filted
        '''
        def apply_filtering_per_type(model, list_widget):
            '''
            Updates a specific model

            parameters:
                - model: the model to be updated
                - list_widget: the list associated to that model
            '''
            model_qt = list_widget.model()
            for index in range(model_qt.rowCount()):
                item = model_qt.item(index)
                model.set_filtered(str(item.text()), item.checkState() != QtCore.Qt.Checked)

        if not self.canceled:
            apply_filtering_per_type(
                self.table.models['system_list_model'],
                self.user_interface.listSystem)
            apply_filtering_per_type(
                self.table.models['status_list_model'],
                self.user_interface.listStatus)
            apply_filtering_per_type(
                self.table.models['label_list_model'],
                self.user_interface.listLabel)
            apply_filtering_per_type(
                self.table.models['difficulty_list_model'],
                self.user_interface.listDifficulty)
            self.table.hide_rows()

        models = [self.table.models['system_list_model'],
                  self.table.models['status_list_model'],
                  self.table.models['label_list_model'],
                  self.table.models['difficulty_list_model']]
        model = 0
        while  model < len(models) and not models[model].is_any_filtered():
            model = model + 1
        self.filtering_all = model >= len(models)
