from PyQt5 import QtGui, QtCore, QtWidgets

# Notification methods
def showErrorMessage(widget, message):
    errorMessage = QtWidgets.QErrorMessage(widget)
    errorMessage.setWindowModality(QtCore.Qt.WindowModal)
    errorMessage.setWindowTitle(widget.windowTitle())
    errorMessage.showMessage(message)
