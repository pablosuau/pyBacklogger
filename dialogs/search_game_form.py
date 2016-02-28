from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from lxml.html.soupparser import fromstring


class SearchGameForm(QtGui.QDialog):
    def __init__(self, html, parent=None):
        super(SearchGameForm, self).__init__(parent)
        self.setWindowTitle('Search results')
        self.main_frame = QWidget()
        
        # Displaying results
        doc = fromstring(html)
        el = doc.xpath("//table[@class='results']")
        for table in el:
            rows = table.getChildren()[2:]
            print(rows)
            print('===')
        
        
        
        self.button_ok = QtGui.QPushButton('Ok')
        self.button_cancel = QtGui.QPushButton('Cancel')
        layout_buttons = QtGui.QHBoxLayout()
        layout_buttons.addWidget(self.button_ok)        
        layout_buttons.addWidget(self.button_cancel)   
        
        layout = QtGui.QVBoxLayout()
        layout.addLayout(layout_buttons)
        
        self.setLayout(layout)
        
        self.ok = False
        
        self.button_ok.clicked.connect(self.okClicked)
        self.button_cancel.clicked.connect(self.cancelClicked)
        
    def okClicked(self):
        self.ok = True
        self.close()
    
    def cancelClicked(self):
        self.ok = False
        self.close()