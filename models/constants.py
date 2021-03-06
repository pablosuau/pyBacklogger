'''
Global constants for the application
'''
from PyQt5 import QtGui

RAWG_USERAGENT = 'pyBacklogger'
RAWG_URL = 'https://rawg.io/games/'

COLUMN_NAME = 'Name'
COLUMN_SYSTEM = 'System'
COLUMN_YEAR = 'Year'
COLUMN_RATING = 'Rating'
COLUMN_VOTES = 'Votes'
COLUMN_WEIGHTED = 'Weighted\nRating'
COLUMN_STATUS = 'Status'
COLUMN_LABELS = 'Labels'
COLUMN_NOTES = 'Notes'
COLUMN_ID = 'Id'
COLUMN_ORDER = 'Order'

LABEL_NONE = '---None---'

HEADERS = [
	   COLUMN_NAME, COLUMN_SYSTEM, COLUMN_YEAR, COLUMN_RATING, COLUMN_VOTES,
	   COLUMN_WEIGHTED, COLUMN_STATUS, COLUMN_LABELS, COLUMN_NOTES, COLUMN_ID
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
