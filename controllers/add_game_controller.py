from PyQt5 import QtGui, QtCore, QtWidgets
import re
import urllib2
from views.add_game_dialog import Ui_AddGameDialog
from controllers.search_results_controller import *
from util import util
from models.constants import SEARCH_URL, GAMEFAQS_URL


class AddGameController(QtWidgets.QDialog):

    htmlRead = QtCore.pyqtSignal(str)

    # UI and signal setup
    def __init__(self, table, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_AddGameDialog()
        self.ui.setupUi(self)

        self.table = table
        self.parent = parent

        self.pending_selected = None

        self.setupSignals()

    def setupSignals(self):
        self.ui.pushButtonOk.clicked.connect(self.okClicked)
        self.ui.pushButtonCancel.clicked.connect(self.cancelClicked)
        self.ui.lineEditSearch.textChanged.connect(self.textChanged)
        self.htmlRead.connect(self.updateAddGame)

    # Signal slots
    def okClicked(self):
        self.addGame()
        #self.hide()

    def cancelClicked(self):
        self.hide()

    def textChanged(self):
        if len(str(self.ui.lineEditSearch.text())) > 0:
            self.ui.pushButtonOk.setEnabled(True)
        else:
            self.ui.pushButtonOk.setEnabled(False)

    # Controller
    def addGame(self):
        if self.ui.radioButtonUrl.isChecked():
            self.add_by_url = True
            # Search by URL
            self.url = str(self.ui.lineEditSearch.text()).strip()
            if not re.match(r'^[a-zA-Z]+://', self.url):
                self.url = 'http://' + self.url
            if not self.url.startswith(GAMEFAQS_URL):
                util.showErrorMessage(self.parent, 'The URL is not a valid GameFAQs one')
            else:
                # Download the content of the page
                self.launchAddGameWorker()
        else:
            self.add_by_url = False
            # Search by name
            self.url = SEARCH_URL + str(self.ui.lineEditSearch.text()).replace(' ', '+')
            # Download the content of the page
            self.launchAddGameWorker()

    def launchAddGameWorker(self):
        self.progress = QtWidgets.QProgressDialog("Adding game", "", 0, 0, self)
        self.progress.setCancelButton(None)
        self.progress.setWindowModality(QtCore.Qt.WindowModal)
        self.progress.show()
        self.thread = self.AddGameWorker(self.url, self.htmlRead, self.table)
        self.thread.start()

    def updateAddGame(self, html):
        self.progress.close()
        if self.add_by_url:
            self.table.add_game(self.url, str(html))
            if self.pending_selected != None:
                self.url = self.pending_selected[0]
                del self.pending_selected[0]
                if len(self.pending_selected) == 0:
                    self.pending_selected = None
                self.launchAddGameWorker()
            else:
                self.parent.clear_options()
                self.parent.set_original_order()

                self.table.update_colors()
                self.hide()
                self.table.resize_columns()

                self.table.scrollToBottom()

        else:
            src = SearchResultsController(html, parent=self)
            src.exec_()
            selected = src.get_search_results()
            print(selected)
            if len(selected) > 0:
                self.add_by_url = True
                self.pending_selected = selected
                self.url = self.pending_selected[0]
                del self.pending_selected[0]
                if len(self.pending_selected) == 0:
                    self.pending_selected = None
                self.launchAddGameWorker()

    class AddGameWorker(QtCore.QThread):
        def __init__(self, url, htmlRead, parent=None):
            QtCore.QThread.__init__(self, parent)
            self.exiting = False
            self.url = url
            self.htmlRead = htmlRead

        def run(self):
            try:
                req = urllib2.Request(self.url, headers={'User-Agent' : "Magic Browser"})
                response = urllib2.urlopen(req)
                self.html = response.read().decode('ascii', 'ignore')
                self.htmlRead.emit(self.html)
            except urllib2.URLError as e:
                print(e.reason)
                util.showErrorMessage(self.parent(), 'Incorrect URL or not Internet connection')
            except urllib2.HTTPError as e:
                print(e.code)
                print(e.read())
                util.showErrorMessage(self.parent(), 'Connection error: ' + e.code + ' ' + e.read())
        def __del__(self):
            self.exiting = True
            self.wait()
