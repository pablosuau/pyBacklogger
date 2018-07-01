from PyQt5 import QtCore, Qt, QtWidgets
from views.filter_dialog import Ui_FilterDialog

class FilterGamesController(QtWidgets.QDialog):
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
        def assign_model(model, list_widget):
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
        def select_all(list_view):
            model_qt = list_view.model()
            for index in range(model_qt.rowCount()):
                item = model_qt.item(index)
                if item.isCheckable() and item.checkState() == QtCore.Qt.Unchecked:
                    item.setCheckState(QtCore.Qt.Checked)

        def deselect_all(list_view):
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
        self.canceled = False
        self.hide()

    def cancel_clicked(self):
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
        def apply_filtering_per_type(model, list_widget):
            model_qt = list_widget.model()
            for index in range(model_qt.rowCount()):
                item = model_qt.item(index)
                model.set_filtered(str(item.text()), item.checkState() != QtCore.Qt.Checked)

        if not self.canceled:
            apply_filtering_per_type(
                self.table.models['system_list_model'],
                self.ui.listSystem)
            apply_filtering_per_type(
                self.table.models['status_list_model'],
                self.ui.listStatus)
            apply_filtering_per_type(
                self.table.models['label_list_model'],
                self.ui.listLabel)
            apply_filtering_per_type(
                self.table.models['difficulty_list_model'],
                self.ui.listDifficulty)
            self.table.hide_rows()

        models = [self.table.models['system_list_model'],
                  self.table.models['status_list_model'],
                  self.table.models['label_list_model'],
                  self.table.models['difficulty_list_model']]
        model = 0
        while  model < len(models) and not models[model].is_any_filtered():
            model = model + 1
        self.filtering_all = model >= len(models)
