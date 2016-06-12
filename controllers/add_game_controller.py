from PyQt4 import QtGui, QtCore
import re
import urllib2
from views.add_game_dialog import Ui_AddGameDialog
from dialogs.search_game_form import SearchGameForm

GAMEFAQS_URL = 'http://www.gamefaqs.com/'
SEARCH_URL = GAMEFAQS_URL + 'search?game='

class AddGameController(QtGui.QDialog):
    # UI and signal setup
    def __init__(self, table, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_AddGameDialog()
        self.ui.setupUi(self)
        
        self.table = table
        
        self.importing = None
        
        self.setupSignals()
        
    def setupSignals(self):
        self.ui.pushButtonOk.clicked.connect(self.okClicked)
        self.ui.pushButtonCancel.clicked.connect(self.cancelClicked)
        self.ui.lineEditSearch.textChanged.connect(self.textChanged)
        
    # Signal slots 
    def okClicked(self):
        self.addGame()
        self.close()
    
    def cancelClicked(self):
        self.close()
        
    def textChanged(self):
        if len(str(self.ui.lineEditSearch.text()))>0:
            self.ui.pushButtonOk.setEnabled(True)
        else:
            self.ui.pushButtonOk.setEnabled(False)
        
    # Controller
    def addGame(self):
        if self.ui.radioButtonUrl.isChecked():
            self.add_by_url = True
            # Search by URL
            self.url = str(self.ui.lineEditSearch.text())
            if not re.match(r'^[a-zA-Z]+://', self.url):
                self.url = 'http://' + self.url
            if not self.url.startswith(GAMEFAQS_URL):
                errorMessage = QtGui.QErrorMessage(self.parent())
                errorMessage.setWindowTitle('Add game')
                errorMessage.showMessage('The URL is not a valid GameFAQs one')
            else:
                # Download the content of the page
                 self.launchAddGameWorker()           
        else:
            self.add_by_url = False
            # Search by name
            self.url = SEARCH_URL + str(self.ui.lineEditSearch.text()).replace(' ','+')
            # Download the content of the page
            self.launchAddGameWorker()
                
    def launchAddGameWorker(self):
        self.progress = QtGui.QProgressDialog("Adding game", "", 0, 0, self)
        self.progress.setCancelButton(None)
        self.progress.setWindowModality(QtCore.Qt.WindowModal)
        self.progress.show()
        self.thread = self.AddGameWorker(self.url, self.table)
        self.connect(self.thread, QtCore.SIGNAL("htmlRead(QString)"), self.updateAddGame)
        self.thread.start()
    
    def updateAddGame(self, html):
        self.progress.close()
        if self.add_by_url:
            self.table.addGame(self.url, str(html))
            self.table.scrollToBottom()
            if self.pending_selected != None:
                self.url = self.pending_selected[0]
                del(self.pending_selected[0])   
                if len(self.pending_selected) == 0:
                    self.pending_selected = None
                self.launchAddGameWorker()
            elif self.importing != None:
                self.importGames()
        else:
            (selected, result) = SearchGameForm.getSearchResult(html, parent = None)
            if result:
                self.add_by_url = True
                self.pending_selected = selected
                self.url = self.pending_selected[0]
                del(self.pending_selected[0])   
                if len(self.pending_selected) == 0:
                    self.pending_selected = None
                self.launchAddGameWorker()
            elif self.importing != None:
                self.importGames()

    class AddGameWorker(QtCore.QThread):
        def __init__(self, url, parent=None):
            QtCore.QThread.__init__(self, parent)
            self.exiting = False
            self.url = url
        
        def run(self):
            try:
                req = urllib2.Request(self.url, headers={'User-Agent' : "Magic Browser"}) 
                response = urllib2.urlopen(req)
                self.html = response.read().decode('ascii','ignore')
                self.emit(QtCore.SIGNAL("htmlRead(QString)"), self.html)
            except urllib2.URLError as e:
                print e.reason   
                errorMessage = QtGui.QErrorMessage(self.parent())
                errorMessage.setWindowTitle('Add game')
                errorMessage.showMessage('Incorrect URL or not Internet connection')
            except urllib2.HTTPError as e:
                print e.code
                print e.read() 
                errorMessage = QtGui.QErrorMessage(self.parent())
                errorMessage.setWindowTitle('Add game')
                errorMessage.showMessage('Connection error: ' + e.code + ' ' + e.read())   
        def __del__(self):
            self.exiting = True
            self.wait()