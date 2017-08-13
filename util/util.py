from PyQt4 import QtGui, QtCore

# Notification methods
def showErrorMessage(widget, message):
    errorMessage = QtGui.QErrorMessage(widget)
    errorMessage.setWindowModality(QtCore.Qt.WindowModal)
    errorMessage.setWindowTitle(widget.windowTitle())
    errorMessage.showMessage(message)