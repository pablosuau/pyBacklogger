from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import status_dialog

class FilterDialog(QDialog):
    def __init__(self, labels, already_selected, already_selected_status, parent = None):
        super(FilterDialog, self).__init__(parent)
        self.setWindowTitle('Filter data')

        self.layout = QtGui.QVBoxLayout(self)
                
        model_status = QStandardItemModel()
        caption_status = QtGui.QLabel('Status')
        for option in status_dialog.options:
            item = QStandardItem(option)
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setData(Qt.Checked, Qt.CheckStateRole)
            if already_selected_status != None and not option in already_selected_status:
                item.setCheckState(QtCore.Qt.Unchecked)
            model_status.appendRow(item)          
        self.listView_status = QListView()
        self.listView_status.setModel(model_status)
        
        # Select all and deselect all buttons
        layout_select_deselect_status = QtGui.QHBoxLayout()
        select_all_status = QtGui.QPushButton('Select all')
        deselect_all_status = QtGui.QPushButton('Deselect all')
        select_all_status.clicked.connect(self.select_all_status)
        deselect_all_status.clicked.connect(self.deselect_all_status)
        layout_select_deselect_status.addWidget(select_all_status)
        layout_select_deselect_status.addWidget(deselect_all_status)        
        
        model = QStandardItemModel()
        caption = QtGui.QLabel('Labels')
        labels.insert(0,'[None]')
        for label in labels:
            item = QStandardItem(label)
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setData(Qt.Checked, Qt.CheckStateRole)
            if already_selected != None and not label in already_selected:
                item.setCheckState(QtCore.Qt.Unchecked)
            model.appendRow(item)          
        self.listView = QListView()
        self.listView.setModel(model)
        
        # Select all and deselect all buttons
        layout_select_deselect_labels = QtGui.QHBoxLayout()
        select_all_labels = QtGui.QPushButton('Select all')
        deselect_all_labels = QtGui.QPushButton('Deselect all')
        select_all_labels.clicked.connect(self.select_all_labels)
        deselect_all_labels.clicked.connect(self.deselect_all_labels)
        layout_select_deselect_labels.addWidget(select_all_labels)
        layout_select_deselect_labels.addWidget(deselect_all_labels)
        
        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        
        self.layout.addWidget(caption_status)
        self.layout.addWidget(self.listView_status)
        self.layout.addLayout(layout_select_deselect_status)
        self.layout.addWidget(caption)
        self.layout.addWidget(self.listView)
        self.layout.addLayout(layout_select_deselect_labels)
        self.layout.addWidget(buttons)
        
    def select_all_labels(self):
        model = self.listView.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Unchecked:
                item.setCheckState(QtCore.Qt.Checked)
    
    def deselect_all_labels(self):
        model = self.listView.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)
                
    def select_all_status(self):
        model = self.listView_status.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Unchecked:
                item.setCheckState(QtCore.Qt.Checked)
    
    def deselect_all_status(self):
        model = self.listView_status.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getFilter(labels, already_selected, already_selected_status, parent = None):
        dialog = FilterDialog(labels, already_selected, already_selected_status, parent)
        result = dialog.exec_()
        
        selected_status = []
        model = dialog.listView_status.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                selected_status.append(str(item.text()))
                
        selected = []
        model = dialog.listView.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                selected.append(str(item.text()))
        
        return (selected, selected_status, result == QDialog.Accepted)