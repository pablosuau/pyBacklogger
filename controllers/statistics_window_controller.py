from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from views.statistics_dialog import Ui_StatisticsWindow
from models.constants import headers, COLUMN_SYSTEM, COLUMN_STATUS, COLUMN_LABELS, COLUMN_YEAR

class StatisticsWindowController(QtGui.QDialog):
    # UI and signal setup
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
       
        self.ui = Ui_StatisticsWindow()
        self.ui.setupUi(self)
        self.table = parent.table
   
        self.initializeUi()     
        self.setupSignals()
    
    def initializeUi(self):
        self.buttons = [self.ui.pushButtonSystem, self.ui.pushButtonYear, self.ui.pushButtonLabel, self.ui.pushButtonStatus]
        self.columns = [COLUMN_SYSTEM, COLUMN_YEAR, COLUMN_LABELS, COLUMN_STATUS]        
        # Make buttons checkable
        for b in self.buttons:
            b.setCheckable(True)
        
    def setupSignals(self):
        self.ui.pushButtonClose.clicked.connect(self.close_clicked)
        for b in self.buttons:
            b.clicked.connect(self.option_clicked)
        
    def close_clicked(self):
        self.close()
        
    def option_clicked(self):
        checked = 0
        selected = []
        for b in self.buttons:
            if b.isChecked():
                checked = checked + 1
                selected.append(self.buttons.index(b))
                
        self.ui.plainTextEdit.clear()
        
        if checked > 2:
            self.ui.plainTextEdit.appendPlainText('Only two criteria can be selected')
        elif checked > 1:
            results = dict()
            for row in range(0, self.table.rowCount()):
                 value1 = self.table.item(row, headers.index(self.columns[selected[0]])).text()
                 value2 = self.table.item(row, headers.index(self.columns[selected[1]])).text()
                 
                 if value1 not in results.keys():
                     results[value1] = dict()
                 if value2 not in results[value1].keys():
                     results[value1][value2] = 1
                 else:
                     results[value1][value2] = results[value1][value2] + 1
                 
            for r1 in sorted(results.keys()):
                self.ui.plainTextEdit.appendPlainText(r1)
                total = 0
                for r2 in results[r1].keys():
                    total = total + results[r1][r2]
                for r2 in sorted(results[r1].keys()):
                    value = "%.2f" % (results[r1][r2]/float(total)*100)
                    self.ui.plainTextEdit.appendPlainText('    ' + r2 + ': ' + value + '% (' + str(results[r1][r2]) + ')')
        elif checked == 1:
            results = dict()
            for row in range(0, self.table.rowCount()):
                value = self.table.item(row, headers.index(self.columns[selected[0]])).text()
                if value not in results.keys():
                    results[value] = 1
                else:
                    results[value] = results[value] + 1
            total = 0
            for r in results.keys():
                total = total + results[r]
            for r in sorted(results.keys()):
                value = "%.2f" % (results[r]/float(total)*100)
                self.ui.plainTextEdit.appendPlainText(r + ': ' + value + '% (' + str(results[r]) + ')')