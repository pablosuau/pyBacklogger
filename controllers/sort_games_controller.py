from PyQt4 import QtGui, QtCore
from views.sort_dialog import Ui_SortDialog
from models.constants import headers

class SortGamesController(QtGui.QDialog):
    # UI and signal setup
    def __init__(self, table, parent):
        QtGui.QWidget.__init__(self, parent)
       
        self.ui = Ui_SortDialog()
        self.ui.setupUi(self)
   
        self.table = table
     
        self.initializeUi()     
        self.setupSignals()
        
    def initializeUi(self):
        self.ui.sortByList.setModel(self.table.sort_list_model.sort)
        self.ui.availableFieldsList.setModel(self.table.sort_list_model.available)
    
    def setupSignals(self):
        self.ui.pushButtonLeft.clicked.connect(self.left_clicked)
        self.ui.pushButtonRight.clicked.connect(self.right_clicked)
        self.ui.pushButtonUp.clicked.connect(self.up_clicked)
        self.ui.pushButtonDown.clicked.connect(self.down_clicked)
        self.ui.availableFieldsList.clicked.connect(self.activate_buttons_available)
        self.ui.sortByList.clicked.connect(self.activate_buttons_sort)
        self.ui.pushButtonOk.clicked.connect(self.ok_clicked)
        self.ui.pushButtonCancel.clicked.connect(self.cancel_clicked)
        
    def activate_buttons_available(self):
        self.ui.pushButtonLeft.setEnabled(True)
        self.ui.sortByList.clearSelection()
        self.ui.pushButtonRight.setEnabled(False)
        self.ui.pushButtonUp.setEnabled(False)
        self.ui.pushButtonDown.setEnabled(False)
        
    def activate_buttons_sort(self):
        self.ui.pushButtonRight.setEnabled(True)
        self.ui.availableFieldsList.clearSelection()
        self.ui.pushButtonLeft.setEnabled(False)
        self.ui.pushButtonUp.setEnabled(False)
        self.ui.pushButtonDown.setEnabled(False)
        self.set_up_down()

    def clear_clicked(self):
        self.ui.availableFieldsList.clearSelection()
        self.ui.sortByList.clearSelection()
        self.ui.pushButtonLeft.setEnabled(False)
        self.ui.pushButtonRight.setEnabled(False)
        self.ui.pushButtonUp.setEnabled(False)
        self.ui.pushButtonDown.setEnabled(False)
        
    def set_up_down(self):
        if self.ui.sortByList.model().rowCount() > 1:
            row = self.ui.sortByList.selectedIndexes()[0].row()
            if row > 0:
                self.ui.pushButtonUp.setEnabled(True)
            if row < self.ui.sortByList.model().rowCount() - 1:
                self.ui.pushButtonDown.setEnabled(True)
        
    def left_clicked(self):
        self.table.sort_list_model.to_sort(self.ui.availableFieldsList.selectedIndexes())
        self.clear_clicked()
                
    def right_clicked(self):
        self.table.sort_list_model.to_available(self.ui.sortByList.selectedIndexes())
        self.clear_clicked()
        
    def up_down_clicked(self, method):
        index = method(self.ui.sortByList.selectedIndexes()[0])
        self.clear_clicked()
        self.ui.sortByList.selectionModel().select(index, QtGui.QItemSelectionModel.Select)
        self.set_up_down()
        
    def up_clicked(self):
        self.up_down_clicked(self.table.sort_list_model.sort_up)
    
    def down_clicked(self):
        self.up_down_clicked(self.table.sort_list_model.sort_down)
        
    def ok_clicked(self):
        self.canceled = False
        self.hide()
        
    def cancel_clicked(self):
        self.canceled = True
        self.hide()
    
    def applySorting(self):
        if not self.canceled:
            self.table.setVisible(False)
            sort_fields = self.table.sort_list_model.get_sort_fields()
            for i in range(0,len(sort_fields)):
                j = len(sort_fields) - i - 1
                index_column = headers.index(sort_fields[j])
                #if sort_order[j] == ASCENDING:
                #    order = QtCore.Qt.AscendingOrder
                #else:
                #    order = QtCore.Qt.DescendingOrder
                order = QtCore.Qt.DescendingOrder
                self.table.sortByColumn(index_column, order)
            self.table.setVisible(True)
        