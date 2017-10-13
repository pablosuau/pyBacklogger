from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from lxml.html.soupparser import fromstring
from views.search_results_dialog import Ui_SearchResultsDialog
from models.constants import GAMEFAQS_URL

class SearchResultsController(QtWidgets.QDialog):
    # UI and signal setup
    def __init__(self, html, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
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
        
        el = doc.xpath("//div[@class='search_result']")
        for sr in el:
            right_panel = sr.getchildren()[1]
            name = right_panel.getchildren()[0].getchildren()[0].getchildren()[0].getchildren()[0].text.strip()
            
            details = right_panel.getchildren()[1].getchildren()
            for d in details:
                if d.get('class') == 'sr_showall':
                    pass
                else:
                    product = d.getchildren()[0].getchildren()[0]
                    system = product.text.strip()
                    url = GAMEFAQS_URL + product.attrib['href']
                    
                    systems.append(system)
                    names.append(name)
                    urls.append(url)    
                        
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
