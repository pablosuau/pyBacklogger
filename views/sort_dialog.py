# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sort_dialog.ui'
#
# Created: Sun Jan 29 09:01:20 2017
#      by: PyQt5 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_SortDialog(object):
    def setupUi(self, SortDialog):
        SortDialog.setObjectName(_fromUtf8("SortDialog"))
        SortDialog.resize(481, 343)
        SortDialog.setMinimumSize(QtCore.QSize(481, 343))
        SortDialog.setMaximumSize(QtCore.QSize(481, 343))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/app_icon/shelf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SortDialog.setWindowIcon(icon)
        self.listView = QtWidgets.QListView(SortDialog)
        self.listView.setGeometry(QtCore.QRect(100, 500, 256, 192))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.sortByList = QtWidgets.QListView(SortDialog)
        self.sortByList.setGeometry(QtCore.QRect(10, 40, 211, 261))
        self.sortByList.setObjectName(_fromUtf8("sortByList"))
        self.availableFieldsList = QtWidgets.QListView(SortDialog)
        self.availableFieldsList.setGeometry(QtCore.QRect(260, 40, 211, 261))
        self.availableFieldsList.setObjectName(_fromUtf8("availableFieldsList"))
        self.label = QtWidgets.QLabel(SortDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(SortDialog)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButtonDown = QtWidgets.QPushButton(SortDialog)
        self.pushButtonDown.setEnabled(False)
        self.pushButtonDown.setGeometry(QtCore.QRect(170, 10, 21, 23))
        self.pushButtonDown.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow_icons/arrow_down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDown.setIcon(icon1)
        self.pushButtonDown.setObjectName(_fromUtf8("pushButtonDown"))
        self.pushButtonUp = QtWidgets.QPushButton(SortDialog)
        self.pushButtonUp.setEnabled(False)
        self.pushButtonUp.setGeometry(QtCore.QRect(200, 10, 21, 23))
        self.pushButtonUp.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow_icons/arrow_up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonUp.setIcon(icon2)
        self.pushButtonUp.setObjectName(_fromUtf8("pushButtonUp"))
        self.pushButtonLeft = QtWidgets.QPushButton(SortDialog)
        self.pushButtonLeft.setEnabled(False)
        self.pushButtonLeft.setGeometry(QtCore.QRect(230, 120, 21, 23))
        self.pushButtonLeft.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow_icons/arrow_left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLeft.setIcon(icon3)
        self.pushButtonLeft.setObjectName(_fromUtf8("pushButtonLeft"))
        self.pushButtonRight = QtWidgets.QPushButton(SortDialog)
        self.pushButtonRight.setEnabled(False)
        self.pushButtonRight.setGeometry(QtCore.QRect(230, 150, 21, 23))
        self.pushButtonRight.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow_icons/arrow_right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRight.setIcon(icon4)
        self.pushButtonRight.setObjectName(_fromUtf8("pushButtonRight"))
        self.pushButtonCancel = QtWidgets.QPushButton(SortDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(390, 310, 75, 23))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.pushButtonOk = QtWidgets.QPushButton(SortDialog)
        self.pushButtonOk.setEnabled(True)
        self.pushButtonOk.setGeometry(QtCore.QRect(300, 310, 75, 23))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.pushButtonSort = QtWidgets.QPushButton(SortDialog)
        self.pushButtonSort.setEnabled(False)
        self.pushButtonSort.setGeometry(QtCore.QRect(140, 10, 21, 23))
        self.pushButtonSort.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow_icons/sort.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSort.setIcon(icon5)
        self.pushButtonSort.setObjectName(_fromUtf8("pushButtonSort"))

        self.retranslateUi(SortDialog)
        QtCore.QMetaObject.connectSlotsByName(SortDialog)

    def retranslateUi(self, SortDialog):
        SortDialog.setWindowTitle(_translate("SortDialog", "Sort games", None))
        self.label.setText(_translate("SortDialog", "Sort by:", None))
        self.label_2.setText(_translate("SortDialog", "Available fields:", None))
        self.pushButtonCancel.setText(_translate("SortDialog", "Cancel", None))
        self.pushButtonOk.setText(_translate("SortDialog", "Ok", None))

import sort_dialog_rc
import app_icon_rc
