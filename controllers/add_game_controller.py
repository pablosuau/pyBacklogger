'''
Module that contains all the code required to add games to the backlog
'''

import re
import urllib.request
import urllib.error
from PyQt5 import QtCore, QtWidgets
from views.add_game_dialog import Ui_AddGameDialog
from controllers.search_results_controller import SearchResultsController
from util import util
from models.constants import SEARCH_URL, GAMEFAQS_URL


class AddGameController(QtWidgets.QDialog):
    '''
    Controller object for adding game functionality. Games are added asynchronously
    by means of threads.
    '''
    # pylint: disable=too-many-instance-attributes

    html_read = QtCore.pyqtSignal(str)

    def __init__(self, table, parent=None):
        '''
        Set up the user interface and the signals

        parameters:
            - table: a table object
            - parent: the parent of the controller
        '''
        QtWidgets.QDialog.__init__(self, parent)
        self.user_interface = Ui_AddGameDialog()
        self.user_interface.setupUi(self)

        self.table = table
        self.parent = parent

        self.pending_selected = None

        self.html = None
        self.add_by_url = None
        self.url = None
        self.progress = None

        self.setup_signals()

    def setup_signals(self):
        '''
        Connects interface's widgets signals to the corresponding slots
        '''
        self.user_interface.pushButtonOk.clicked.connect(self.ok_clicked)
        self.user_interface.pushButtonCancel.clicked.connect(self.cancel_clicked)
        self.user_interface.lineEditSearch.textChanged.connect(self.text_changed)
        self.html_read.connect(self.update_add_game)

    def ok_clicked(self):
        '''
        Signal slot for when the ok button is clicked. The process to add
        a game is launched
        '''
        self.add_game()

    def cancel_clicked(self):
        '''
        Signal slot for when the cancel button is clicked. The dialog
        is closed.
        '''
        self.hide()

    def text_changed(self):
        '''
        Signal slot for when we modify the text in the search bar. The ok button
        is enabled or disabled depending on whether there is any text on the
        search bar
        '''
        if str(self.user_interface.lineEditSearch.text()):
            self.user_interface.pushButtonOk.setEnabled(True)
        else:
            self.user_interface.pushButtonOk.setEnabled(False)

    def add_game(self):
        '''
        The controller code entry point. A first initial thread is created fo add a new game,
        if we are adding a game by URL, or to scrape the results of the search page, if we
        are adding by name.
        '''
        if self.user_interface.radioButtonUrl.isChecked():
            self.add_by_url = True
            # Search by URL
            self.url = str(self.user_interface.lineEditSearch.text()).strip()
            if not re.match(r'^[a-zA-Z]+://', self.url):
                self.url = 'http://' + self.url
            if not self.url.startswith(GAMEFAQS_URL):
                util.show_error_message(self.parent, 'The URL is not a valid GameFAQs one')
            else:
                # Download the content of the page
                self.launch_add_game_worker()
        else:
            self.add_by_url = False
            # Search by name
            self.url = SEARCH_URL + str(self.user_interface.lineEditSearch.text()).replace(' ', '+')
            # Download the content of the page
            self.launch_add_game_worker()

    def launch_add_game_worker(self):
        '''
        Creates a background process to add a game while displaying/updating a progress bar.
        '''
        self.progress = QtWidgets.QProgressDialog("Adding game", "", 0, 0, self)
        self.progress.setCancelButton(None)
        self.progress.setWindowModality(QtCore.Qt.WindowModal)
        self.progress.show()
        self.thread = self.AddGameWorker(self.url, self.html_read, self.table)
        self.thread.start()

    def update_add_game(self, html):
        '''
        Decides what's the next step after adding a game. If we are already adding games,
        and there are games pending, a new worker is created. If we are searching by name,
        the search dialog is displayed and a worker is created to add the first game in
        the list of selected games.

        parameters:
            - html: html code to be parsed in order to add a game
        '''
        self.progress.close()
        if self.add_by_url:
            self.table.add_game(self.url, str(html))
            if self.pending_selected != None:
                self.url = self.pending_selected[0]
                del self.pending_selected[0]
                if not self.pending_selected:
                    self.pending_selected = None
                self.launch_add_game_worker()
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
            if selected:
                self.add_by_url = True
                self.pending_selected = selected
                self.url = self.pending_selected[0]
                del self.pending_selected[0]
                if not self.pending_selected:
                    self.pending_selected = None
                self.launch_add_game_worker()

    class AddGameWorker(QtCore.QThread):
        '''
        Private class to create background processes in order to parse a piece of html code.
        '''
        def __init__(self, url, html_read, parent=None):
            QtCore.QThread.__init__(self, parent)
            self.exiting = False
            self.url = url
            self.html_read = html_read

        def run(self):
            '''
            Parses the html assigned to the worker.
            '''
            try:
                req = urllib.request.Request(self.url, headers={'User-Agent' : "Magic Browser"})
                response = urllib.request.urlopen(req)
                html = response.read().decode('ascii', 'ignore')
                self.html_read.emit(html)
            except urllib.error.HTTPError as exception:
                print(exception.code)
                print(exception.read())
                util.show_error_message(
                    self.parent(),
                    'Connection error: ' + exception.code + ' ' + exception.read()
                )
            except urllib.error.URLError as exception:
                print(exception.reason)
                util.show_error_message(self.parent(), 'Incorrect URL or no Internet connection')
        def __del__(self):
            self.exiting = True
