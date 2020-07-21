'''
Module for generic utility methods
'''
from PyQt5 import QtCore, QtWidgets

def show_error_message(widget, message):
    '''
    Displays a dialog with an error message.

    parameters:
        - message: the error message to be displayed
    '''
    error_message = QtWidgets.QErrorMessage(widget)
    error_message.setWindowModality(QtCore.Qt.WindowModal)
    error_message.setWindowTitle(widget.windowTitle())
    error_message.showMessage(message)

def parse_difficulty_length(doc, id_element):
    '''
    Auxiliar function to parse both difficulty and length, since the parsing process
    is very similar and is used at several points in the code
    '''
    element = doc.xpath("//div[@id='" + id_element + "']")
    value = element[0].text
    if value != 'Unrated':
        ret = value.split('(')[0].rstrip()
    else:
        ret = 'Not Yet Rated'
    return ret
