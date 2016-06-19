from PyQt4 import QtGui

# Notification methods
def showErrorMessage(widget, message):
    errorMessage = QtGui.QErrorMessage(widget)
    errorMessage.setWindowTitle(widget.windowTitle())
    errorMessage.showMessage(message)