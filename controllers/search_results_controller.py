'''
Code to control the search results interface. It allows to add the selected games
in the search results dialog to the backlog.
'''

from PyQt5 import QtGui, QtCore, QtWidgets
from lxml.html.soupparser import fromstring
from views.search_results_dialog import Ui_SearchResultsDialog
from models.constants import GAMEFAQS_URL

class SearchResultsController(QtWidgets.QDialog):
    '''
    Controller of the dialog to interact with game search results
    '''

    def __init__(self, html, parent=None):
        '''
        Initialises the user interface and sets up the signals

        parameters:
            - parent: the controller which is the parent of the search results dialog
        '''
        super(SearchResultsController, self).__init__(parent)

        self.view = Ui_SearchResultsDialog()
        self.view.setupUi(self)

        self.html = html
        self.canceled = False

        self.importing = None
        self.pending_selected = None

        self.checked = 0

        self.initialize_ui()
        self.setup_signals()

    def initialize_ui(self):
        '''
        Fills the view with the game search results
        '''
        systems = []
        names = []
        urls = []
        doc = fromstring(str(self.html))

        element = doc.xpath("//div[@class='search_result']")
        for search_result in element:
            name = (
                search_result.getchildren()[1]
                .getchildren()[0]
                .getchildren()[0]
                .getchildren()[0]
                .getchildren()[0]
                .text
                .strip()
            )

            details = search_result.getchildren()[1].getchildren()[1].getchildren()
            for detail in details:
                if detail.get('class') == 'sr_showall':
                    pass
                else:
                    product = detail.getchildren()[0].getchildren()[0]

                    systems.append(product.text.strip())
                    names.append(name)
                    urls.append(GAMEFAQS_URL + product.attrib['href'])

        # Displaying search results
        model = QtGui.QStandardItemModel()
        if systems:
            for system, name in zip(systems, names):
                item = QtGui.QStandardItem('(' + system + ') ' + name)
                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setData(QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)
                model.appendRow(item)
            model.itemChanged.connect(self.on_item_changed)
        else:
            item = QtGui.QStandardItem('No game was found')
            model.appendRow(item)
        self.view.listViewGames.setModel(model)

        self.urls = urls
        self.checked = 0
        self.view.pushButtonOk.setEnabled(False)

    def setup_signals(self):
        '''
        Connects the user interface control events to the corresponding signals
        '''
        self.view.pushButtonOk.clicked.connect(self.ok_clicked)
        self.view.pushButtonCancel.clicked.connect(self.cancel_clicked)

    def ok_clicked(self):
        '''
        Signal slot for the event of pressing the ok button
        '''
        self.hide()

    def cancel_clicked(self):
        '''
        Signal slot for the event of pressing the cancel button
        '''
        self.hide()
        self.canceled = True

    def closeEvent(self, _event):
        '''
        Signal slot for the event of closing the window. The event parameter is unused.
        '''
        # pylint: disable=invalid-name
        # pylint: disable=unused-argument
        self.canceled = True

    def on_item_changed(self, item):
        '''
        Modifies the behaviour of the items in the list so they behave like radio buttons
        '''
        if item.checkState() == QtCore.Qt.Checked:
            self.checked = self.checked + 1
            if self.checked == 1:
                self.view.pushButtonOk.setEnabled(True)
        else:
            self.checked = self.checked - 1
            if self.checked == 0:
                self.view.pushButtonOk.setEnabled(False)

    def get_search_results(self):
        '''
        Returns a list with the games that were selected by the user by means of the selection
        checkboxes.

        returns:
            - a list with the URLs of the selected games in the search results dialog
        '''
        selected = []
        if not self.canceled:
            model = self.view.listViewGames.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                    selected.append(self.urls[index])

        return selected
