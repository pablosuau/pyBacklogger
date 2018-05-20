from PyQt5 import QtGui, QtCore, Qt, QtWidgets
from views.filter_dialog import Ui_FilterDialog

class FilterGamesController(QtWidgets.QDialog):
    def __init__(self, table, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_FilterDialog()
        self.ui.setupUi(self)

        self.table = table
        self.canceled = False
        self.filtering_all = True

        self.initializeUi()
        self.setupSignals()

    def initializeUi(self):
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

        assign_model(self.table.models['system_list_model'], self.ui.listSystem)
        assign_model(self.table.models['status_list_model'], self.ui.listStatus)
        assign_model(self.table.models['label_list_model'], self.ui.listLabel)
        assign_model(self.table.models['difficulty_list_model'], self.ui.listDifficulty)

    def setupSignals(self):
        self.ui.pushButtonSelectAllSystem.clicked.connect(
            lambda: self.select_all(self.ui.listSystem))
        self.ui.pushButtonDeselectAllSystem.clicked.connect(
            lambda: self.deselect_all(self.ui.listSystem))
        self.ui.pushButtonSelectAllStatus.clicked.connect(
            lambda: self.select_all(self.ui.listStatus))
        self.ui.pushButtonDeselectAllStatus.clicked.connect(
            lambda: self.deselect_all(self.ui.listStatus))
        self.ui.pushButtonSelectAllLabel.clicked.connect(
            lambda: self.select_all(self.ui.listLabel))
        self.ui.pushButtonDeselectAllLabel.clicked.connect(
            lambda: self.deselect_all(self.ui.listLabel))
        self.ui.pushButtonSelectAllDifficulty.clicked.connect(
            lambda: self.select_all(self.ui.listDifficulty))
        self.ui.pushButtonDeselectAllDifficulty.clicked.connect(
            lambda: self.deselect_all(self.ui.listDifficulty))
        self.ui.pushButtonOk.clicked.connect(self.ok_clicked)
        self.ui.pushButtonCancel.clicked.connect(self.cancel_clicked)

    def select_all(self, list_view):
        model_qt = list_view.model()
        for index in range(model_qt.rowCount()):
            item = model_qt.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Unchecked:
                item.setCheckState(QtCore.Qt.Checked)

    def deselect_all(self, list_view):
        model_qt = list_view.model()
        for index in range(model_qt.rowCount()):
            item = model_qt.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)

    def ok_clicked(self):
        self.canceled = False
        self.hide()

    def cancel_clicked(self):
        self.canceled = True
        self.hide()

    def closeEvent(self, event):
        self.canceled = True

    def applyFiltering(self):
        def applyFilteringPerType(model, list_widget):
            model_qt = list_widget.model()
            for index in range(model_qt.rowCount()):
                item = model_qt.item(index)
                model.set_filtered(str(item.text()), item.checkState() != QtCore.Qt.Checked)

        if not self.canceled:
            applyFilteringPerType(self.table.models['system_list_model'], self.ui.listSystem)
            applyFilteringPerType(self.table.models['status_list_model'], self.ui.listStatus)
            applyFilteringPerType(self.table.models['label_list_model'], self.ui.listLabel)
            applyFilteringPerType(self.table.models['difficulty_list_model'], self.ui.listDifficulty)
            self.table.hide_rows()

        models = [self.table.models['system_list_model'],
                  self.table.models['status_list_model'],
                  self.table.models['label_list_model'],
                  self.table.models['difficulty_list_model']]
        m = 0
        while  m < len(models) and not models[m].is_any_filtered():
            m = m + 1
        self.filtering_all = m >= len(models)
