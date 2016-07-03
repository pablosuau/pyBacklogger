from PyQt4 import QtGui, QtCore, Qt
from views.filter_dialog import Ui_FilterDialog
from dialogs.status_dialog import options

class FilterGamesController(QtGui.QDialog):
    def __init__(self, table, labels, already_selected, already_selected_status, systems, already_selected_systems, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_FilterDialog()
        self.ui.setupUi(self)
        
        self.initializeUi(labels, already_selected, already_selected_status, systems, already_selected_systems)
        
        self.setupSignals()
        
        self.table = table
        self.canceled = False
        self.already_selected = already_selected
        self.already_selected_status = already_selected_status
        self.already_selected_systems = already_selected_systems

    def initializeUi(self, labels, already_selected, already_selected_status, systems, already_selected_systems):
         
        model_system = Qt.QStandardItemModel()
        for system in systems:
            item = Qt.QStandardItem(system)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setData(QtCore.Qt.Checked, QtCore.Qt.CheckStateRole)
            if already_selected_systems != None and not system in already_selected_systems:
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

        model = Qt.QStandardItemModel()
        labels.insert(0,'[None]')
        for label in labels:
            item = Qt.QStandardItem(label)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setData(QtCore.Qt.Checked, QtCore.Qt.CheckStateRole)
            if already_selected != None and not label in already_selected:
                item.setCheckState(QtCore.Qt.Unchecked)
            model.appendRow(item)          
        self.ui.listLabel.setModel(model)

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

    def getFilter(self):
        if not self.canceled:
            selected_systems = []
            model = self.ui.listSystem.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                    selected_systems.append(str(item.text()))        
            
            selected_status = []
            model = self.ui.listStatus.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                    selected_status.append(str(item.text()))
                    
            selected = []
            model = self.ui.listLabel.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                    selected.append(str(item.text()))
                    
            self.table.hide_rows(selected, selected_status, selected_systems)
            
            return (selected, selected_status, selected_systems)
        else:
            return (self.already_selected, self.already_selected_status, self.already_selected_systems)