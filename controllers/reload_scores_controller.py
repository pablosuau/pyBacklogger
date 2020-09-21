'''
Module that contains the code required to update the games' data by scraping
GameFAQs. Several warning messages are displayed when convinient to avoid the user's ip
to be banned.
'''

from random import randint
from time import sleep
import numpy as np
import urllib.request
import urllib.error
import rawgpy
from rawgpy.game import Game
from PyQt5 import QtCore, QtWidgets
from lxml.html.soupparser import fromstring
from util import util
from util.util import parse_difficulty_length
from models.constants import RAWG_USERAGENT
from models.constants import HEADERS, COLUMN_NAME, COLUMN_RATING, COLUMN_VOTES, COLUMN_ID

WARNING_MESSAGE = """<strong>A warning about doing too many requests.</strong><br><br>\n
Making too many requests to rawg.io may overload their servers.
As a consequence of this, this application limits the size of the selection to be updated to 100 rows.
Please, try not to update more than this amount of games on a single day."""

class ReloadScoresController(QtWidgets.QWidget):
    '''
    Controller object to update games' data by scraping GameFAQs
    '''
    progress_signal = QtCore.pyqtSignal(int)

    def __init__(self, table, parent=None):
        '''
        There is no user interface linked to this controller,
        so this method simply stores references to the requried
        objects.

        parameters:
            - table: a table object
            - parent: the parent of the controller
        '''
        QtWidgets.QWidget.__init__(self, parent)
        self.table = table
        self.parent = parent
        self.progress = None

    def reload_scores(self):
        '''
        Checks that between 1 and 200 games where selected, and then
        creates a brackground thread to make the scraping requests.
        '''
        indexes = self.table.selectionModel().selectedRows()
        if not indexes:
            error = QtWidgets.QErrorMessage(self.parent)
            error.setWindowModality(QtCore.Qt.WindowModal)
            error.showMessage('No games were selected')
            error.setWindowTitle('Reload scores')
            error.exec_()
        elif len(indexes) > 100:
            error = QtWidgets.QErrorMessage(self.parent)
            error.setWindowModality(QtCore.Qt.WindowModal)
            error.showMessage(WARNING_MESSAGE + \
                '<br><br><strong>A maximum of 100 games can be selected</strong>')
            error.setWindowTitle('Reload scores')
            error.exec_()
        else:
            error = QtWidgets.QErrorMessage(self.parent)
            error.setWindowModality(QtCore.Qt.WindowModal)
            error.showMessage(WARNING_MESSAGE)
            error.setWindowTitle('Reload scores')
            self.progress = QtWidgets.QProgressDialog(
                'Updating scores', '', 0, len(indexes), self.parent)
            self.progress.setWindowTitle('Reload scores')
            self.progress.setCancelButton(None)
            self.progress.setWindowModality(QtCore.Qt.WindowModal)
            self.thread = self.ReloadScoresWorker(self.table, indexes, self.progress_signal)
            self.progress_signal.connect(self.update_progress)
            self.progress.setValue(0)
            self.thread.start()

    def update_progress(self, i):
        '''
        Updates the progress bar
        '''
        self.progress.setValue(i+1)

    class ReloadScoresWorker(QtCore.QThread):
        '''
        Object for the thread that will scrape GameFAQs to update
        games' data.
        '''
        def __init__(self, table, indexes, progress_signal, parent = None):
            '''
            Initialization of the thread.

            parameters:
                - table: the table object
                - indexes: the index of the games to update
                - progress_signal: the signal linked to the progress bar dialog
                - parent: the parent object
            '''
            QtCore.QThread.__init__(self, parent)
            self.exiting = False
            self.table = table
            self.indexes = indexes
            self.parent = parent
            self.progress_signal = progress_signal

        def run(self):
            '''
            Downloads the HTML data from GameFAQs for the selected games and
            applies the required updated to the data in the table.
            '''
            try:
                for i in range(0, len(self.indexes)):
                    row = self.indexes[i].row()
                    sleep(randint(1, 5))
                    game_id = self.table.item(row, HEADERS.index(COLUMN_ID)).text()
                    try:
                        rawg = rawgpy.RAWG(RAWG_USERAGENT)
                        game = Game({'slug': game_id})
                        game.populate()
                        self.progress_signal.emit(i)

                        self.table.item(row,
                                        HEADERS.index(COLUMN_NAME)).setText(game.name)
                        self.table.item(row, 
                                        HEADERS.index(COLUMN_RATING)).setText(str(game.rating))
                        self.table.item(row, 
                                        HEADERS.index(COLUMN_VOTES)) \
                                  .setText(str(np.sum([r['count'] for r in game.ratings])))
                    except Exception as e:
                        print(e)
                        util.show_error_message(self.parent, 'The game data couldn\'t be retrieved')

                self.table.compute_final_rating()
                self.table.changed = True
                self.table.update_colors()
            except urllib.error.HTTPError as exception:
                print(exception.code)
                print(exception.read())
                error_message = QtWidgets.QErrorMessage(self.parent)
                error_message.showMessage(
                    'Connection error: ' + exception.code + ' ' + exception.read())
            except urllib.error.URLError as exception:
                print(exception.reason)
                error_message = QtWidgets.QErrorMessage(self.parent)
                error_message.showMessage('Incorrect URL or not Internet connection')

        def __del__(self):
            self.exiting = True
            self.wait()
