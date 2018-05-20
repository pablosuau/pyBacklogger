from random import randint
from time import sleep
import urllib.request, urllib.error
from PyQt5 import QtGui, QtCore, QtWidgets
from lxml.html.soupparser import fromstring
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from models.constants import headers, COLUMN_NAME, COLUMN_RATING, COLUMN_VOTES, COLUMN_DIFFICULTY, COLUMN_LENGTH, COLUMN_URL

WARNING_MESSAGE = """<strong>A warning about doing too many requests to GameFAQs.</strong><br><br>\n 
Making too many requests to GameFAQs during the same day can result in your IP to be permanently blocked.
As a consequence of this, this application limits the size of the selection to be updated to 200 rows.
Please, try not to update more than this amount of games on a single day."""

class ReloadScoresController(QtWidgets.QWidget):
    progress_signal = QtCore.pyqtSignal(int)

    def __init__(self, table, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.table = table
        self.parent = parent

    def reload_scores(self):
        indexes = self.table.selectionModel().selectedRows()
        if len(indexes) == 0:
            error = QtWidgets.QErrorMessage(self.parent)
            error.setWindowModality(QtCore.Qt.WindowModal)
            error.showMessage('No games were selected')
            error.setWindowTitle('Reload scores')
            error.exec_()
        elif len(indexes) > 200:
            error = QtWidgets.QErrorMessage(self.parent)
            error.setWindowModality(QtCore.Qt.WindowModal)
            error.showMessage(WARNING_MESSAGE + '<br><br><strong>Please select less than 200 games to use this option.</strong>')
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
            self.progress.setWindowModality(Qt.WindowModal)
            self.thread = self.ReloadScoresWorker(self.table, indexes, self.progress_signal)
            self.progress_signal.connect(self.update_progress)
            self.progress.setValue(0)
            self.thread.start()

    def update_progress(self, i):
        self.progress.setValue(i+1)

    class ReloadScoresWorker(QtCore.QThread):
        def __init__(self, table, indexes, progress_signal, parent=None):
            QtCore.QThread.__init__(self, parent)
            self.exiting = False
            self.table = table
            self.indexes = indexes
            self.parent = parent
            self.progress_signal = progress_signal

        def run(self):
            try:
                for i in range(0, len(self.indexes)):
                    row = self.indexes[i].row()
                    sleep(randint(5, 15))
                    url = self.table.item(row, headers.index(COLUMN_URL)).text()
                    req = urllib.request.Request(str(url), headers={'User-Agent' : "Magic Browser"})
                    response = urllib.request.urlopen(req)
                    html = response.read().decode('ascii', 'ignore')
                    doc = fromstring(html)
                    # Updating the name, in case it changed
                    el = doc.xpath("//h1[@class='page-title']")
                    name = el[0].findtext('a')
                    self.table.item(row, headers.index(COLUMN_NAME)).setText(name)
                    # Updating the score
                    el = doc.xpath("//fieldset[@id='js_mygames_rate']")
                    if len(el) > 0:
                        rating_str = (
                            el[0]
                            .getchildren()[0]
                            .getchildren()[0]
                            .getchildren()[1]
                            .findtext('a')
                        )
                        if rating_str == None:
                            rating = '0.00'
                            votes = '0'
                        else:
                            rating = rating_str.split(' / ')[0]
                            votes_str = (
                                el[0]
                                .getchildren()[0]
                                .getchildren()[0]
                                .getchildren()[2]
                                .text
                            )
                            votes = votes_str.split(' ')[0]
                    else:
                        rating = '0.00'
                        votes = '0'
                    # Difficulty
                    element = doc.xpath("//fieldset[@id='js_mygames_diff']")
                    if len(element) > 0:
                        difficulty = element[0].getchildren()[0].getchildren()[0].getchildren()[1].findtext('a')
                        difficulty = element[0].getchildren()[0].getchildren()[0].getchildren()[1].findtext('a')
                        if difficulty is None:
                            difficulty = 'Not Yet Rated'
                    else:
                        difficulty = 'Not Yet Rated'
                    # Length
                    element = doc.xpath("//fieldset[@id='js_mygames_time']")
                    if len(element) > 0:
                        length = element[0].getchildren()[0].getchildren()[0].getchildren()[1].findtext('a')
                        length = element[0].getchildren()[0].getchildren()[0].getchildren()[1].findtext('a')
                        if length is None:
                            length = 'Not Yet Rated'
                        else:
                            length = length.split(' ')[0]
                    else:
                        length = 'Not Yet Rated'

                    self.table.item(row, headers.index(COLUMN_RATING)).setText(rating)
                    self.table.item(row, headers.index(COLUMN_VOTES)).setText(votes)
                    self.table.item(row, headers.index(COLUMN_DIFFICULTY)).setText(difficulty)
                    self.table.item(row, headers.index(COLUMN_LENGTH)).setText(length)
                    self.progress_signal.emit(i)
                self.table.compute_final_rating()
                self.table.changed = True
                self.table.update_colors()
            except urllib.error.URLError as e:
                print(e.reason)
                errorMessage = QtWidgets.QErrorMessage(self.parent)
                errorMessage.showMessage('Incorrect URL or not Internet connection')
            except urllib.error.HTTPError as e:
                print(e.code)
                print(e.read())
                errorMessage = QtWidgets.QErrorMessage(self.parent)
                errorMessage.showMessage('Connection error: ' + e.code + ' ' + e.read())

        def __del__(self):
            self.exiting = True
            self.wait()
