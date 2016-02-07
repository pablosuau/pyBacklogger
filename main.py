import sys
import re
import urllib2
import csv

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from table import *
from add_game_form import *
from filter_dialog import FilterDialog
from sort_dialog import *

GAMEFAQS_URL = 'http://www.gamefaqs.com/'

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
        layoutButtons.setAlignment(Qt.AlignTop)
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
        
        self.already_selected = None
        self.already_selected_status = None
        self.already_sorted = None
        self.already_sort_order = None
        self.previous_search = ''
    
    class AddGameWorker(QThread):
        def __init__(self, url, parent=None):
            QThread.__init__(self, parent)
            self.exiting = False
            self.url = url
        
        def run(self):
            try:
                req = urllib2.Request(self.url, headers={'User-Agent' : "Magic Browser"}) 
                response = urllib2.urlopen(req)
                self.html = response.read().decode('ascii','ignore')
                self.emit(SIGNAL("htmlRead(QString)"), self.html)
            except urllib2.URLError as e:
                print e.reason   
                errorMessage=QErrorMessage(self)
                errorMessage.setWindowTitle('Add game')
                errorMessage.showMessage('Incorrect URL or not Internet connection')
            except urllib2.HTTPError as e:
                print e.code
                print e.read() 
                errorMessage=QErrorMessage(self)
                errorMessage.setWindowTitle('Add game')
                errorMessage.showMessage('Connection error: ' + e.code + ' ' + e.read())   
        def __del__(self):
            self.exiting = True
            self.wait()
            
    def addGame(self):
        # Asking the user for an url
        window = AddGameForm(self)
        window.exec_()
        
        if window.ok:
            self.url = str(window.url.text())
            if not re.match(r'^[a-zA-Z]+://', self.url):
                self.url = 'http://' + self.url
            if not self.url.startswith(GAMEFAQS_URL):
                errorMessage=QErrorMessage(self)
                errorMessage.setWindowTitle('Add game')
                errorMessage.showMessage('The URL is not a valid GameFAQs one')
            else:
                # Download the content of the page
                self.progress = QProgressDialog("Adding game", "", 0, 0, self)
                self.progress.setCancelButton(None)
                self.progress.show()
                self.progress.setWindowModality(Qt.WindowModal)
                self.thread = self.AddGameWorker(self.url, self.table)
                self.connect(self.thread, SIGNAL("htmlRead(QString)"), self.updateAddGame)
                self.thread.start()
    
    def updateAddGame(self, html):
                self.progress.close()
                self.table.addGame(self.url, str(html))
                self.table.scrollToBottom()
                self.table.resizeColumnsToContents()
                 
                    
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
                    self.table.removeRow(actual_indexes[i])
                self.table.resizeColumnsToContents()
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
                    progress.setWindowModality(Qt.WindowModal)
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
            self.already_selected = None
            self.already_selected_status = None
            if fileName:
                for i in reversed(range(self.table.rowCount())):
                    self.table.removeRow(i)
                with open(fileName, 'r') as fp:
                    reader = csv.reader(fp, delimiter=',',quoting=csv.QUOTE_ALL)
                    rows = sum(1 for row in reader)
                    fp.seek(0)
                    progress = QProgressDialog("Loading backlog", "", 0, rows, self)
                    progress.setCancelButton(None)
                    progress.setWindowModality(Qt.WindowModal)
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
                    self.table.resizeColumnsToContents()
                    
    def reloadScores(self):
        if not self.checkEmpty():
            self.table.reload_scores()
        
    def filterGames(self):
        if not self.checkEmpty():
            # We get the labels
            labels = []
            for i in range(0,self.table.rowCount()):
                labels_widget = self.table.cellWidget(i,headers.index(COLUMN_LABELS)).getLabels()
                for j in range(0,len(labels_widget)):
                    if not str(labels_widget[j]) in labels:
                        labels.append(str(labels_widget[j]))
                        
            # and show a dialog to select the labels
            (selected, selected_status, result) = FilterDialog.getFilter(labels, self.already_selected, self.already_selected_status, self)
            # Finally we hide or show rows depending on the labels
            if result:
                self.table.hide_rows(selected, selected_status)
                self.already_selected = selected
                self.already_selected_status = selected_status
            
    def sortGames(self): 
        if not self.checkEmpty():
            # Show the dialog to select the sorting criteria
            (sort_fields, sort_order, result) = SortDialog.getSortingCriteria(self.already_sorted, self.already_sort_order)
            # We apply the order if required. In order to apply
            # multiple column ordering, we order from the last
            # selected column to the first
            if result:
                for i in range(0,len(sort_fields)):
                    j = len(sort_fields) - i - 1
                    index_column = headers.index(sort_fields[j])
                    if sort_order[j] == ASCENDING:
                        order = Qt.AscendingOrder
                    else:
                        order = Qt.DescendingOrder
                    self.table.sortByColumn(index_column, order)
                self.already_sorted = sort_fields
                self.already_sort_order = sort_order
                
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