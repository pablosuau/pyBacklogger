from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import table
import models.table_model as table_model

order = ['ascending', 'descending']
ASCENDING = 0
DESCENDING = 1

class SortDialog(QDialog):
    def __init__(self, already_selected, already_sort_order, parent = None):
        super(SortDialog, self).__init__(parent)
        self.setWindowTitle('Sort data')
        
        self.layout = QtGui.QVBoxLayout(self)

        # Sorting criteria
        self.layouts = QtGui.QVBoxLayout()
        layout = QtGui.QHBoxLayout()
        combo_header = QtGui.QComboBox()
        for header in table_model.headers:
            combo_header.addItem(header)
        combo_order = QtGui.QComboBox()
        for o in order:
            combo_order.addItem(o)
        combo_header.currentIndexChanged.connect(self.combo_value_changed)
        layout.addWidget(combo_header)
        layout.addWidget(combo_order)
        self.layouts.addLayout(layout)
        
        # Add and remove column buttons
        layout_buttons = QtGui.QHBoxLayout()
        self.button_add = QtGui.QPushButton('Add column')        
        self.button_add.clicked.connect(self.add_column)
        self.button_remove = QtGui.QPushButton('Remove column')
        self.button_remove.clicked.connect(self.remove_column)
        self.button_remove.setEnabled(False)
        layout_buttons.addWidget(self.button_add)
        layout_buttons.addWidget(self.button_remove)        
        
        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        
        self.layout.addLayout(self.layouts)
        self.layout.addLayout(layout_buttons)
        self.layout.addWidget(buttons)
        
        self.setFixedSize(self.minimumSizeHint())
        
        # Initializing the array that will contain the
        # previous selected fields
        self.previous_selected = []
        
        # Selecting the alrady selected elements
        if already_selected != None:
            self.show()
            for item in range(0,len(already_selected)):
               prev_layout = self.layouts.itemAt(self.layouts.count() - 1)
               prev_combo_header = prev_layout.itemAt(0).widget() 
               all_items = [prev_combo_header.itemText(i) for i in range(prev_combo_header.count())]
               selected = all_items.index(already_selected[item]) 
               prev_combo_header.setCurrentIndex(selected)
               if item < len(already_selected) - 1:
                   self.add_column()
        
    def add_column(self):
        # Obtaining a list of columns that does not include the selected
        # in the previous combo box
        prev_layout = self.layouts.itemAt(self.layouts.count() - 1)
        prev_combo = prev_layout.itemAt(0).widget()
        headers = [prev_combo.itemText(i) for i in range(prev_combo.count())]
        selected = prev_combo.currentIndex()
        self.previous_selected.append(headers[selected])
        del headers[selected]
        # Adding the new combobox
        layout = QtGui.QHBoxLayout()
        combo_header = QtGui.QComboBox()
        for header in headers:
            combo_header.addItem(header)
        combo_order = QtGui.QComboBox()
        for o in order:
            combo_order.addItem(o)
        layout.addWidget(combo_header)
        combo_header.currentIndexChanged.connect(self.combo_value_changed)
        layout.addWidget(combo_order)
        self.layouts.addLayout(layout) 
        # Disabling the add button in the case in which it is not possible
        # to add more headers
        if len(headers) == 1:
            self.button_add.setEnabled(False)
        self.button_remove.setEnabled(True)
        
        QApplication.processEvents()
        self.setFixedSize(self.minimumSizeHint()) 
        
    def remove_column(self):
        # Removing the last combobox
        item = self.layouts.itemAt(self.layouts.count() - 1)
        widgets = [item.itemAt(i).widget() for i in range(0,item.count())]
        for w in widgets:
            w.close()
        self.layouts.removeItem(item)
        del self.previous_selected[len(self.previous_selected) - 1]
        
        # Enabling/disabling buttons
        self.button_add.setEnabled(True)
        if self.layouts.count() == 1:
            self.button_remove.setEnabled(False)

        # Resizing the window
        self.setFixedSize(self.minimumSizeHint())
        
    def combo_value_changed(self):
        # Checking if the value of all the comboboxes corresponds
        # with the stored ones
        i = 0
        equal = True
        while i < self.layouts.count() - 1 and equal:
            prev_layout = self.layouts.itemAt(i)
            prev_combo = prev_layout.itemAt(0).widget()
            selected = prev_combo.currentText()
            if selected != self.previous_selected[i]:
                equal = False
            else:
                i = i + 1
        # Removing columns if necessary
        if not equal:
            count = self.layouts.count()
            for j in range(i+1, count):
                self.remove_column()


    # Static method to create the dialog and return sorting criteria
    @staticmethod
    def getSortingCriteria(already_selected, already_sort_order):
        dialog = SortDialog(already_selected, already_sort_order)
        result = dialog.exec_()
        
        # Extracting sorting criteria
        sort_fields = []
        sort_order = []
        for i in range(0,dialog.layouts.count()):
            prev_layout = dialog.layouts.itemAt(i)
            prev_combo_field = prev_layout.itemAt(0).widget()
            prev_combo_order = prev_layout.itemAt(1).widget()
            sort_fields.append(prev_combo_field.currentText())
            sort_order.append(prev_combo_order.currentIndex())
            
        return (sort_fields, sort_order, result == QDialog.Accepted)
