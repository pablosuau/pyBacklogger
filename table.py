from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from lxml.html.soupparser import fromstring
import re
from widgets.label_widget import LabelWidget
import dialogs
from controllers.select_date_controller import SelectDateController
from dialogs.status_dialog import StatusDialog
import urllib2
import numpy as np
from models.system_list_model import SystemListModel
from models.label_list_model import LabelListModel

COLUMN_NAME = 'Name'
COLUMN_SYSTEM = 'System'
COLUMN_YEAR = 'Year'
COLUMN_RATING = 'Rating'
COLUMN_VOTES = 'Votes'
COLUMN_WEIGHTED = 'Weighted Rating'
COLUMN_STATUS = 'Status'
COLUMN_LABELS = 'Labels'
COLUMN_NOTES = 'Notes'
COLUMN_URL = 'URL'

headers = [COLUMN_NAME, COLUMN_SYSTEM, COLUMN_YEAR, COLUMN_RATING, COLUMN_VOTES, COLUMN_WEIGHTED, COLUMN_STATUS, COLUMN_LABELS, COLUMN_NOTES, COLUMN_URL]

class NumericWidgetItem(QtGui.QTableWidgetItem):
    def __lt__(self, other):
        return (float(str(self.text()).encode('ascii','ignore')) <
                float(str(other.text()).encode('ascii','ignore')))

