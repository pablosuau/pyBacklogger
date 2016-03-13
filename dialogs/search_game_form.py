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
        html = str(html)
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
                
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)  

        layout = QtGui.QVBoxLayout()              

        # Displaying search results        
        if len(systems) > 0:
            model = QStandardItemModel()
            for i in range(0,len(systems)):
                item = QStandardItem('(' + systems[i] + ') ' + names[i])
                item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                item.setData(Qt.Unchecked, Qt.CheckStateRole)
                model.appendRow(item)   
            model.itemChanged.connect(self.on_item_changed)
            self.listView = QListView()
            self.listView.setModel(model)
            layout.addWidget(QtGui.QLabel('Select the game or games to add to your backlog'))
            layout.addWidget(self.listView)
        else:
            layout.addWidget(QtGui.QLabel('No game was found'))          
            self.listView = None
            
        self.buttons.button(QDialogButtonBox.Ok).setEnabled(False)
        layout.addWidget(self.buttons)
        
        self.setLayout(layout)
        
        self.ok = False
        self.urls = urls
        self.checked = 0
     
    # Modification of the behaviour of the items, so they behave like radio buttons 
    def on_item_changed(self, item):
        if item.checkState() == QtCore.Qt.Checked:
            self.checked = self.checked + 1
            if self.checked == 1:
                self.buttons.button(QDialogButtonBox.Ok).setEnabled(True)
        else:
            self.checked = self.checked - 1
            if self.checked == 0:
                self.buttons.button(QDialogButtonBox.Ok).setEnabled(False)
            
    # static method to create the dialog and return a list of urls
    @staticmethod
    def getSearchResult(html, parent = None):
        dialog = SearchGameForm(html, parent)
        result = dialog.exec_()
        
        selected = []
        if dialog.listView != None:
            model = dialog.listView.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                    selected.append(dialog.urls[index])
            
        return (selected, result == QDialog.Accepted)