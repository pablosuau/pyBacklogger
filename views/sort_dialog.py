# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sort_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SortDialog(object):
    def setupUi(self, SortDialog):
        SortDialog.setObjectName("SortDialog")
        SortDialog.resize(481, 343)
        SortDialog.setMinimumSize(QtCore.QSize(481, 343))
        SortDialog.setMaximumSize(QtCore.QSize(481, 343))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/app_icon/shelf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SortDialog.setWindowIcon(icon)
        self.listView = QtWidgets.QListView(SortDialog)
        self.listView.setGeometry(QtCore.QRect(100, 500, 256, 192))
        self.listView.setObjectName("listView")
        self.sortByList = QtWidgets.QListView(SortDialog)
        self.sortByList.setGeometry(QtCore.QRect(10, 40, 211, 261))
        self.sortByList.setObjectName("sortByList")
        self.availableFieldsList = QtWidgets.QListView(SortDialog)
        self.availableFieldsList.setGeometry(QtCore.QRect(260, 40, 211, 261))
        self.availableFieldsList.setObjectName("availableFieldsList")
        self.label = QtWidgets.QLabel(SortDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SortDialog)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 121, 16))
        self.label_2.setObjectName("label_2")
        self.pushButtonDown = QtWidgets.QPushButton(SortDialog)
        self.pushButtonDown.setEnabled(False)
        self.pushButtonDown.setGeometry(QtCore.QRect(170, 10, 21, 23))
        self.pushButtonDown.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/arrow_icons/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDown.setIcon(icon1)
        self.pushButtonDown.setObjectName("pushButtonDown")
        self.pushButtonUp = QtWidgets.QPushButton(SortDialog)
        self.pushButtonUp.setEnabled(False)
        self.pushButtonUp.setGeometry(QtCore.QRect(200, 10, 21, 23))
        self.pushButtonUp.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/arrow_icons/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonUp.setIcon(icon2)
        self.pushButtonUp.setObjectName("pushButtonUp")
        self.pushButtonLeft = QtWidgets.QPushButton(SortDialog)
        self.pushButtonLeft.setEnabled(False)
        self.pushButtonLeft.setGeometry(QtCore.QRect(230, 120, 21, 23))
        self.pushButtonLeft.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/arrow_icons/arrow_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLeft.setIcon(icon3)
        self.pushButtonLeft.setObjectName("pushButtonLeft")
        self.pushButtonRight = QtWidgets.QPushButton(SortDialog)
        self.pushButtonRight.setEnabled(False)
        self.pushButtonRight.setGeometry(QtCore.QRect(230, 150, 21, 23))
        self.pushButtonRight.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/arrow_icons/arrow_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRight.setIcon(icon4)
        self.pushButtonRight.setObjectName("pushButtonRight")
        self.pushButtonCancel = QtWidgets.QPushButton(SortDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(390, 310, 75, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.pushButtonOk = QtWidgets.QPushButton(SortDialog)
        self.pushButtonOk.setEnabled(True)
        self.pushButtonOk.setGeometry(QtCore.QRect(300, 310, 75, 23))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.pushButtonSort = QtWidgets.QPushButton(SortDialog)
        self.pushButtonSort.setEnabled(False)
        self.pushButtonSort.setGeometry(QtCore.QRect(140, 10, 21, 23))
        self.pushButtonSort.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/arrow_icons/sort.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSort.setIcon(icon5)
        self.pushButtonSort.setObjectName("pushButtonSort")

        self.retranslateUi(SortDialog)
        QtCore.QMetaObject.connectSlotsByName(SortDialog)

    def retranslateUi(self, SortDialog):
        _translate = QtCore.QCoreApplication.translate
        SortDialog.setWindowTitle(_translate("SortDialog", "Sort games"))
        self.label.setText(_translate("SortDialog", "Sort by:"))
        self.label_2.setText(_translate("SortDialog", "Available fields:"))
        self.pushButtonCancel.setText(_translate("SortDialog", "Cancel"))
        self.pushButtonOk.setText(_translate("SortDialog", "Ok"))

import views.app_icon_rc
import views.sort_dialog_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SortDialog = QtWidgets.QDialog()
    ui = Ui_SortDialog()
    ui.setupUi(SortDialog)
    SortDialog.show()
    sys.exit(app.exec_())