class Table(QTableWidget):
    def __init__(self, *args):
        QTableWidget.__init__(self, *args)
        self.clicked.connect(self.cellClicked)
        
        self.setHorizontalHeaderLabels(headers)
        self.setRowCount(0)
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)
        
        # Weighted rating initialization
        self.minimum = 100
        # Scrollbar policy
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        
        self.changed = False
        self.already_selected_status = False
        self.loading = False
        
        # Models initialization
        self.system_list_model = SystemListModel()
        self.label_list_model = LabelListModel()
        
    def setmydata(self, data): 
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)
        
    def addGame(self, url, html):
        try:
            doc = fromstring(html)
            data = dict()
            # Game's name
            el = doc.xpath("//h1[@class='page-title']")
            data[COLUMN_NAME] = el[0].findtext('a')
            # Game's system
            el = doc.xpath("//title")
            system = el[0].text
            system = system.split(data[COLUMN_NAME] + ' for ')[1]
            system = system.split(' - GameFAQs')[0]
            data[COLUMN_SYSTEM] = system
            # Year
            el = doc.xpath("//div[@class='pod pod_gameinfo']")
            year = el[0].getchildren()[1].getchildren()[0].getchildren()[3].findtext('a')
            data[COLUMN_YEAR] = re.search('[0-9][0-9][0-9][0-9]|Canceled|TBA', year).group()
            # Rating, votes and final rating
            el = doc.xpath("//fieldset[@id='js_mygames_rate']")
            if len(el)>0:
                rating_str = el[0].getchildren()[0].getchildren()[0].getchildren()[1].findtext('a')
                if rating_str == None:
                    data[COLUMN_RATING] = '0.00'
                    data[COLUMN_VOTES] = '0'
                else:
                    data[COLUMN_RATING] = rating_str.split(' / ')[0]
                    votes_str = el[0].getchildren()[0].getchildren()[0].getchildren()[2].text
                    data[COLUMN_VOTES] = votes_str.split(' ')[0]   
            else:
                data[COLUMN_RATING] = '0.00'
                data[COLUMN_VOTES] = '0'
            # Checking that the game is not already in the database
            rows = self.rowCount()
            found = False
            pos = 0
            while not found and pos < rows:
                if self.item(pos,headers.index(COLUMN_URL)).text() == url:
                    found = True
                pos = pos + 1
        
            if found:
                errorMessage=QErrorMessage(self)
                errorMessage.showMessage(data[COLUMN_NAME] + ' (' + data[COLUMN_SYSTEM] + ') is already in the database')
            else:
                data[COLUMN_WEIGHTED] = ''
                data[COLUMN_STATUS] = 'unplayed'
                data[COLUMN_LABELS] = ''
                data[COLUMN_NOTES] = ''
                data[COLUMN_URL] = url
                self.addGameRow(data)
                # And recomputing weighted ratins
                self.compute_final_rating()
        except:
            errorMessage=QErrorMessage(self)
            errorMessage.showMessage('The URL ' + url + ' does not seem to be a valid game entry on GameFAQs')
    
    def addGameRow(self, data, row=None):
            # Adding the row, and disabling some of the fields, so
            # they can not be edited
            # name
            if row == None:
                rows = self.rowCount()
                self.setRowCount(rows + 1)
            else:
                rows = row
            item = QtGui.QTableWidgetItem(data[COLUMN_NAME])
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setItem(rows, headers.index(COLUMN_NAME), item)
            # system
            item = QtGui.QTableWidgetItem(data[COLUMN_SYSTEM])
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setItem(rows, headers.index(COLUMN_SYSTEM), item)
            self.system_list_model.add_system(data[COLUMN_SYSTEM])
            # date
            item = QtGui.QTableWidgetItem(data[COLUMN_YEAR])
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setItem(rows, headers.index(COLUMN_YEAR), item)
            # rating
            item = QtGui.QTableWidgetItem(data[COLUMN_RATING])
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setItem(rows, headers.index(COLUMN_RATING), item)
            # votes
            item = NumericWidgetItem(data[COLUMN_VOTES])
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setItem(rows, headers.index(COLUMN_VOTES), item)
            # Weighted rating
            item = QtGui.QTableWidgetItem(data[COLUMN_WEIGHTED])
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setItem(rows, headers.index(COLUMN_WEIGHTED), item)
            # Status
            item = QtGui.QTableWidgetItem(data[COLUMN_STATUS])
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setItem(rows, headers.index(COLUMN_STATUS), item)
            item.setTextColor(dialogs.status_dialog.colors[dialogs.status_dialog.options.index(data[COLUMN_STATUS])])
            # labels
            item = QtGui.QTableWidgetItem('')
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setItem(rows, headers.index(COLUMN_LABELS), item)
            widget = LabelWidget(item, self)
            widget.stringToLabels(data[COLUMN_LABELS])
            self.setCellWidget(rows, headers.index(COLUMN_LABELS), widget)
            new_labels = widget.getLabels()
            for label in new_labels:
                self.label_list_model.add_label(label)  
            # Notes
            item = QtGui.QTableWidgetItem(data[COLUMN_NOTES])
            self.setItem(rows, headers.index(COLUMN_NOTES), item)
            # Url
            item = QtGui.QTableWidgetItem(data[COLUMN_URL])
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setItem(rows, headers.index(COLUMN_URL), item)
            
            self.changed = True
            
            
        
    def getGameData(self, row):
        data = dict()
        data[COLUMN_NAME] = self.item(row, headers.index(COLUMN_NAME)).text()
        data[COLUMN_SYSTEM] = self.item(row,headers.index(COLUMN_SYSTEM)).text()
        data[COLUMN_YEAR] = self.item(row,headers.index(COLUMN_YEAR)).text()
        data[COLUMN_RATING] = self.item(row,headers.index(COLUMN_RATING)).text()
        data[COLUMN_VOTES] = self.item(row,headers.index(COLUMN_VOTES)).text()
        data[COLUMN_WEIGHTED] = self.item(row,headers.index(COLUMN_WEIGHTED)).text()
        data[COLUMN_STATUS] = self.item(row, headers.index(COLUMN_STATUS)).text()
        data[COLUMN_LABELS] = self.cellWidget(row,headers.index(COLUMN_LABELS)).labelsToString()
        data[COLUMN_NOTES] = self.item(row,headers.index(COLUMN_NOTES)).text()
        data[COLUMN_URL] = self.item(row,headers.index(COLUMN_URL)).text()
                 
        return data
        
    def compute_final_rating(self):
        rows = self.rowCount()
        # Computing the mean
        ratings_i = []
        votes_i = []
        for i in range(0,rows):
            ratings_i.append(float(self.item(i,headers.index(COLUMN_RATING)).text()))
            votes_i.append(float(self.item(i,headers.index(COLUMN_VOTES)).text()))
        ratings_i = np.array(ratings_i)
        votes_i = np.array(votes_i)
        non_zeros = np.where(votes_i != 0)[0]  
        mean = np.mean(ratings_i[non_zeros])

        wr = np.zeros((rows))
        wr[non_zeros] = (votes_i[non_zeros]/(votes_i[non_zeros] + self.minimum))*ratings_i[non_zeros]
        wr[non_zeros] = wr[non_zeros] + (self.minimum / (votes_i[non_zeros] + self.minimum))*mean
        
        wr_str = np.zeros((rows),dtype='S4')
        wr_str[non_zeros] = ["%.2f" % x for x in wr[non_zeros]]
        # Computing the weighted rating for all the games again
        for i in range(0,rows):
            self.item(i, headers.index(COLUMN_WEIGHTED)).setText(wr_str[i])
            
         
    def reload_scores(self):
        rows = self.rowCount()
        progress = QProgressDialog("Updating scores", "", 0, rows, self)
        progress.setWindowTitle('Reload scores')
        progress.setCancelButton(None)
        progress.setWindowModality(Qt.WindowModal)
        try:
            for i in range(0,rows):
                url = self.item(i,headers.index(COLUMN_URL)).text()        
                req = urllib2.Request(str(url), headers={'User-Agent' : "Magic Browser"}) 
                response = urllib2.urlopen(req)
                html = response.read().decode('ascii','ignore') 
                doc = fromstring(html)
                # Updating the name, in case it changed
                el = doc.xpath("//h1[@class='page-title']")
                name = el[0].findtext('a')
                self.item(i,headers.index(COLUMN_NAME)).setText(name)
                # Updating the score
                el = doc.xpath("//fieldset[@id='js_mygames_rate']")
                if len(el)>0:
                    rating_str = el[0].getchildren()[0].getchildren()[0].getchildren()[1].findtext('a')
                    if rating_str == None:
                        rating = '0.00'
                        votes = '0'
                    else:
                        rating = rating_str.split(' / ')[0]
                        votes_str = el[0].getchildren()[0].getchildren()[0].getchildren()[2].text
                        votes = votes_str.split(' ')[0]   
                else:
                    rating = '0.00'
                    votes = '0'
                self.item(i,headers.index(COLUMN_RATING)).setText(rating)
                self.item(i,headers.index(COLUMN_VOTES)).setText(votes)
                progress.setValue(i+1)
            self.compute_final_rating()
            self.changed = True
        except urllib2.URLError as e:
            print e.reason   
            errorMessage=QErrorMessage(self)
            errorMessage.showMessage('Incorrect URL or not Internet connection')
        except urllib2.HTTPError as e:
            print e.code
            print e.read() 
            errorMessage=QErrorMessage(self)
            errorMessage.showMessage('Connection error: ' + e.code + ' ' + e.read())
        
    def hide_rows(self, status):
        self.already_selected_status = status
        self.hide_rows_already()
    
    def hide_rows_already(self):
        none = self.label_list_model.get_filtered('---None---')
        for row in range(0,self.rowCount()):
             labels_row = self.cellWidget(row,headers.index(COLUMN_LABELS)).getLabels()
             filtered_out = none and len(labels_row) == 0
             i = 0                          
             while not filtered_out and i<len(labels_row):
                 filtered_out = self.label_list_model.get_filtered(labels_row[i])
                 i = i + 1
             filtered_out = filtered_out or not self.item(row, headers.index(COLUMN_STATUS)).text() in self.already_selected_status
             filtered_out = filtered_out or self.system_list_model.get_filtered(self.item(row, headers.index(COLUMN_SYSTEM)).text())
             self.setRowHidden(row, filtered_out)

    def hide_rows_search(self, text):
        for row in range(0,self.rowCount()):
            item_text = str(self.item(row, headers.index(COLUMN_NAME)).text()).lower()
            self.setRowHidden(row, not text in item_text)
            
    def show_all_rows(self):
        for row in range(0,self.rowCount()):
            self.setRowHidden(row, False)
        
    def resizeColumns(self):
        self.setVisible(False)
        self.resizeColumnsToContents()
        self.setVisible(True)
        
    def cellClicked(self, tableItem):
        row = tableItem.row()
        column = tableItem.column()        
        
        if column == headers.index(COLUMN_YEAR):
            sdc = SelectDateController(self.item(row, column).text(), self)
            sdc.exec_()
            date = sdc.getDate()
            if date != None:
                self.item(row, column).setText(date)
        elif column == headers.index(COLUMN_STATUS):
            (status, color, accepted) = StatusDialog.getStatus(self.item(row, column).text())
            if accepted:
                self.item(row, column).setText(status)
                self.item(row, column).setTextColor(color)
                self.hide_rows_already()
