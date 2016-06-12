from PyQt4 import QtGui

# Notification methods
def showErrorMessage(widget, message):
    errorMessage = QtGui.QErrorMessage(widget.parent())
    errorMessage.setWindowTitle(widget.windowTitle())
    errorMessage.showMessage(message)