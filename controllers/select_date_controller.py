from PyQt5 import QtGui, QtWidgets
from views.select_date_dialog import Ui_SelectDateDialog
from util import util

from models.constants import INITIAL_YEAR, FINAL_YEAR

class SelectDateController(QtWidgets.QDialog):
    # UI and signal setup
    def __init__(self, year, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_SelectDateDialog()
        self.ui.setupUi(self)
        
        self.initializeUi(year)
        
        self.setupSignals()
        
        self.canceled = False
        
    def initializeUi(self, year):
        self.ui.sliderYear.setRange(INITIAL_YEAR, FINAL_YEAR)
        self.ui.sliderYear.setValue(INITIAL_YEAR)
        if year == 'Canceled':
            self.ui.radioButtonCanceled.click()
        elif year == 'TBA':
            self.ui.radioButtonTba.click()           
        else:
            self.ui.radioButtonYear.click()
        
        self.ui.lineEditYear.setText(year)
        if year != 'Canceled' and year != 'TBA':
            self.ui.sliderYear.setValue(int(year))
        else:
            self.ui.sliderYear.setEnabled(False)
            self.ui.lineEditYear.setEnabled(False)
        
    def setupSignals(self):
        self.ui.sliderYear.valueChanged.connect(self.sliderYearChanged)
        self.ui.lineEditYear.textChanged.connect(self.lineEditYearChanged)
        self.ui.pushButtonOk.clicked.connect(self.pushButtonOkClicked)
        self.ui.pushButtonCancel.clicked.connect(self.pushButtonCancelClicked)
        self.ui.radioButtonCanceled.clicked.connect(self.radioButtonCanceledClicked)
        self.ui.radioButtonTba.clicked.connect(self.radioButtonTbaClicked)
        self.ui.radioButtonYear.clicked.connect(self.radioButtonYearClicked)

    def radioButtonCanceledClicked(self):
        self.ui.sliderYear.setEnabled(False)
        self.ui.lineEditYear.setEnabled(False)
        self.ui.lineEditYear.setText('Canceled')
        
    def radioButtonTbaClicked(self):
        self.ui.sliderYear.setEnabled(False)
        self.ui.lineEditYear.setEnabled(False)
        self.ui.lineEditYear.setText('TBA')
        
    def radioButtonYearClicked(self):
        self.ui.sliderYear.setEnabled(True)
        self.ui.lineEditYear.setEnabled(True)
        self.ui.lineEditYear.setText(str(self.ui.sliderYear.value()))
        
    def sliderYearChanged(self):
        self.ui.lineEditYear.setText(str(self.ui.sliderYear.value()))
        
    def lineEditYearChanged(self):
        if self.ui.lineEditYear.isEnabled() and self.ui.lineEditYear.text() != '':
            try:            
                year = int(self.ui.lineEditYear.text())
                if year >= INITIAL_YEAR and year <= FINAL_YEAR:
                    self.ui.sliderYear.setValue(year)
            except ValueError:
                pass
                
    def pushButtonOkClicked(self):
        date = self.ui.lineEditYear.text()
        isNumber = self.ui.lineEditYear.isEnabled()
        try:
            if isNumber and (int(date) < INITIAL_YEAR or int(date) > FINAL_YEAR):
                util.showErrorMessage(self, 'The year must be a number between ' + str(INITIAL_YEAR) + ' and ' + str(FINAL_YEAR))
            else:
                self.hide()  
        except ValueError:
            util.showErrorMessage(self, 'The year must be a number')
                
    def pushButtonCancelClicked(self):
        self.canceled = True
        self.hide()
        
    def closeEvent(self, event):
        self.canceled = True

    def getDate(self):
        if self.canceled == True:
            return None
        else:
            return self.ui.lineEditYear.text()
