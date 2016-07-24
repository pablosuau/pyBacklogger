from PyQt4 import QtGui, QtCore, Qt
from views.filter_dialog import Ui_FilterDialog
from dialogs.status_dialog import options

class FilterGamesController(QtGui.QDialog):
    def __init__(self, table, already_selected_status, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_FilterDialog()
        self.ui.setupUi(self)
        
        self.table = table
        self.canceled = False
        
        self.initializeUi(already_selected_status)
        self.setupSignals()

    def initializeUi(self, already_selected_status):
        model_system = Qt.QStandardItemModel()
        systems_list = self.table.system_list_model.get_system_list()
        for system in systems_list:
            item = Qt.QStandardItem(system)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setData(QtCore.Qt.Checked, QtCore.Qt.CheckStateRole)
            if self.table.system_list_model.get_filtered(system):
                item.setCheckState(QtCore.Qt.Unchecked)
            model_system.appendRow(item)          
        self.ui.listSystem.setModel(model_system)
        
        model_status = Qt.QStandardItemModel()
        for option in options: # Imported from dialog.status_dialog
            item = Qt.QStandardItem(option)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setData(QtCore.Qt.Checked, QtCore.Qt.CheckStateRole)
            if already_selected_status != None and not option in already_selected_status:
                item.setCheckState(QtCore.Qt.Unchecked)
            model_status.appendRow(item)          
        self.ui.listStatus.setModel(model_status)  
        
        model_label = Qt.QStandardItemModel()
        labels_list = self.table.label_list_model.get_label_list()
        for label in labels_list:
            item = Qt.QStandardItem(label)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setData(QtCore.Qt.Checked, QtCore.Qt.CheckStateRole)
            if self.table.label_list_model.get_filtered(label):
                item.setCheckState(QtCore.Qt.Unchecked)
            model_label.appendRow(item)          
        self.ui.listLabel.setModel(model_label)

    def setupSignals(self):
        self.ui.pushButtonSelectAllSystem.clicked.connect(self.select_all_system)
        self.ui.pushButtonDeselectAllSystem.clicked.connect(self.deselect_all_system)
        self.ui.pushButtonSelectAllStatus.clicked.connect(self.select_all_status)
        self.ui.pushButtonDeselectAllStatus.clicked.connect(self.deselect_all_status)
        self.ui.pushButtonSelectAllLabel.clicked.connect(self.select_all_labels)
        self.ui.pushButtonDeselectAllLabel.clicked.connect(self.deselect_all_labels)
        self.ui.pushButtonOk.clicked.connect(self.ok_clicked)
        self.ui.pushButtonCancel.clicked.connect(self.cancel_clicked)
        
    def select_all_labels(self):
        model = self.ui.listLabel.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Unchecked:
                item.setCheckState(QtCore.Qt.Checked)
    
    def deselect_all_labels(self):
        model = self.ui.listLabel.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)
                
    def select_all_status(self):
        model = self.ui.listStatus.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Unchecked:
                item.setCheckState(QtCore.Qt.Checked)
    
    def deselect_all_status(self):
        model = self.ui.listStatus.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)
                
    def select_all_system(self):
        model = self.ui.listSystem.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Unchecked:
                item.setCheckState(QtCore.Qt.Checked)
    
    def deselect_all_system(self):
        model = self.ui.listSystem.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)
                
    def ok_clicked(self):
        self.canceled = False
        self.hide()
        
    def cancel_clicked(self):
        self.canceled = True
        self.hide()

    def applyFiltering(self):
        if not self.canceled:            
            model_system = self.ui.listSystem.model()
            for index in range(model_system.rowCount()):
                item = model_system.item(index)
                self.table.system_list_model.set_filtered(str(item.text()), item.checkState() != QtCore.Qt.Checked)
            
            selected_status = []
            model = self.ui.listStatus.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                    selected_status.append(str(item.text()))
               
               
            model_label = self.ui.listLabel.model()
            for index in range(model_label.rowCount()):
                item = model_label.item(index)
                self.table.label_list_model.set_filtered(str(item.text()), item.checkState() != QtCore.Qt.Checked)   
            self.table.hide_rows(selected_status)
            
            return selected_status
        else:
            return (self.already_selected_status)