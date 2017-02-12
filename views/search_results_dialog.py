# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_results_dialog.ui'
#
# Created: Sun Jan 29 09:00:52 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SearchResultsDialog(object):
    def setupUi(self, SearchResultsDialog):
        SearchResultsDialog.setObjectName(_fromUtf8("SearchResultsDialog"))
        SearchResultsDialog.resize(270, 286)
        SearchResultsDialog.setMinimumSize(QtCore.QSize(270, 286))
        SearchResultsDialog.setMaximumSize(QtCore.QSize(270, 286))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/app_icon/shelf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SearchResultsDialog.setWindowIcon(icon)
        self.label = QtGui.QLabel(SearchResultsDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.listViewGames = QtGui.QListView(SearchResultsDialog)
        self.listViewGames.setGeometry(QtCore.QRect(10, 30, 251, 221))
        self.listViewGames.setObjectName(_fromUtf8("listViewGames"))
        self.pushButtonOk = QtGui.QPushButton(SearchResultsDialog)
        self.pushButtonOk.setEnabled(True)
        self.pushButtonOk.setGeometry(QtCore.QRect(95, 257, 75, 23))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.pushButtonCancel = QtGui.QPushButton(SearchResultsDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(185, 257, 75, 23))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))

        self.retranslateUi(SearchResultsDialog)
        QtCore.QMetaObject.connectSlotsByName(SearchResultsDialog)

    def retranslateUi(self, SearchResultsDialog):
        SearchResultsDialog.setWindowTitle(_translate("SearchResultsDialog", "Search results", None))
        self.label.setText(_translate("SearchResultsDialog", "Select the game or games to add to your backlog", None))
        self.pushButtonOk.setText(_translate("SearchResultsDialog", "Ok", None))
        self.pushButtonCancel.setText(_translate("SearchResultsDialog", "Cancel", None))

import app_icon_rc
