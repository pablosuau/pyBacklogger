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

    element = doc.xpath("//fieldset[@id='" + id_element + "']")
    if element:
        try:
            value = element[0] \
                    .getchildren()[0] \
                    .getchildren()[0] \
                    .getchildren()[2] \
                    .findtext('a')
            if value is None:
                ret = 'Not Yet Rated'
            else:
                ret = value
                if id_element == 'js_mygames_time':
                    ret = ret.split(' ')[0]
        except IndexError:
            # Not rated yet, therefore, length of the div is 2, not three
            ret = 'Not Yet Rated'
    else:
        ret = 'Not Yet Rated'
    return ret
