'''
Global constants for the application
'''
from PyQt5 import QtGui

GAMEFAQS_URL = 'https://gamefaqs.gamespot.com'
SEARCH_URL = GAMEFAQS_URL + '/search?game='

COLUMN_NAME = 'Name'
COLUMN_SYSTEM = 'System'
COLUMN_YEAR = 'Year'
COLUMN_RATING = 'Rating'
COLUMN_VOTES = 'Votes'
COLUMN_WEIGHTED = 'Weighted\nRating'
COLUMN_LENGTH = 'Length'
COLUMN_DIFFICULTY = 'Difficulty'
COLUMN_STATUS = 'Status'
COLUMN_LABELS = 'Labels'
COLUMN_NOTES = 'Notes'
COLUMN_URL = 'URL'
COLUMN_ORDER = 'Order'

LABEL_NONE = '---None---'

HEADERS = [
	   COLUMN_NAME, COLUMN_SYSTEM, COLUMN_YEAR, COLUMN_RATING, COLUMN_VOTES,
	   COLUMN_WEIGHTED, COLUMN_LENGTH, COLUMN_DIFFICULTY, COLUMN_STATUS,
	   COLUMN_LABELS, COLUMN_NOTES, COLUMN_URL
]
HEADERS_EXTENDED = HEADERS[:]
HEADERS_EXTENDED.append(COLUMN_ORDER)

ORDER_ASCENDING = 'ascending'
ORDER_DESCENDING = 'descending'

INITIAL_YEAR = 1940
FINAL_YEAR = 2100

FILTERED = 'filtered'
COUNT = 'count'

OPTIONS_STATUS = {
    'unplayed':  QtGui.QColor(155, 0, 0),
    'playing':   QtGui.QColor(0, 0, 155),
    'played':    QtGui.QColor(255, 155, 0),
    'completed': QtGui.QColor(0, 155, 0),
    'shelved':   QtGui.QColor(120, 155, 0)
}

DIFFICULTY_COLORS = {
    'Simple': QtGui.QColor(0, 0, 155),
    'Simple-Easy': QtGui.QColor(0, 0, 200), 
    'Easy': QtGui.QColor(0, 0, 255),
    'Easy-Just Right': QtGui.QColor(0, 255, 255), 
    'Just Right': QtGui.QColor(0, 155, 0),
    'Just Right-Tough': QtGui.QColor(179, 255, 0), 
    'Tough': QtGui.QColor(255, 155, 0),
    'Tough-Unforgiving': QtGui.QColor(255, 77, 0),
    'Unforgiving': QtGui.QColor(255, 0, 0),
    'Not Yet Rated': QtGui.QColor(155, 0, 0),
}
