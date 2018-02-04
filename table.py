'''
Module that contains the code that controllers the table that visualises the games.
'''

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from lxml.html.soupparser import fromstring
import re
import sys
from widgets.label_widget import LabelWidget
from controllers.select_date_controller import SelectDateController
from controllers.select_status_controller import SelectStatusController
import numpy as np
from models.filter_list_model import FilterListModel
from models.status_model import StatusModel
from models.sort_list_model import SortListModel
from models.constants import headers, headers_extended, LABEL_NONE, COLUMN_NAME, \
                             COLUMN_SYSTEM, COLUMN_YEAR, COLUMN_RATING, \
                             COLUMN_VOTES, COLUMN_WEIGHTED, COLUMN_STATUS, \
                             COLUMN_LABELS, COLUMN_NOTES, COLUMN_URL, COLUMN_ORDER

class Table(QtWidgets.QTableWidget):
    '''
    Class that represents the application's data table and deals with user
    interactions with the cells.
    '''

    class _NumericWidgetItem(QtWidgets.QTableWidgetItem):
        '''
        The only purpose of this class is to overload the lesser than operator for
        numeric cells so that sorting is done not in lexicographic order but in
        numeric order.
        '''
        # pylint: disable=too-few-public-methods
        def __lt__(self, other):
            return (float(str(self.text()).encode('ascii', 'ignore')) <
                    float(str(other.text()).encode('ascii', 'ignore')))

    def initialize(self):
        '''
        Initialization of the table parameters, including headers, weighted rating,
        callbacks and models.
        '''
        self.setRowCount(0)
        self.setColumnCount(len(headers_extended))

        self.setHorizontalHeaderLabels(headers_extended)
        font = QFont()
        font.setBold(True)
        font.setPointSize(11)
        self.horizontalHeader().setFont(font)

        self.setColumnHidden(headers_extended.index(COLUMN_ORDER), True)

        # Weighted rating initialization
        self.minimum = 100
        # Scrollbar policy
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        self.changed = False
        self.loading = False
        self.search_string = ''

        # Models initialization
        self.models = dict()
        self.models['system_list_model'] = FilterListModel()
        self.models['label_list_model'] = FilterListModel(LABEL_NONE)
        self.models['status_list_model'] = FilterListModel()
        self.models['status_model'] = StatusModel()
        self.models['sort_list_model'] = SortListModel()

        self.last_index = 0

        # Callbacks
        self.clicked.connect(self.cellIsClicked)
        self.cellChanged.connect(self.cellIsChanged)

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
            if len(el) > 0:
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
                if self.item(pos, headers.index(COLUMN_URL)).text() == url:
                    found = True
                pos = pos + 1

            if found:
                errorMessage = QtWidgets.QErrorMessage(self)
                errorMessage.showMessage(data[COLUMN_NAME] + ' (' +
                                         data[COLUMN_SYSTEM] +
                                         ') is already in the database')
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
            errorMessage = QtWidgets.QErrorMessage(self)
            errorMessage.showMessage('The URL ' + url +
                                     ' does not seem to be a valid game entry on GameFAQs')

    def addGameRow(self, data, row=None):
        # Adding the row, and disabling some of the fields, so
        # they can not be edited
        # name
        if row == None:
            rows = self.rowCount()
            self.setRowCount(rows + 1)
        else:
            rows = row

        item = QtWidgets.QTableWidgetItem(data[COLUMN_NAME])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.setItem(rows, headers_extended.index(COLUMN_NAME), item)
        # system
        item = QtWidgets.QTableWidgetItem(data[COLUMN_SYSTEM])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.setItem(rows, headers_extended.index(COLUMN_SYSTEM), item)
        self.models['system_list_model'].add(data[COLUMN_SYSTEM])
        # date
        item = QtWidgets.QTableWidgetItem(data[COLUMN_YEAR])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.setItem(rows, headers_extended.index(COLUMN_YEAR), item)
        # rating
        item = QtWidgets.QTableWidgetItem(data[COLUMN_RATING])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.setItem(rows, headers_extended.index(COLUMN_RATING), item)
        # votes
        item = self._NumericWidgetItem(data[COLUMN_VOTES])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.setItem(rows, headers_extended.index(COLUMN_VOTES), item)
        # Weighted rating
        item = QtWidgets.QTableWidgetItem(data[COLUMN_WEIGHTED])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.setItem(rows, headers_extended.index(COLUMN_WEIGHTED), item)
        # Status
        item = QtWidgets.QTableWidgetItem(data[COLUMN_STATUS])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.setItem(rows, headers_extended.index(COLUMN_STATUS), item)
        item.setForeground(self.models['status_model'].getColor(data[COLUMN_STATUS]))
        self.models['status_list_model'].add(data[COLUMN_STATUS])
        # labels
        item = QtWidgets.QTableWidgetItem('')
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.setItem(rows, headers.index(COLUMN_LABELS), item)
        widget = LabelWidget(item, self)
        widget.stringToLabels(data[COLUMN_LABELS])
        self.setCellWidget(rows, headers_extended.index(COLUMN_LABELS), widget)
        new_labels = widget.getLabels()
        for label in new_labels:
            self.models['label_list_model'].add(label)
        # Notes
        item = QtWidgets.QTableWidgetItem(data[COLUMN_NOTES])
        self.setItem(rows, headers.index(COLUMN_NOTES), item)
        # Url
        item = QtWidgets.QTableWidgetItem(data[COLUMN_URL])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.setItem(rows, headers_extended.index(COLUMN_URL), item)

        # Used to restore the original order
        item = QtWidgets.QTableWidgetItem()
        item.setData(Qt.DisplayRole, self.last_index)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.setItem(rows, headers_extended.index(COLUMN_ORDER), item)
        self.last_index = self.last_index + 1

    def getGameData(self, row):
        data = dict()
        data[COLUMN_NAME] = self.item(row, headers.index(COLUMN_NAME)).text()
        data[COLUMN_SYSTEM] = self.item(row, headers.index(COLUMN_SYSTEM)).text()
        data[COLUMN_YEAR] = self.item(row, headers.index(COLUMN_YEAR)).text()
        data[COLUMN_RATING] = self.item(row, headers.index(COLUMN_RATING)).text()
        data[COLUMN_VOTES] = self.item(row, headers.index(COLUMN_VOTES)).text()
        data[COLUMN_WEIGHTED] = self.item(row, headers.index(COLUMN_WEIGHTED)).text()
        data[COLUMN_STATUS] = self.item(row, headers.index(COLUMN_STATUS)).text()
        data[COLUMN_LABELS] = self.cellWidget(row, headers.index(COLUMN_LABELS)).labelsToString()
        data[COLUMN_NOTES] = self.item(row, headers.index(COLUMN_NOTES)).text()
        data[COLUMN_URL] = self.item(row, headers.index(COLUMN_URL)).text()

        return data

    def compute_final_rating(self):
        rows = self.rowCount()
        # Computing the mean
        ratings_i = []
        votes_i = []
        for i in range(0, rows):
            ratings_i.append(float(self.item(i, headers.index(COLUMN_RATING)).text()))
            votes_i.append(float(self.item(i, headers.index(COLUMN_VOTES)).text()))
        ratings_i = np.array(ratings_i)
        votes_i = np.array(votes_i)
        non_zeros = np.where(votes_i != 0)[0]
        mean = np.mean(ratings_i[non_zeros])

        wr = np.zeros((rows))
        wr[non_zeros] = (votes_i[non_zeros]/(votes_i[non_zeros] + \
                        self.minimum))*ratings_i[non_zeros]
        wr[non_zeros] = wr[non_zeros] + (self.minimum / (votes_i[non_zeros] + self.minimum))*mean

        wr_str = np.zeros((rows), dtype='S4')
        wr_str[non_zeros] = ["%.2f" % x for x in wr[non_zeros]]
        # Computing the weighted rating for all the games again
        for i in range(0, rows):
            self.item(i, headers.index(COLUMN_WEIGHTED)).setText(wr_str[i])

    def update_colors(self):
        if self.rowCount() > 1:
            # Gradient color for the year, rating, votes and weighted columns
            def update_colors_column(column):
                max_value = -1
                min_value = sys.float_info.max
                all_values = []
                # Computing colour ranges
                for row in range(0, self.rowCount()):
                    try:
                        value = float(self.item(row, headers.index(column)).text())
                        max_value = max(max_value, value)
                        min_value = min(min_value, value)
                        all_values.append(value)
                    except:
                        all_values.append(-1)
                # Assigning colour ranges
                all_values = np.array(all_values)
                indices = all_values == -1
                if max_value - min_value > 0:
                    all_values = 100*(all_values - min_value)/(max_value - min_value)
                else:
                    all_values = 0*all_values
                all_values[indices] = 0
                for row in range(0, self.rowCount()):
                    color = QtGui.QColor()
                    color.setHsv(all_values[row], 255, 150)
                    self.item(row, headers.index(column)).setForeground(color)

            update_colors_column(COLUMN_WEIGHTED)
            update_colors_column(COLUMN_YEAR)
            update_colors_column(COLUMN_VOTES)
            update_colors_column(COLUMN_RATING)

            # Colour code for different systems
            systems = []
            for row in range(0, self.rowCount()):
                system = self.item(row, headers.index(COLUMN_SYSTEM)).text()
                if system not in systems:
                    systems.append(system)
            number_systems = len(systems)
            step = int(360/float(number_systems))
            for row in range(0, self.rowCount()):
                system = self.item(row, headers.index(COLUMN_SYSTEM)).text()
                color = QtGui.QColor()
                color.setHsv(step*systems.index(system), 255, 150)
                self.item(row, headers.index(COLUMN_SYSTEM)).setForeground(color)

    def hide_rows(self):
        none = self.models['label_list_model'].get_filtered(LABEL_NONE)
        for row in range(0, self.rowCount()):
            filtered_out = False
            if self.search_string != '':
                item_text = str(self.item(row, headers.index(COLUMN_NAME)).text()).lower()
                filtered_out = not self.search_string in item_text
            if not filtered_out:
                labels_row = self.cellWidget(row, headers.index(COLUMN_LABELS)).getLabels()
                filtered_out = none and len(labels_row) == 0
                if not filtered_out and len(labels_row) > 0:
                    filtered_list = []
                    for i in range(len(labels_row)):
                        filtered_list.append(
                            self.models['label_list_model'].get_filtered(labels_row[i]))
                    filtered_out = all(filtered_list)
                filtered_out = filtered_out or \
                               self.models['system_list_model'].get_filtered(
                                   self.item(row, headers.index(COLUMN_SYSTEM)).text())
                filtered_out = filtered_out or \
                               self.models['status_list_model'].get_filtered(
                                   self.item(row, headers.index(COLUMN_STATUS)).text())
            self.setRowHidden(row, filtered_out)

    def show_all_rows(self):
        for row in range(0, self.rowCount()):
            self.setRowHidden(row, False)

    def resizeColumns(self):
        self.setVisible(False)
        self.resizeColumnsToContents()
        self.setVisible(True)

    def cellIsClicked(self, tableItem):
        row = tableItem.row()
        column = tableItem.column()

        if column == headers.index(COLUMN_YEAR):
            sdc = SelectDateController(self.item(row, column).text(), self)
            sdc.exec_()
            date = sdc.getDate()
            if date != None:
                self.item(row, column).setText(date)
                self.update_colors()
        elif column == headers.index(COLUMN_STATUS):
            ssc = SelectStatusController(self.item(row, column).text(), self)
            ssc.exec_()
            status = ssc.getStatus()
            if status != None:
                self.item(row, column).setText(status)
                self.item(row, column).setForeground(self.models['status_model'].getColor(status))
                self.models['status_list_model'].add(status)
                self.models['status_list_model'].remove(ssc.getPreviousStatus())
                self.hide_rows()

    def cellIsChanged(self, row, col):
        self.changed = True
