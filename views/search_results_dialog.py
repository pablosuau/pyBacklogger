# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_results_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchResultsDialog(object):
    def setupUi(self, SearchResultsDialog):
        SearchResultsDialog.setObjectName("SearchResultsDialog")
        SearchResultsDialog.resize(270, 286)
        SearchResultsDialog.setMinimumSize(QtCore.QSize(270, 286))
        SearchResultsDialog.setMaximumSize(QtCore.QSize(270, 286))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/app_icon/shelf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SearchResultsDialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(SearchResultsDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 16))
        self.label.setObjectName("label")
        self.listViewGames = QtWidgets.QListView(SearchResultsDialog)
        self.listViewGames.setGeometry(QtCore.QRect(10, 30, 251, 221))
        self.listViewGames.setObjectName("listViewGames")
        self.pushButtonOk = QtWidgets.QPushButton(SearchResultsDialog)
        self.pushButtonOk.setEnabled(True)
        self.pushButtonOk.setGeometry(QtCore.QRect(95, 257, 75, 23))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.pushButtonCancel = QtWidgets.QPushButton(SearchResultsDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(185, 257, 75, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")

        self.retranslateUi(SearchResultsDialog)
        QtCore.QMetaObject.connectSlotsByName(SearchResultsDialog)

    def retranslateUi(self, SearchResultsDialog):
        _translate = QtCore.QCoreApplication.translate
        SearchResultsDialog.setWindowTitle(_translate("SearchResultsDialog", "Search results"))
        self.label.setText(_translate("SearchResultsDialog", "Select the game or games to add to your backlog"))
        self.pushButtonOk.setText(_translate("SearchResultsDialog", "Ok"))
        self.pushButtonCancel.setText(_translate("SearchResultsDialog", "Cancel"))

import views.app_icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchResultsDialog = QtWidgets.QDialog()
    ui = Ui_SearchResultsDialog()
    ui.setupUi(SearchResultsDialog)
    SearchResultsDialog.show()
    sys.exit(app.exec_())

