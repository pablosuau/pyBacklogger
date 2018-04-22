'''
Module that contains the code that controls the table that visualises the games.
'''

import re
import sys
import numpy as np
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from lxml.html.soupparser import fromstring
from widgets.label_widget import LabelWidget
from controllers.select_date_controller import SelectDateController
from controllers.select_status_controller import SelectStatusController
from models.filter_list_model import FilterListModel
from models.status_model import StatusModel
from models.sort_list_model import SortListModel
from models.constants import headers, headers_extended, LABEL_NONE, COLUMN_NAME, \
                             COLUMN_SYSTEM, COLUMN_YEAR, COLUMN_RATING, \
                             COLUMN_VOTES, COLUMN_WEIGHTED, COLUMN_LENGTH, \
                             COLUMN_DIFFICULTY, COLUMN_STATUS, COLUMN_LABELS, \
                             COLUMN_NOTES, COLUMN_URL, COLUMN_ORDER

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

    def __init__(self, parent=None):
        '''
        Initialization of the table parameters, including headers, weighted rating,
        callbacks and models.
        '''
        super(Table, self).__init__(parent)

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
        self.clicked.connect(self.cell_is_clicked)
        self.cellChanged.connect(self.cell_is_changed)

    def add_game(self, url, html):
        '''
        Extracts the game data from a downloaded html page prior to adding the game to the table
        (see add_game_row). The URL of the downloaded html page is used to check whether the game
        was already in the database, and an error message is produced if that is the case.

        parameters:
            - url: URL from which the html data was downloaded
            - html: html page of the game to be added to the database
        '''
        try:
            doc = fromstring(html)
            data = dict()
            # Game's name
            element = doc.xpath("//h1[@class='page-title']")
            data[COLUMN_NAME] = element[0].findtext('a')
            # Game's system
            element = doc.xpath("//title")
            system = element[0].text
            system = system.split(data[COLUMN_NAME] + ' for ')[1]
            system = system.split(' - GameFAQs')[0]
            data[COLUMN_SYSTEM] = system
            # Year
            element = doc.xpath("//div[@class='pod pod_gameinfo']")
            year = element[0].getchildren()[1].getchildren()[0].getchildren()[3].findtext('a')
            data[COLUMN_YEAR] = re.search('[0-9][0-9][0-9][0-9]|Canceled|TBA', year).group()
            # Rating, votes and final rating
            element = doc.xpath("//fieldset[@id='js_mygames_rate']")
            if len(element) > 0:
                rating = element[0].getchildren()[0].getchildren()[0].getchildren()[1].findtext('a')
                if rating is None:
                    data[COLUMN_RATING] = '0.00'
                    data[COLUMN_VOTES] = '0'
                else:
                    data[COLUMN_RATING] = rating.split(' / ')[0]
                    votes = element[0].getchildren()[0].getchildren()[0].getchildren()[2].text
                    data[COLUMN_VOTES] = votes.split(' ')[0]
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
                error_message = QtWidgets.QErrorMessage(self)
                error_message.showMessage(data[COLUMN_NAME] + ' (' +
                                          data[COLUMN_SYSTEM] +
                                          ') is already in the database')
            else:
                data[COLUMN_WEIGHTED] = ''
                data[COLUMN_STATUS] = 'unplayed'
                data[COLUMN_LABELS] = ''
                data[COLUMN_NOTES] = ''
                data[COLUMN_URL] = url
                self.add_game_row(data)
                # And recomputing weighted ratins
                self.compute_final_rating()
        except (TypeError, IndexError):
            # This exception is produced if there is an error while parsing the HTML
            error_message = QtWidgets.QErrorMessage(self)
            error_message.showMessage('The URL ' + url +
                                      ' does not seem to be a valid game entry on GameFAQs')

    def add_game_row(self, data, row=None):
        '''
        This method effectively adds a single game as a row to the table after the data has been
        parsed from the corresponding HTML page.

        parameters:
            - data: a dictionary which contains the data to be added to the rwo
            - row: row in which the game should be added. If the default value (None) is used,
              the row will be appended at the end of the table
        '''
        if row is None:
            rows = self.rowCount()
            self.setRowCount(rows + 1)
        else:
            rows = row

        # name
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
        item_numeric = self._NumericWidgetItem(data[COLUMN_VOTES])
        item_numeric.setFlags(QtCore.Qt.ItemIsEnabled)
        self.setItem(rows, headers_extended.index(COLUMN_VOTES), item_numeric)
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

    def get_game_data(self, row):
        '''
        Produces a dictionary which contains the game data from the selected row

        parameters:
            - row: the row from which extract the data
        returns:
            - A dictionary which contains the data of the selected row
        '''
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
        '''
        In-place computation of the weighted rating of the games based on GameFAQS' rating and
        number of votes. See https://math.stackexchange.com/questions/169032/understanding-the-imdb-
        weighted-rating-function-for-usage-on-my-own-website for a description of this method.
        '''
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

        weighted_rating = np.zeros((rows))
        weighted_rating[non_zeros] = (votes_i[non_zeros]/(votes_i[non_zeros] + \
                        self.minimum))*ratings_i[non_zeros]
        weighted_rating[non_zeros] = weighted_rating[non_zeros] + (
            self.minimum / (votes_i[non_zeros] + self.minimum)
            )*mean

        weighted_rating_str = np.zeros((rows)).astype('|S4')
        weighted_rating_str[non_zeros] = ['%.2f' % x for x in weighted_rating[non_zeros]]
        # Computing the weighted rating for all the games again
        for i in range(0, rows):
            self.item(i, headers.index(COLUMN_WEIGHTED)).setText(weighted_rating_str[i].decode('UTF-8'))

    def update_colors(self):
        '''
        Assigns a colour gradient to to the values in the year, rating, votes and weighted
        rating columns. Additionally, a different colour is assigned to each different
        system.
        '''
        if self.rowCount() > 1:
            # Gradient color for the year, rating, votes and weighted columns
            def update_colors_column(column):
                '''
                Auxilar function to compute the colour gradient values
                for a given column given its range of values.

                parameters:
                    - column: the table's column identifier to which the colouring operation
                      is applied.
                '''
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
                    except ValueError:
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
        '''
        Hides table rows depending on search and filtering criteria.
        '''
        none = self.models['label_list_model'].get_filtered(LABEL_NONE)
        for row in range(0, self.rowCount()):
            filtered_out = False
            if self.search_string != '':
                item_text = str(self.item(row, headers.index(COLUMN_NAME)).text()).lower()
                filtered_out = self.search_string not in item_text
            if not filtered_out:
                labels_row = self.cellWidget(row, headers.index(COLUMN_LABELS)).getLabels()
                filtered_out = none and len(labels_row) == 0
                if not filtered_out and len(labels_row) > 0:
                    filtered_list = []
                    for _, label in enumerate(labels_row):
                        filtered_list.append(
                            self.models['label_list_model'].get_filtered(label))
                    filtered_out = all(filtered_list)
                filtered_out = filtered_out or \
                               self.models['system_list_model'].get_filtered(
                                   self.item(row, headers.index(COLUMN_SYSTEM)).text())
                filtered_out = filtered_out or \
                               self.models['status_list_model'].get_filtered(
                                   self.item(row, headers.index(COLUMN_STATUS)).text())
            self.setRowHidden(row, filtered_out)

    def show_all_rows(self):
        '''
        Makes all rows to go visible
        '''
        for row in range(0, self.rowCount()):
            self.setRowHidden(row, False)

    def resize_columns(self):
        '''
        Adapts the columns' width to their contents. Some workaround is needed for this
        to work properly.
        '''
        self.setVisible(False)
        self.resizeColumnsToContents()
        self.setVisible(True)

    def cell_is_clicked(self, table_item):
        '''
        This callback is invoked when a cell in the table is clicked. If the cell is in the year
        or status columns, the corresponding selector GUI will be displayed.

        parameters:
            - table_item: the clicked table item
        '''
        row = table_item.row()
        column = table_item.column()

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

    def cell_is_changed(self):
        '''
        This callback is invoked when the content of a cell changes. If that is the case,
        we set a flag to control that the user is aware that changes were made before
        quitting the application and therefore to make him decide whether he/she wants to
        save the changes in disk
        '''
        self.changed = True
