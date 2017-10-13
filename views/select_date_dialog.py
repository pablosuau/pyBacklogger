# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_date_dialog.ui'
#
# Created: Sun Jan 29 09:00:15 2017
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

class Ui_SelectDateDialog(object):
    def setupUi(self, SelectDateDialog):
        SelectDateDialog.setObjectName(_fromUtf8("SelectDateDialog"))
        SelectDateDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        SelectDateDialog.resize(176, 149)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SelectDateDialog.sizePolicy().hasHeightForWidth())
        SelectDateDialog.setSizePolicy(sizePolicy)
        SelectDateDialog.setMinimumSize(QtCore.QSize(176, 149))
        SelectDateDialog.setMaximumSize(QtCore.QSize(176, 149))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/app_icon/shelf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SelectDateDialog.setWindowIcon(icon)
        self.radioButtonCanceled = QtWidgets.QRadioButton(SelectDateDialog)
        self.radioButtonCanceled.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButtonCanceled.setObjectName(_fromUtf8("radioButtonCanceled"))
        self.radioButtonTba = QtWidgets.QRadioButton(SelectDateDialog)
        self.radioButtonTba.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButtonTba.setObjectName(_fromUtf8("radioButtonTba"))
        self.radioButtonYear = QtWidgets.QRadioButton(SelectDateDialog)
        self.radioButtonYear.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButtonYear.setObjectName(_fromUtf8("radioButtonYear"))
        self.pushButtonOk = QtWidgets.QPushButton(SelectDateDialog)
        self.pushButtonOk.setGeometry(QtCore.QRect(10, 110, 75, 23))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.pushButtonCancel = QtWidgets.QPushButton(SelectDateDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(90, 110, 75, 23))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.sliderYear = QtWidgets.QSlider(SelectDateDialog)
        self.sliderYear.setGeometry(QtCore.QRect(10, 80, 151, 22))
        self.sliderYear.setOrientation(QtCore.Qt.Horizontal)
        self.sliderYear.setObjectName(_fromUtf8("sliderYear"))
        self.lineEditYear = QtWidgets.QLineEdit(SelectDateDialog)
        self.lineEditYear.setGeometry(QtCore.QRect(60, 50, 51, 20))
        self.lineEditYear.setText(_fromUtf8(""))
        self.lineEditYear.setMaxLength(8)
        self.lineEditYear.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditYear.setObjectName(_fromUtf8("lineEditYear"))

        self.retranslateUi(SelectDateDialog)
        QtCore.QMetaObject.connectSlotsByName(SelectDateDialog)

    def retranslateUi(self, SelectDateDialog):
        SelectDateDialog.setWindowTitle(_translate("SelectDateDialog", "Date", None))
        self.radioButtonCanceled.setText(_translate("SelectDateDialog", "Canceled", None))
        self.radioButtonTba.setText(_translate("SelectDateDialog", "TBA", None))
        self.radioButtonYear.setText(_translate("SelectDateDialog", "Year:", None))
        self.pushButtonOk.setText(_translate("SelectDateDialog", "Ok", None))
        self.pushButtonCancel.setText(_translate("SelectDateDialog", "Cancel", None))

import app_icon_rc
