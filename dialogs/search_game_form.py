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
        
        
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(QtGui.QLabel('Select the game or games to add to your backlog'))
        layout.addWidget(self.listView)
        layout.addWidget(buttons)
        
        self.setLayout(layout)
        
        self.ok = False
        self.urls = urls
        
    # static method to create the dialog and return a list of urls
    @staticmethod
    def getSearchResult(html, parent = None):
        dialog = SearchGameForm(html, parent)
        result = dialog.exec_()
        
        selected = []
        model = dialog.listView.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                selected.append(dialog.urls[index])
        
        return (selected, result == QDialog.Accepted)