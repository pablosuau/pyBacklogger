'''
Code to control the dialog to select a date after clicking the corresponding
cell on the table.
'''

from PyQt5 import QtWidgets
from views.select_date_dialog import Ui_SelectDateDialog
from util import util

from models.constants import INITIAL_YEAR, FINAL_YEAR

class SelectDateController(QtWidgets.QDialog):
    '''
    Controller for the select date dialog
    '''
    def __init__(self, year, parent=None):
        '''
        Initialises the user interface and sets up the signals

        parameters:
            - year: the current value of the selected year field
            - parent: the controller which is the parent of the search results dialog
        '''
        QtWidgets.QDialog.__init__(self, parent)
        self.user_interface = Ui_SelectDateDialog()
        self.user_interface.setupUi(self)

        self.initialize_ui(year)

        self.setup_signals()

        self.canceled = False

    def initialize_ui(self, year):
        '''
        Initialises the user interface and selects the already
        existing year value

        parameters:
            - year: the current value of the selected year field
        '''
        self.user_interface.sliderYear.setRange(INITIAL_YEAR, FINAL_YEAR)
        self.user_interface.sliderYear.setValue(INITIAL_YEAR)
        if year == 'Canceled':
            self.user_interface.radioButtonCanceled.click()
        elif year == 'TBA':
            self.user_interface.radioButtonTba.click()
        else:
            self.user_interface.radioButtonYear.click()

        self.user_interface.lineEditYear.setText(year)
        if year != 'Canceled' and year != 'TBA':
            self.user_interface.sliderYear.setValue(int(year))
        else:
            self.user_interface.sliderYear.setEnabled(False)
            self.user_interface.lineEditYear.setEnabled(False)

    def setup_signals(self):
        '''
        Connects the user interface control events to the corresponding signals
        '''
        self.user_interface.sliderYear.valueChanged.connect(self.slider_year_changed)
        self.user_interface.lineEditYear.textChanged.connect(self.line_edit_year_changed)
        self.user_interface.pushButtonOk.clicked.connect(self.push_button_ok_clicked)
        self.user_interface.pushButtonCancel.clicked.connect(self.push_button_cancel_clicked)
        self.user_interface.radioButtonCanceled.clicked.connect(self.radio_button_canceled_clicked)
        self.user_interface.radioButtonTba.clicked.connect(self.radio_button_tba_clicked)
        self.user_interface.radioButtonYear.clicked.connect(self.radio_button_year_clicked)

    def radio_button_canceled_clicked(self):
        '''
        Signal slot of the event of pressing the 'cancelled' value button
        '''
        self.user_interface.sliderYear.setEnabled(False)
        self.user_interface.lineEditYear.setEnabled(False)
        self.user_interface.lineEditYear.setText('Canceled')

    def radio_button_tba_clicked(self):
        '''
        Signal slot for the event of pressing the 'TBA' value button
        '''
        self.user_interface.sliderYear.setEnabled(False)
        self.user_interface.lineEditYear.setEnabled(False)
        self.user_interface.lineEditYear.setText('TBA')

    def radio_button_year_clicked(self):
        '''
        Signal slot for the event of pressing the 'year' value button
        '''
        self.user_interface.sliderYear.setEnabled(True)
        self.user_interface.lineEditYear.setEnabled(True)
        self.user_interface.lineEditYear.setText(str(self.user_interface.sliderYear.value()))

    def slider_year_changed(self):
        '''
        Signal slot linked to the year selection slider
        '''
        self.user_interface.lineEditYear.setText(str(self.user_interface.sliderYear.value()))

    def line_edit_year_changed(self):
        '''
        Signal slot for the event of changing the text in the year
        line editor
        '''
        if self.user_interface.lineEditYear.isEnabled() and \
           self.user_interface.lineEditYear.text() != '':
            try:
                year = int(self.user_interface.lineEditYear.text())
                if year >= INITIAL_YEAR and year <= FINAL_YEAR:
                    self.user_interface.sliderYear.setValue(year)
            except ValueError:
                pass

    def push_button_ok_clicked(self):
        '''
        Signal slot for the event of pressing the ok button
        '''
        date = self.user_interface.lineEditYear.text()
        is_number = self.user_interface.lineEditYear.isEnabled()
        try:
            if is_number and (int(date) < INITIAL_YEAR or int(date) > FINAL_YEAR):
                util.show_error_message(
                    self,
                    'The year must be a number between ' + str(INITIAL_YEAR) +
                    ' and ' + str(FINAL_YEAR)
                )
            else:
                self.hide()
        except ValueError:
            util.show_error_message(self, 'The year must be a number')

    def push_button_cancel_clicked(self):
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

    def get_date(self):
        '''
        Returns the selected value (cancelled, TBA or a year)
        '''
        ret = None

        if not self.canceled:
            ret = self.user_interface.lineEditYear.text()

        return ret
