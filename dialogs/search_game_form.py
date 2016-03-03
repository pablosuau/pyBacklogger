from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from lxml.html.soupparser import fromstring

GAMEFAQS_URL = 'http://www.gamefaqs.com'

class SearchGameForm(QtGui.QDialog):
    def __init__(self, html, parent=None):
        super(SearchGameForm, self).__init__(parent)
        self.setWindowTitle('Search results')
        self.main_frame = QWidget()
        
        # search results
        systems = []
        names = []
        urls = []
        doc = fromstring(html)
        el = doc.xpath("//table[@class='results']")
        for table in el:
            rows = table.getchildren()[2:]
            for row in rows:
                system = row.getchildren()[0].text.strip()
                if system == '':
                    system = systems[-1]
                systems.append(system)
                names.append(row.getchildren()[1].findtext('a'))
                urls.append(GAMEFAQS_URL + row.getchildren()[1].getchildren()[0].attrib['href'])
                
        # Displaying search results
        model = QStandardItemModel()
        for i in range(0,len(systems)):
            item = QStandardItem('(' + systems[i] + ') ' + names[i])
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setData(Qt.Unchecked, Qt.CheckStateRole)
            model.appendRow(item)          
        self.listView = QListView()
        self.listView.setModel(model)
        
        
        self.button_ok = QtGui.QPushButton('Ok')
        self.button_cancel = QtGui.QPushButton('Cancel')
        layout_buttons = QtGui.QHBoxLayout()
        layout_buttons.addWidget(self.button_ok)        
        layout_buttons.addWidget(self.button_cancel)   
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(QtGui.QLabel('Select the game or games to add to your backlog'))
        layout.addWidget(self.listView)
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