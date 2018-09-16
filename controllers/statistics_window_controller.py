'''
Code to populate the statistics dialog with the corresponding data.
'''

from PyQt5 import QtWidgets
from views.statistics_dialog import Ui_StatisticsWindow
from models.constants import HEADERS, COLUMN_SYSTEM, COLUMN_STATUS, \
                             COLUMN_LABELS, COLUMN_YEAR, LABEL_NONE

class StatisticsWindowController(QtWidgets.QDialog):
    '''
    Controller for the dialog that shows statistics about the collection
    '''
    def __init__(self, parent=None):
        '''
        Initialises the user interface and sets up the signals

        parameters:
            - parent: the controller which is the parent of the search results dialog
        '''
        QtWidgets.QDialog.__init__(self, parent)

        self.user_interface = Ui_StatisticsWindow()
        self.user_interface.setupUi(self)
        self.table = parent.table

        self.initialize_ui()
        self.setup_signals()

    def initialize_ui(self):
        '''
        Sets up the buttons in the dialog
        '''
        self.buttons = [
            self.user_interface.pushButtonSystem,
            self.user_interface.pushButtonYear,
            self.user_interface.pushButtonLabel,
            self.user_interface.pushButtonStatus
        ]
        self.columns = [COLUMN_SYSTEM, COLUMN_YEAR, COLUMN_LABELS, COLUMN_STATUS]
        # Make buttons checkable
        for button in self.buttons:
            button.setCheckable(True)

    def setup_signals(self):
        '''
        Connects the user interface control events to the corresponding signals
        '''
        self.user_interface.pushButtonClose.clicked.connect(self.close_clicked)
        for button in self.buttons:
            button.clicked.connect(self.option_clicked)

    def close_clicked(self):
        '''
        Signal for the event of clicking the close button
        '''
        self.close()

    def option_clicked(self):
        '''
        Signal for the event of clicking any of the buttons on the top
        of the dialog which let the user select the variables to produce
        statistics for.
        '''
        checked = 0
        selected = []
        for button in self.buttons:
            if button.isChecked():
                checked = checked + 1
                selected.append(self.buttons.index(button))

        self.user_interface.plainTextEdit.clear()

        if checked > 2:
            self.user_interface.plainTextEdit.appendPlainText('Only two criteria can be selected')
        elif checked > 1:
            self._display_multiple(selected)
        elif checked == 1:
            self._display_single(selected)

    def _display_multiple(self, selected):
        '''
        Private method to display statistics when two criteria are selected

        parameters:
            - selected: list of selected criteria
        '''
        results = dict()
        for row in range(0, self.table.rowCount()):
            value1 = str(self.table.item(row, HEADERS.index(self.columns[selected[0]])).text())
            value1 = value1.split(',') # To deal wiht labels
            value1 = [v1.strip() if v1 != '' else LABEL_NONE for v1 in value1]
            value2 = str(self.table.item(row, HEADERS.index(self.columns[selected[1]])).text())
            value2 = value2.split(',')
            value2 = [v2.strip() if v2 != '' else LABEL_NONE for v2 in value2]

            for v1strip in value1:
                if v1strip not in results.keys():
                    results[v1strip] = dict()
                for v2strip in value2:
                    if v2strip not in results[v1strip].keys():
                        results[v1strip][v2strip] = 1
                    else:
                        results[v1strip][v2strip] = results[v1strip][v2strip] + 1

        for result1 in sorted(results.keys()):
            self.user_interface.plainTextEdit.appendPlainText(result1)
            total = 0
            for result2 in results[result1].keys():
                total = total + results[result1][result2]
            for result2 in sorted(results[result1].keys()):
                value = "%.2f" % (results[result1][result2]/float(total)*100)
                self.user_interface.plainTextEdit.appendPlainText(
                    '    ' + result2 + ': ' + value +
                    '% (' + str(results[result1][result2]) + ')'
                )

    def _display_single(self, selected):
        '''
        Private method to display statistics when a single criterion is selected
        '''
        results = dict()
        for row in range(0, self.table.rowCount()):
            values = str(self.table.item(row, HEADERS.index(self.columns[selected[0]])).text())
            values = values.split(',') # To deal with labels
            values = [v.strip() if v != '' else LABEL_NONE for v in values]
            for vstrip in values:
                if vstrip not in results.keys():
                    results[vstrip] = 1
                else:
                    results[vstrip] = results[vstrip] + 1
        total = 0
        keys = results.keys()
        for result in keys:
            total = total + results[result]
        for result in sorted(keys):
            value = "%.2f" % (results[result]/float(total)*100)
            self.user_interface.plainTextEdit.appendPlainText(
                result + ': ' + value + '% (' + str(results[result]) + ')'
            )
