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
