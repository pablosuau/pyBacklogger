from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *

INITIAL_YEAR = 1940
FINAL_YEAR = 2100

class DateDialog(QDialog):
    def __init__(self, year, parent = None):
        super(DateDialog, self).__init__(parent)

        layout = QtGui.QVBoxLayout(self)
        
        radio_group = QtGui.QButtonGroup(self) 
        r0 = QtGui.QRadioButton("Canceled")
        r0.clicked.connect(self.r0_clicked)
        radio_group.addButton(r0)
        r1 = QtGui.QRadioButton("TBA")
        r1.clicked.connect(self.r1_clicked)
        radio_group.addButton(r1)
        r2 = QtGui.QRadioButton('Year:')
        r2.clicked.connect(self.r2_clicked)
        radio_group.addButton(r2)
        layout.addWidget(r0)
        layout.addWidget(r1)
        layout.addWidget(r2)

        self.slider = QtGui.QSlider(Qt.Horizontal)
        self.slider.setRange(INITIAL_YEAR, FINAL_YEAR)
        self.slider.setValue(INITIAL_YEAR)
        self.slider.valueChanged.connect(self.slider_changed)
        
        self.year_widget = QtGui.QLineEdit()
        self.year_widget.textChanged.connect(self.year_changed)
        
        if year == 'Canceled':
            r0.click()
            self.slider.setEnabled(False)
            self.year_widget.setEnabled(False)
        elif year == 'TBA':
            r1.click()
            self.slider.setEnabled(False)
            self.year_widget.setEnabled(False)
        else:
            r2.click()
        
        self.year_widget.setText(year)
        if year != 'Canceled' and year != 'TBA':
            self.slider.setValue(int(year))
        
        slider_layout = QtGui.QHBoxLayout(self)
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.year_widget)
        layout.addLayout(slider_layout)

        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def r0_clicked(self):
        self.slider.setEnabled(False)
        self.year_widget.setEnabled(False)
        self.year_widget.setText('Canceled')
        
    def r1_clicked(self):
        self.slider.setEnabled(False)
        self.year_widget.setEnabled(False)
        self.year_widget.setText('TBA')
        
    def r2_clicked(self):
        self.slider.setEnabled(True)
        self.year_widget.setEnabled(True)
        self.year_widget.setText(str(self.slider.value()))
        
    def slider_changed(self):
        self.year_widget.setText(str(self.slider.value()))
        
    def year_changed(self):
        if self.year_widget.isEnabled() and self.year_widget.text() != '':
            try:
                year = int(self.year_widget.text())
                if year >= INITIAL_YEAR and year <= FINAL_YEAR:
                    self.slider.setValue(year)
            except Exception:
                errorMessage=QErrorMessage(self)
                errorMessage.showMessage('The year must be a number')
                self.year_widget.setText(str(self.slider.value())) 

    def get_date(self):
        return (self.year_widget.text(), self.year_widget.isEnabled())

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getDate(year, parent = None):
        dialog = DateDialog(year, parent)
        date = 0
        isNumber = True
        result = True
        while (result and isNumber and (int(date) < INITIAL_YEAR or int(date) > FINAL_YEAR)):
           result = dialog.exec_() 
           (date, isNumber) = dialog.get_date()
           if isNumber and result == QDialog.Accepted:
               if (int(date) < INITIAL_YEAR or int(date) > FINAL_YEAR):
                   errorMessage=QErrorMessage(dialog)
                   errorMessage.showMessage('The year must be a number between ' + str(INITIAL_YEAR) + ' and ' + str(FINAL_YEAR))
                      
        return (date, result == QDialog.Accepted)