from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from lxml.html.soupparser import fromstring
from views.search_results_dialog import Ui_SearchResultsDialog
from models.constants import GAMEFAQS_URL

class SearchResultsController(QtGui.QDialog):
    # UI and signal setup
    def __init__(self, html, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_SearchResultsDialog()
        self.ui.setupUi(self)
        
        self.html = html
        self.canceled = False
        
        self.importing = None
        self.pending_selected = None
        
        self.initializeUi()
        self.setupSignals()
        
    def initializeUi(self):
        # search results
        html = str(self.html)
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
        if len(systems) > 0:
            for i in range(0,len(systems)):
                item = QStandardItem('(' + systems[i] + ') ' + names[i])
                item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                item.setData(Qt.Unchecked, Qt.CheckStateRole)
                model.appendRow(item)   
            model.itemChanged.connect(self.on_item_changed)
        else:
            item = QStandardItem('No game was found')
            model.appendRow(item)
        self.ui.listViewGames.setModel(model)
            
        self.urls = urls
        self.checked = 0
        self.ui.pushButtonOk.setEnabled(False)
        
        
    def setupSignals(self):
        self.ui.pushButtonOk.clicked.connect(self.okClicked)
        self.ui.pushButtonCancel.clicked.connect(self.cancelClicked)
    
        # Signal slots 
    def okClicked(self):
        self.hide()
    
    def cancelClicked(self):
        self.hide()   
        self.canceled = True
        
    def closeEvent(self, event):
        self.canceled = True
    
    # Modification of the behaviour of the items, so they behave like radio buttons 
    def on_item_changed(self, item):
        if item.checkState() == QtCore.Qt.Checked:
            self.checked = self.checked + 1
            if self.checked == 1:
                self.ui.pushButtonOk.setEnabled(True)
        else:
            self.checked = self.checked - 1
            if self.checked == 0:
                self.ui.pushButtonOk.setEnabled(False)
                
    def get_search_results(self):
        selected = []
        if not self.canceled:
            model = self.ui.listViewGames.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                    selected.append(self.urls[index])
            
        return selected