'''
Code to control the sort games dialog. It lets the user decide
the criteria according to which the list of games is sorted
'''

from PyQt5 import QtCore, QtWidgets
from views.sort_dialog import Ui_SortDialog
import models.constants as constants

class SortGamesController(QtWidgets.QDialog):
    '''
    Controller for the sort games dialog
    '''
    def __init__(self, table, parent):
        '''
        Initialises the user interface and sets up the signals

        parameters:
            - table: the main table object in the application
            - parent: the controller which is the parent of the search results dialog
        '''
        QtWidgets.QDialog.__init__(self, parent)

        self.user_interface = Ui_SortDialog()
        self.user_interface.setupUi(self)

        self.table = table
        self.table.models['sort_list_model'].save_model()
        self.canceled = False
        self.sorting_active = False

        self.initialize_ui()
        self.setup_signals()

    def initialize_ui(self):
        '''
        Links controls with the corresponding models
        '''
        self.user_interface.sortByList.setModel(
            self.table.models['sort_list_model'].sort)
        self.user_interface.availableFieldsList.setModel(
            self.table.models['sort_list_model'].available)

    def setup_signals(self):
        '''
        Connects the user interface control events to the corresponding signals
        '''
        self.user_interface.pushButtonLeft.clicked.connect(self.left_clicked)
        self.user_interface.pushButtonRight.clicked.connect(self.right_clicked)
        self.user_interface.pushButtonUp.clicked.connect(self.up_clicked)
        self.user_interface.pushButtonDown.clicked.connect(self.down_clicked)
        self.user_interface.availableFieldsList.clicked.connect(self.activate_buttons_available)
        self.user_interface.sortByList.clicked.connect(self.activate_buttons_sort)
        self.user_interface.pushButtonOk.clicked.connect(self.ok_clicked)
        self.user_interface.pushButtonCancel.clicked.connect(self.cancel_clicked)
        self.user_interface.pushButtonSort.clicked.connect(self.sort_clicked)

    def activate_buttons_available(self):
        '''
        Signal slot for the event of selecting any of the options in the available
        fields list
        '''
        self.user_interface.pushButtonLeft.setEnabled(True)
        self.user_interface.sortByList.clearSelection()
        self.user_interface.pushButtonRight.setEnabled(False)
        self.user_interface.pushButtonUp.setEnabled(False)
        self.user_interface.pushButtonDown.setEnabled(False)
        self.user_interface.pushButtonSort.setEnabled(False)

    def activate_buttons_sort(self):
        '''
        Signal slot for the event of selecting any of the options in the
        sort by list
        '''
        self.user_interface.pushButtonRight.setEnabled(True)
        self.user_interface.availableFieldsList.clearSelection()
        self.user_interface.pushButtonLeft.setEnabled(False)
        self.user_interface.pushButtonUp.setEnabled(False)
        self.user_interface.pushButtonDown.setEnabled(False)
        self.user_interface.pushButtonSort.setEnabled(True)
        self.set_up_down()

    def clear_clicked(self):
        '''
        Auxiliar button to tidy up the interface after some
        operations are done by the user
        '''
        self.user_interface.availableFieldsList.clearSelection()
        self.user_interface.sortByList.clearSelection()
        self.user_interface.pushButtonLeft.setEnabled(False)
        self.user_interface.pushButtonRight.setEnabled(False)
        self.user_interface.pushButtonUp.setEnabled(False)
        self.user_interface.pushButtonDown.setEnabled(False)

    def set_up_down(self):
        '''
        Auxiliar function to enable/disable the buttons to modify
        the order of the sorting criteria depending on the
        contents of the different elements of the interface
        '''
        if self.user_interface.sortByList.model().rowCount() > 1:
            row = self.user_interface.sortByList.selectedIndexes()[0].row()
            if row > 0:
                self.user_interface.pushButtonUp.setEnabled(True)
            if row < self.user_interface.sortByList.model().rowCount() - 1:
                self.user_interface.pushButtonDown.setEnabled(True)

    def left_clicked(self):
        '''
        Signal slot for the event of clicking the button that moves
        a sorting criterium from the list of available fields to the
        list of sorting fields
        '''
        self.table.models['sort_list_model'].to_sort(
            self.user_interface.availableFieldsList.selectedIndexes())
        self.clear_clicked()

    def right_clicked(self):
        '''
        Signal slot for the event of clicking the button that moves
        a sorting criterium from the list of sorting fiels to the
        list of available fields
        '''
        self.table.models['sort_list_model'].to_available(
            self.user_interface.sortByList.selectedIndexes())
        self.clear_clicked()

    def up_down_clicked(self, method):
        '''
        Auxiliar function that encapsulates the common code of the
        signal slots for the events of clicking the up or down buttons
        '''
        index = method(self.user_interface.sortByList.selectedIndexes()[0])
        self.clear_clicked()
        self.user_interface.sortByList.selectionModel().select(
            index, QtCore.QItemSelectionModel.Select)
        self.set_up_down()

    def up_clicked(self):
        '''
        Signal slot for the event of clicking the button that moves a sorting
        criterium up in the list of sorting fields
        '''
        self.up_down_clicked(self.table.models['sort_list_model'].sort_up)

    def down_clicked(self):
        '''
        Signal slot for the event of clicking the button that moves a sorting
        criterium down in the list of sorting fields
        '''
        self.up_down_clicked(self.table.models['sort_list_model'].sort_down)

    def sort_clicked(self):
        '''
        Signal slot for the event of clicking the button to switch
        between ascending/descending order for a specific sorting criterium
        '''
        index = self.user_interface.sortByList.selectedIndexes()
        row = index[0].row()
        order = self.table.models['sort_list_model'].get_sort_order(index)
        if order == constants.ORDER_ASCENDING:
            new_order = constants.ORDER_DESCENDING
        else:
            new_order = constants.ORDER_ASCENDING
        order = self.table.models['sort_list_model'].set_sort_order(index, new_order)
        index = self.user_interface.sortByList.model().createIndex(row, 0)
        self.user_interface.sortByList.selectionModel().select(
            index, QtCore.QItemSelectionModel.Select)

    def ok_clicked(self):
        '''
        Signal slot for the event of pressing the ok button
        '''
        self.canceled = False
        self.hide()

    def cancel_clicked(self):
        '''
        Signal slot for the event of pressing the cancel button
        '''
        self.canceled = True
        self.hide()

    def closeEvent(self, event):
        '''
        Signal slot for the event of closing the window. The event parameter is unused.
        '''
        # pylint: disable=invalid-name
        # pylint: disable=unused-argument
        self.canceled = True

    def apply_sorting(self):
        '''
        Applies the selected sorting criteria to the data in the table
        '''
        if not self.canceled:
            self.table.setVisible(False)
            (sort_fields, sort_order) = self.table.models['sort_list_model'].get_sort_fields()

            if sort_fields:
                for i in range(0, len(sort_fields)):
                    j = len(sort_fields) - i - 1
                    index_column = constants.headers.index(sort_fields[j])
                    if sort_order[j] == constants.ORDER_ASCENDING:
                        order = QtCore.Qt.AscendingOrder
                    else:
                        order = QtCore.Qt.DescendingOrder
                    self.table.sortByColumn(index_column, order)
            else:
                order = QtCore.Qt.AscendingOrder
                self.table.sortByColumn(
                    constants.headers_extended.index(constants.COLUMN_ORDER), order
                )

            self.table.setVisible(True)
        else:
            self.table.models['sort_list_model'].restore_model()

        self.sorting_active = len(self.table.models['sort_list_model'].get_sort_fields()[0]) > 0
