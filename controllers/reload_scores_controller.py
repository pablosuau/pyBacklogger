'''
Module that contains the code required to update the games' data by scraping
GameFAQs. Several warning messages are displayed when convinient to avoid the user's ip
to be banned.
'''

from random import randint
from time import sleep
import urllib.request
import urllib.error
from PyQt5 import QtCore, QtWidgets
from lxml.html.soupparser import fromstring
from models.constants import HEADERS, COLUMN_NAME, COLUMN_RATING, COLUMN_VOTES, COLUMN_DIFFICULTY, \
                             COLUMN_LENGTH, COLUMN_URL

WARNING_MESSAGE = """<strong>A warning about doing too many requests to GameFAQs.</strong><br><br>\n
Making too many requests to GameFAQs during the same day can result in your IP to be permanently blocked.
As a consequence of this, this application limits the size of the selection to be updated to 200 rows.
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
        if indexes:
            error = QtWidgets.QErrorMessage(self.parent)
            error.setWindowModality(QtCore.Qt.WindowModal)
            error.showMessage('No games were selected')
            error.setWindowTitle('Reload scores')
            error.exec_()
        elif len(indexes) > 200:
            error = QtWidgets.QErrorMessage(self.parent)
            error.setWindowModality(QtCore.Qt.WindowModal)
            error.showMessage(WARNING_MESSAGE + \
                '<br><br><strong>Please select less than 200 games to use this option.</strong>')
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
        def __init__(self, table, indexes, progress_signal, parent=None):
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
                    sleep(randint(5, 15))
                    url = self.table.item(row, HEADERS.index(COLUMN_URL)).text()
                    response = urllib.request.urlopen(
                        urllib.request.Request(
                            str(url),
                            headers={'User-Agent' : "Magic Browser"})
                        )
                    doc = fromstring(response.read().decode('ascii', 'ignore'))
                    # Updating the name, in case it changed
                    element = doc.xpath("//h1[@class='page-title']")
                    self.table.item(row,
                                    HEADERS.index(COLUMN_NAME)).setText(element[0].findtext('a'))
                    # Updating the score
                    element = doc.xpath("//fieldset[@id='js_mygames_rate']")
                    if element:
                        rating_str = (
                            element[0]
                            .getchildren()[0]
                            .getchildren()[0]
                            .getchildren()[1]
                            .findtext('a')
                        )
                        if rating_str is None:
                            rating = '0.00'
                            votes = '0'
                        else:
                            rating = rating_str.split(' / ')[0]
                            votes_str = (
                                element[0]
                                .getchildren()[0]
                                .getchildren()[0]
                                .getchildren()[2]
                                .text
                            )
                            votes = votes_str.split(' ')[0]
                    else:
                        rating = '0.00'
                        votes = '0'
                    self.table.item(row, HEADERS.index(COLUMN_RATING)).setText(rating)
                    self.table.item(row, HEADERS.index(COLUMN_VOTES)).setText(votes)
                    # Difficulty and length
                    def parse_difficulty_length(doc, id_element):
                        '''
                        Auxiliar function to parse difficulty and length, since the parsing process
                        is very similar
                        '''
                        element = doc.xpath("//fieldset[@id='" + id_element + "']")
                        if element:
                            value = element[0] \
                                    .getchildren()[0] \
                                    .getchildren()[0] \
                                    .getchildren()[1] \
                                    .findtext('a')
                            if value is None:
                                ret = 'Not Yet Rated'
                            else:
                                ret = value
                                if id_element == 'js_mygames_time':
                                    ret = ret.split(' ')[0]
                        else:
                            ret = 'Not Yet Rated'
                        return ret
                    self.table.item(row,
                                    HEADERS.index(COLUMN_DIFFICULTY)) \
                                    .setText(parse_difficulty_length(doc,
                                                                     'js_mygames_diff'))
                    self.table.item(row,
                                    HEADERS.index(COLUMN_LENGTH)) \
                                    .setText(parse_difficulty_length(doc,
                                                                     'js_mygames_time'))

                    self.progress_signal.emit(i)
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
