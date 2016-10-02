import sys
import csv

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from table import *
from dialogs.search_game_form import *
from controllers.add_game_controller import *
from controllers.filter_games_controller import *
from controllers.sort_games_controller import *

GAMEFAQS_URL = 'http://www.gamefaqs.com/'
SEARCH_URL = GAMEFAQS_URL + 'search?game='

class Window(QMainWindow):
    def __init__(self, parent=None):   
        super(Window, self).__init__(parent)
        self.setWindowTitle('pyBacklogger')
        
        # Creating the interface
        self.main_frame = QWidget()
        self.table = Table()     
        
        self.buttonAdd = QtGui.QPushButton('Add game')
        self.buttonRemove = QtGui.QPushButton('Remove game')
        self.buttonLoad = QtGui.QPushButton('Load backlog')
        self.buttonSave = QtGui.QPushButton('Save backlog')
        self.buttonReload = QtGui.QPushButton('Reload scores')
        self.buttonSort = QtGui.QPushButton('Sort data')
        self.buttonFilter = QtGui.QPushButton('Filter data')
        self.buttonSearch = QtGui.QPushButton('Search game')
        layoutButtons = QtGui.QVBoxLayout()
        layoutButtons.setAlignment(QtCore.Qt.AlignTop)
        layoutButtons.addWidget(self.buttonAdd)
        layoutButtons.addWidget(self.buttonRemove)
        layoutButtons.addWidget(self.buttonLoad)
        layoutButtons.addWidget(self.buttonSave)
        layoutButtons.addWidget(self.buttonReload)
        layoutButtons.addWidget(self.buttonSort)
        layoutButtons.addWidget(self.buttonFilter)
        layoutButtons.addWidget(self.buttonSearch)
        self.buttonAdd.clicked.connect(self.addGame)
        self.buttonRemove.clicked.connect(self.removeGame)
        self.buttonSave.clicked.connect(self.saveBacklog)
        self.buttonLoad.clicked.connect(self.loadBacklog)
        self.buttonReload.clicked.connect(self.reloadScores)
        self.buttonSort.clicked.connect(self.sortGames)
        self.buttonFilter.clicked.connect(self.filterGames)
        self.buttonSearch.clicked.connect(self.searchGames)
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(layoutButtons)
        
        self.main_frame.setLayout(layout)
        self.setCentralWidget(self.main_frame)      
        self.setWindowState(QtCore.Qt.WindowMaximized)
        
        self.previous_search = ''
            
    def addGame(self):
        # Asking the user for an url
        addGameController = AddGameController(self.table, self)
        addGameController.show()
        
    def removeGame(self):
        indexes = self.table.selectionModel().selectedRows()
        if len(indexes) > 0:
            actual_indexes = []
            for index in sorted(indexes):
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
            reply = QtGui.QMessageBox.question(self, 'Confirm game removal', 
                             delete_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        
            if reply == QtGui.QMessageBox.Yes:
                for i in range(len(actual_indexes) - 1, -1, -1):
                    system = self.table.getGameData(actual_indexes[i])[COLUMN_SYSTEM]
                    status = self.table.getGameData(actual_indexes[i])[COLUMN_STATUS]
                    labels = self.table.cellWidget(actual_indexes[i],headers.index(COLUMN_LABELS)).getLabels()
                    self.table.system_list_model.remove(system)
                    self.table.status_list_model.remove(status)
                    for label in labels:
                        self.table.label_list_model.remove(label)
                    self.table.removeRow(actual_indexes[i])
                self.table.changed = True
        else:
            error = QErrorMessage()
            error.showMessage('No games were selected')
            error.setWindowTitle('Remove game')
            error.exec_()
    
    def saveBacklog(self):
        if not self.checkEmpty():
            fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save backlog', '', '*.blg')
            if fileName:
                with open(fileName, 'w') as fp:
                    writer = csv.writer(fp, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_ALL)
                    rows = self.table.rowCount()
                    progress = QProgressDialog("Saving backlog", "", 0, rows, self)
                    progress.setCancelButton(None)
                    progress.setWindowModality(QtCore.Qt.WindowModal)
                    for i in range(0,rows):
                        data = self.table.getGameData(i)
                        data_list = []
                        for h in headers: # defined in the table file
                            data_list.append(str(data[h]))
                        writer.writerows([data_list])
                        progress.setValue(i+1)
                    self.table.changed = False
                    
    def loadBacklog(self):
        confirm = False
        if self.table.changed:
            confirm = self.showConfirmDialog()
        if confirm or not self.table.changed:    
            fileName = QtGui.QFileDialog.getOpenFileName(self, 'Load backlog', '', '*.blg')
            if fileName:
                self.table.system_list_model.clear()
                self.table.status_list_model.clear()
                self.table.label_list_model.clear()
                for i in reversed(range(self.table.rowCount())):
                    self.table.removeRow(i)
                with open(fileName, 'r') as fp:
                    reader = csv.reader(fp, delimiter=',',quoting=csv.QUOTE_ALL)
                    rows = sum(1 for row in reader)
                    fp.seek(0)
                    progress = QProgressDialog("Loading backlog", "", 0, rows, self)
                    progress.setCancelButton(None)
                    progress.setWindowModality(QtCore.Qt.WindowModal)
                    i = 0
                    self.table.setRowCount(rows)
                    self.table.loading = True
                    for row in reader:
                        row_dict = dict()
                        for j in range(0,len(headers)): # defined in the table file
                            row_dict[headers[j]] = row[j]
                        self.table.addGameRow(row_dict, i)
                        progress.setValue(i+1)
                        i = i + 1
                    self.table.changed = False
                    self.table.loading = False
                    self.table.resizeColumns()
                    
    def reloadScores(self):
        if not self.checkEmpty():
            self.table.reload_scores()
        
    def filterGames(self):
        if not self.checkEmpty():
            fgc = FilterGamesController(self.table, self)
            fgc.exec_()
            fgc.applyFiltering()
           
    def sortGames(self): 
        if not self.checkEmpty():
            sgc = SortGamesController(self.table, self)
            sgc.exec_()
            sgc.applySorting()
                
    def searchGames(self):
        if not self.checkEmpty():
            search_text, ok = QtGui.QInputDialog.getText(self,
                   'Seach game', 
                   'Search string:',
                   QtGui.QLineEdit.Normal,
                   self.previous_search)
            
            if ok:
                search_text = str(search_text).lower()
                self.previous_search = search_text
                self.table.hide_rows_search(search_text)
            else:
                self.previous_search = ''
                self.table.show_all_rows()
            
    def checkEmpty(self):
        empty = self.table.rowCount() == 0
        if empty:
            error = QErrorMessage()
            error.showMessage('Add some games first!')
            error.setWindowTitle('No games')
            error.exec_()
        return(empty)
        
    def showConfirmDialog(self):
        reply = QtGui.QMessageBox.question(self, 'Confirm action', 
                     "Your data changed since you loaded it. Are you sure you want to do this?", 
                     QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        return reply == QtGui.QMessageBox.Yes                     

    def closeEvent(self, event):
        confirm = False
        if self.table.changed:
            confirm = self.showConfirmDialog()
        if confirm or not self.table.changed:
            event.accept()
        else:
            event.ignore()
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())