'''
This module controls the main dialog of the application
'''

import csv
import os
from shutil import copyfile
from PyQt5 import QtCore, QtWidgets
from views.main_window import Ui_MainWindow
from controllers.add_game_controller import AddGameController
from controllers.filter_games_controller import FilterGamesController
from controllers.sort_games_controller import SortGamesController
from controllers.reload_scores_controller import ReloadScoresController
from controllers.statistics_window_controller import StatisticsWindowController
from models.constants import HEADERS, HEADERS_EXTENDED, COLUMN_SYSTEM, COLUMN_STATUS, \
                             COLUMN_LABELS, COLUMN_ORDER

class MainWindowController(QtWidgets.QWidget):
    '''
    Controller object for the main window
    '''
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.user_interface = Ui_MainWindow()
        self.user_interface.setupUi(self)

        self.table = self.user_interface.table
        self.canceled = False

        self.initialize_ui()
        self.setup_signals()

    def initialize_ui(self):
        '''
        Simply maximize the main window
        '''
        self.setWindowState(QtCore.Qt.WindowMaximized)

    def setup_signals(self):
        '''
        Connects interface's widgets signals to the corresponding slots
        '''
        self.user_interface.pushButtonAddGame.clicked.connect(self.add_game_clicked)
        self.user_interface.pushButtonRemoveGame.clicked.connect(self.remove_game_clicked)
        self.user_interface.pushButtonLoadBacklog.clicked.connect(self.load_backlog_clicked)
        self.user_interface.pushButtonSaveBacklog.clicked.connect(self.save_backlog_clicked)
        self.user_interface.pushButtonReloadScores.clicked.connect(self.reload_scores_clicked)
        self.user_interface.pushButtonSortData.clicked.connect(self.sort_data_clicked)
        self.user_interface.pushButtonFilterData.clicked.connect(self.filter_data_clicked)
        self.user_interface.pushButtonStatistics.clicked.connect(self.statistics_clicked)
        self.user_interface.lineEditSearchGame.textChanged.connect(self.search_text_changed)

    def add_game_clicked(self):
        '''
        Display the dialog to add new games
        '''
        add_game_controller = AddGameController(self.table, parent=self)
        add_game_controller.show()

    def remove_game_clicked(self):
        '''
        Removes the game/games selected. A confirmation dialog is displayed first.
        '''
        indexes = self.table.selectionModel().selectedRows()
        if indexes:
            actual_indexes = []
            for index in sorted(indexes):
                if not self.table.isRowHidden(index.row()):
                    actual_indexes.append(index.row())
            name = []
            system = []
            for i in actual_indexes:
                name.append(self.table.item(i, 0).text())
                system.append(self.table.item(i, 1).text())

            delete_msg = 'Are you sure you want to delete the following entries?\n'
            for i in range(0, min(len(name), 10)):
                delete_msg = delete_msg + '\n' + name[i] + ' (' + system[i] + ')'
            if len(name) > 10:
                delete_msg = delete_msg + '\n...'
            reply = QtWidgets.QMessageBox.question(
                self, 'Confirm game removal',
                delete_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                progress = QtWidgets.QProgressDialog(
                    'Removing games', '', 0, len(actual_indexes), self)
                progress.setCancelButton(None)
                progress.setWindowModality(QtCore.Qt.WindowModal)
                for i in range(len(actual_indexes) - 1, -1, -1):
                    system = self.table.get_game_data(actual_indexes[i])[COLUMN_SYSTEM]
                    status = self.table.get_game_data(actual_indexes[i])[COLUMN_STATUS]
                    labels = self.table.cellWidget(
                        actual_indexes[i], HEADERS.index(COLUMN_LABELS)).getLabels()
                    self.table.models['system_list_model'].remove(system)
                    self.table.models['status_list_model'].remove(status)
                    for label in labels:
                        self.table.models['label_list_model'].remove(label)
                    self.table.removeRow(actual_indexes[i])
                    progress.setValue(len(actual_indexes) - i)
                self.table.changed = True

            self.table.update_colors()
            self.table.resize_columns()
        else:
            error = QtWidgets.QErrorMessage()
            error.showMessage('No games were selected')
            error.setWindowTitle('Remove game')
            error.exec_()

    def load_backlog_clicked(self):
        '''
        Displays the dialog to load a backlog and populates the table with the
        information of the selected file, if any was selected.
        '''
        confirm = False
        if self.table.changed:
            confirm = self.show_confirm_dialog()
        if confirm or not self.table.changed:
            filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Load backlog', '', '*.blg')[0]
            if filename:
                self.table.last_index = 0

                self.clear_options()

                for i in reversed(range(self.table.rowCount())):
                    self.table.removeRow(i)
                with open(filename, 'r') as file:
                    reader = csv.reader(file, delimiter=',', quoting=csv.QUOTE_ALL)
                    rows = sum(1 for row in reader)
                    file.seek(0)
                    progress = QtWidgets.QProgressDialog("Loading backlog", "", 0, rows, self)
                    progress.setCancelButton(None)
                    progress.setWindowModality(QtCore.Qt.WindowModal)
                    i = 0
                    self.table.setRowCount(rows)
                    self.table.loading = True
                    for row in reader:
                        row_dict = dict()
                        for header, cell in zip(HEADERS, row):
                            row_dict[header] = cell
                        self.table.add_game_row(row_dict, i)
                        progress.setValue(i+1)
                        i = i + 1
                    self.table.resize_columns()
                    self.table.update_colors()
                    self.table.changed = False
                    self.table.loading = False

    def save_backlog_clicked(self):
        '''
        Displays the dialog to save the backlog. It saves the backlog as a csv file, if any file
        was selected, after a backup copy of the original file was created.
        '''
        if not self.check_empty():
            filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save backlog', '', '*.blg')[0]
            if filename:
                if os.path.isfile(filename):
                    (directory, file) = os.path.split(str(filename))
                    name, _ = os.path.splitext(file)
                    copyfile(filename, os.path.join(directory, name + '.bak'))
                with open(filename, 'w') as file:
                    self.set_original_order()

                    writer = csv.writer(
                        file, delimiter=',', lineterminator='\n',
                        quoting=csv.QUOTE_ALL)
                    rows = self.table.rowCount()
                    progress = QtWidgets.QProgressDialog("Saving backlog", "", 0, rows, self)
                    progress.setCancelButton(None)
                    progress.setWindowModality(QtCore.Qt.WindowModal)
                    for i in range(0, rows):
                        data = self.table.get_game_data(i)
                        data_list = []
                        for header in HEADERS:
                            data_list.append(str(data[header]))
                        writer.writerows([data_list])
                        progress.setValue(i+1)

                    sort_games_controller = SortGamesController(self.table, self)
                    sort_games_controller.canceled = False
                    sort_games_controller.apply_sorting()
                    self.table.changed = False

    def reload_scores_clicked(self):
        '''
        Invokes the controller that reloads the data for the selected games
        by re-scraping
        '''
        if not self.check_empty():
            reload_scores_controller = ReloadScoresController(self.table, self)
            reload_scores_controller.reload_scores()

    def sort_data_clicked(self):
        '''
        Displays the dialog to select sorting criteria for the data
        '''
        self.user_interface.pushButtonSortData.setChecked(False)
        if not self.check_empty():
            sort_games_controller = SortGamesController(self.table, self)
            sort_games_controller.exec_()
            sort_games_controller.apply_sorting()
            self.user_interface.pushButtonSortData.setChecked(sort_games_controller.sorting_active)

    def filter_data_clicked(self):
        '''
        Displays the dialog to select filterin criteria for the data
        '''
        self.user_interface.pushButtonFilterData.setChecked(False)
        if not self.check_empty():
            filter_games_controller = FilterGamesController(self.table, self)
            filter_games_controller.exec_()
            filter_games_controller.apply_filtering()
            self.user_interface.pushButtonFilterData.setChecked(
                not filter_games_controller.filtering_all)

    def statistics_clicked(self):
        '''
        Displays the statistics window
        '''
        if not self.check_empty():
            statistics_window_controller = StatisticsWindowController(self)
            statistics_window_controller.exec_()

    def search_text_changed(self):
        '''
        Callback for when the text in the search edit field changes. Gives the control
        to the table object to do so.
        '''
        search_text = str(self.user_interface.lineEditSearchGame.text()).lower()
        self.table.search_string = search_text
        self.table.hide_rows()

    def check_empty(self):
        '''
        Displays an error message if the backlog is empty.
        '''
        empty = self.table.rowCount() == 0
        if empty:
            error = QtWidgets.QErrorMessage()
            error.showMessage('Add some games first!')
            error.setWindowTitle('No games')
            error.exec_()
        return empty

    def show_confirm_dialog(self):
        '''
        Displays a confirmation window for those cases in which an operation may cause
        a result that may not be cancelled.
        '''
        reply = QtWidgets.QMessageBox.question(
            self, 'Confirm action',
            'Your data changed since you loaded it. Are you sure you want to do this?',
            QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        return reply == QtWidgets.QMessageBox.Yes

    def closeEvent(self, event):
        # pylint: disable-msg=invalid-name
        '''
        Callback which is invoked when the main window is closed. It asks for confirmation
        in case there is unsaved data.

        Ignoring pylint warning about invalid name because this is overriding
        a method from the super class
        '''
        confirm = False
        if self.table.changed:
            confirm = self.show_confirm_dialog()
        if confirm or not self.table.changed:
            event.accept()
        else:
            event.ignore()

    def clear_options(self):
        '''
        Resets the interface options to the default values.
        '''
        self.user_interface.pushButtonSortData.setChecked(False)
        self.user_interface.pushButtonFilterData.setChecked(False)
        self.user_interface.lineEditSearchGame.setText('')

        self.table.models['system_list_model'].clear_filtered()
        self.table.models['status_list_model'].clear_filtered()
        self.table.models['label_list_model'].clear_filtered()

        self.table.show_all_rows()

    def set_original_order(self):
        '''
        Restores the order of the rows in the backlog to that in which
        they were read from the file/downloaded from GameFAQs
        '''
        self.table.models['sort_list_model'].clear()
        order = QtCore.Qt.AscendingOrder
        self.table.sortByColumn(HEADERS_EXTENDED.index(COLUMN_ORDER), order)
