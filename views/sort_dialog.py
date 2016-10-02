# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sort_dialog.ui'
#
# Created: Sun Oct 02 08:28:30 2016
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

class Ui_SortDialog(object):
    def setupUi(self, SortDialog):
        SortDialog.setObjectName(_fromUtf8("SortDialog"))
        SortDialog.resize(481, 343)
        SortDialog.setMinimumSize(QtCore.QSize(481, 343))
        SortDialog.setMaximumSize(QtCore.QSize(481, 343))
        self.listView = QtGui.QListView(SortDialog)
        self.listView.setGeometry(QtCore.QRect(100, 500, 256, 192))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.sortByList = QtGui.QListView(SortDialog)
        self.sortByList.setGeometry(QtCore.QRect(10, 40, 211, 261))
        self.sortByList.setObjectName(_fromUtf8("sortByList"))
        self.availableFieldsList = QtGui.QListView(SortDialog)
        self.availableFieldsList.setGeometry(QtCore.QRect(260, 40, 211, 261))
        self.availableFieldsList.setObjectName(_fromUtf8("availableFieldsList"))
        self.label = QtGui.QLabel(SortDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(SortDialog)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButtonDown = QtGui.QPushButton(SortDialog)
        self.pushButtonDown.setEnabled(False)
        self.pushButtonDown.setGeometry(QtCore.QRect(170, 10, 21, 23))
        self.pushButtonDown.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow_icons/arrow_down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDown.setIcon(icon)
        self.pushButtonDown.setObjectName(_fromUtf8("pushButtonDown"))
        self.pushButtonUp = QtGui.QPushButton(SortDialog)
        self.pushButtonUp.setEnabled(False)
        self.pushButtonUp.setGeometry(QtCore.QRect(200, 10, 21, 23))
        self.pushButtonUp.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow_icons/arrow_up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonUp.setIcon(icon1)
        self.pushButtonUp.setObjectName(_fromUtf8("pushButtonUp"))
        self.pushButtonLeft = QtGui.QPushButton(SortDialog)
        self.pushButtonLeft.setEnabled(False)
        self.pushButtonLeft.setGeometry(QtCore.QRect(230, 120, 21, 23))
        self.pushButtonLeft.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow_icons/arrow_left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLeft.setIcon(icon2)
        self.pushButtonLeft.setObjectName(_fromUtf8("pushButtonLeft"))
        self.pushButtonRight = QtGui.QPushButton(SortDialog)
        self.pushButtonRight.setEnabled(False)
        self.pushButtonRight.setGeometry(QtCore.QRect(230, 150, 21, 23))
        self.pushButtonRight.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow_icons/arrow_right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRight.setIcon(icon3)
        self.pushButtonRight.setObjectName(_fromUtf8("pushButtonRight"))
        self.pushButtonCancel = QtGui.QPushButton(SortDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(390, 310, 75, 23))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.pushButtonOk = QtGui.QPushButton(SortDialog)
        self.pushButtonOk.setEnabled(True)
        self.pushButtonOk.setGeometry(QtCore.QRect(300, 310, 75, 23))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))

        self.retranslateUi(SortDialog)
        QtCore.QMetaObject.connectSlotsByName(SortDialog)

    def retranslateUi(self, SortDialog):
        SortDialog.setWindowTitle(_translate("SortDialog", "Sort games", None))
        self.label.setText(_translate("SortDialog", "Sort by:", None))
        self.label_2.setText(_translate("SortDialog", "Available fields:", None))
        self.pushButtonCancel.setText(_translate("SortDialog", "Cancel", None))
        self.pushButtonOk.setText(_translate("SortDialog", "Ok", None))

import sort_dialog_rc
