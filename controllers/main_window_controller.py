import csv
import os
from shutil import copyfile
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from views.main_window import Ui_MainWindow
from controllers.add_game_controller import *
from controllers.filter_games_controller import *
from controllers.sort_games_controller import *
from controllers.reload_scores_controller import *
from controllers.statistics_window_controller import *
from models.constants import headers, COLUMN_SYSTEM, COLUMN_STATUS, COLUMN_LABELS

class MainWindowController(QtWidgets.QWidget):
    # UI and signal setup
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
       
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
   
        self.table = self.ui.table
        self.canceled = False
     
        self.initializeUi()     
        self.setupSignals()
    
    def initializeUi(self):
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.table.initialize()
        
    def setupSignals(self):
        self.ui.pushButtonAddGame.clicked.connect(self.add_game_clicked)
        self.ui.pushButtonRemoveGame.clicked.connect(self.remove_game_clicked)
        self.ui.pushButtonLoadBacklog.clicked.connect(self.load_backlog_clicked)
        self.ui.pushButtonSaveBacklog.clicked.connect(self.save_backlog_clicked)
        self.ui.pushButtonReloadScores.clicked.connect(self.reload_scores_clicked)
        self.ui.pushButtonSortData.clicked.connect(self.sort_data_clicked)
        self.ui.pushButtonFilterData.clicked.connect(self.filter_data_clicked)
        self.ui.pushButtonStatistics.clicked.connect(self.statistics_clicked)
        self.ui.lineEditSearchGame.textChanged.connect(self.search_text_changed)
        
    def add_game_clicked(self):
        addGameController = AddGameController(self.table, parent=self)
        addGameController.show()
    
    def remove_game_clicked(self):
        indexes = self.table.selectionModel().selectedRows()
        if len(indexes) > 0:
            actual_indexes = []
            for index in sorted(indexes):
                if not self.table.isRowHidden(index.row()):
                    actual_indexes.append(index.row())
            names = []
            systems = []
            for i in actual_indexes:
                names.append(self.table.item(i,0).text())
                systems.append(self.table.item(i,1).text())
            
            delete_msg = "Are you sure you want to delete the following entries?\n" 
            for i in range(0,min(len(names),10)):
                delete_msg = delete_msg + '\n' + names[i] + ' (' + systems[i] + ')'
            if len(names) > 10:
                delete_msg = delete_msg + '\n...'
            reply = QtWidgets.QMessageBox.question(self, 'Confirm game removal', 
                             delete_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        
            if reply == QtWidgets.QMessageBox.Yes:
                progress = QtWidgets.QProgressDialog("Removing games", "", 0, len(actual_indexes), self)
                progress.setCancelButton(None)
                progress.setWindowModality(QtCore.Qt.WindowModal)
                for i in range(len(actual_indexes) - 1, -1, -1):
                    system = self.table.getGameData(actual_indexes[i])[COLUMN_SYSTEM]
                    status = self.table.getGameData(actual_indexes[i])[COLUMN_STATUS]
                    labels = self.table.cellWidget(actual_indexes[i],headers.index(COLUMN_LABELS)).getLabels()
                    self.table.system_list_model.remove(system)
                    self.table.status_list_model.remove(status)
                    for label in labels:
                        self.table.label_list_model.remove(label)
                    self.table.removeRow(actual_indexes[i])
                    progress.setValue(len(actual_indexes) - i)
                self.table.changed = True
                
            self.table.update_colors()
            self.table.resizeColumns()
        else:
            error = QtWidgets.QErrorMessage()
            error.showMessage('No games were selected')
            error.setWindowTitle('Remove game')
            error.exec_()
                
    def load_backlog_clicked(self):
        confirm = False
        if self.table.changed:
            confirm = self.showConfirmDialog()
        if confirm or not self.table.changed:    
            fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Load backlog', '', '*.blg')[0]
            if fileName:
                self.table.last_index = 0            
            
                self.clear_options()
                
                for i in reversed(range(self.table.rowCount())):
                    self.table.removeRow(i)
                with open(fileName, 'r') as fp:
                    reader = csv.reader(fp, delimiter=',',quoting=csv.QUOTE_ALL)
                    rows = sum(1 for row in reader)
                    fp.seek(0)
                    progress = QtWidgets.QProgressDialog("Loading backlog", "", 0, rows, self)
                    progress.setCancelButton(None)
                    progress.setWindowModality(QtCore.Qt.WindowModal)
                    i = 0
                    self.table.setRowCount(rows)
                    self.table.loading = True
                    for row in reader:
                        row_dict = dict()
                        for j in range(0,len(headers)): 
                            row_dict[headers[j]] = row[j].decode('utf-8')
                        self.table.addGameRow(row_dict, i)
                        progress.setValue(i+1)
                        i = i + 1
                    self.table.changed = False
                    self.table.loading = False
                    self.table.resizeColumns()
        
        self.table.update_colors()
    
    def save_backlog_clicked(self):
        if not self.checkEmpty():
            fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Save backlog', '', '*.blg')[0]
            if fileName:
                if os.path.isfile(fileName):
                    (dir, file) = os.path.split(str(fileName))
                    name, extension = os.path.splitext(file)
                    bak_file = os.path.join(dir, name + '.bak')
                    copyfile(fileName, bak_file)
                with open(fileName, 'w') as fp:
                    self.set_original_order()
                    
                    writer = csv.writer(fp, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_ALL)
                    rows = self.table.rowCount()
                    progress = QtWidgets.QProgressDialog("Saving backlog", "", 0, rows, self)
                    progress.setCancelButton(None)
                    progress.setWindowModality(QtCore.Qt.WindowModal)
                    for i in range(0,rows):
                        data = self.table.getGameData(i)
                        data_list = []
                        for h in headers: 
                            data_list.append(str(data[h]).encode('utf-8'))
                        writer.writerows([data_list])
                        progress.setValue(i+1)
                    self.table.changed = False
                    
                    sgc = SortGamesController(self.table, self)
                    sgc.canceled = False
                    sgc.applySorting()
    
    def reload_scores_clicked(self):
        if not self.checkEmpty():
            rsc = ReloadScoresController(self.table, self)
            rsc.reload_scores()
    
    def sort_data_clicked(self):
        self.ui.pushButtonSortData.setChecked(False)
        if not self.checkEmpty():
            sgc = SortGamesController(self.table, self)
            sgc.exec_()
            sgc.applySorting()
            self.ui.pushButtonSortData.setChecked(sgc.sorting_active)
    
    def filter_data_clicked(self):
        self.ui.pushButtonFilterData.setChecked(False)
        if not self.checkEmpty():
            fgc = FilterGamesController(self.table, self)
            fgc.exec_()
            fgc.applyFiltering()
            self.ui.pushButtonFilterData.setChecked(not fgc.filtering_all)   
            
    def statistics_clicked(self):
        if not self.checkEmpty():
            swc = StatisticsWindowController(self)
            swc.exec_()
    
    def search_text_changed(self):
        search_text = str(self.ui.lineEditSearchGame.text()).lower()
        self.table.search_string = search_text
        self.table.hide_rows()

    def checkEmpty(self):
        empty = self.table.rowCount() == 0
        if empty:
            error = QtWidgets.QErrorMessage()
            error.showMessage('Add some games first!')
            error.setWindowTitle('No games')
            error.exec_()
        return(empty)
        
    def showConfirmDialog(self):
        reply = QtWidgets.QMessageBox.question(self, 'Confirm action', 
                     "Your data changed since you loaded it. Are you sure you want to do this?", 
                     QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        return reply == QtWidgets.QMessageBox.Yes                     

    def closeEvent(self, event):
        confirm = False
        if self.table.changed:
            confirm = self.showConfirmDialog()
        if confirm or not self.table.changed:
            event.accept()
        else:
            event.ignore()
            
    def clear_options(self):
        self.ui.pushButtonSortData.setChecked(False)
        self.ui.pushButtonFilterData.setChecked(False)
        self.ui.lineEditSearchGame.setText('')                    
        
        self.table.system_list_model.clear_filtered()
        self.table.status_list_model.clear_filtered()
        self.table.label_list_model.clear_filtered()
        
        self.table.show_all_rows()

    def set_original_order(self):
        self.table.sort_list_model.clear()
        order = QtCore.Qt.AscendingOrder
        self.table.sortByColumn(constants.headers_extended.index(constants.COLUMN_ORDER), order) 
                                                 
