# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_date_dialog.ui'
#
# Created: Sun Jun 12 15:48:03 2016
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

class Ui_SelectDateDialog(object):
    def setupUi(self, SelectDateDialog):
        SelectDateDialog.setObjectName(_fromUtf8("SelectDateDialog"))
        SelectDateDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        SelectDateDialog.resize(176, 149)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SelectDateDialog.sizePolicy().hasHeightForWidth())
        SelectDateDialog.setSizePolicy(sizePolicy)
        SelectDateDialog.setMinimumSize(QtCore.QSize(176, 149))
        SelectDateDialog.setMaximumSize(QtCore.QSize(176, 149))
        self.radioButtonCanceled = QtGui.QRadioButton(SelectDateDialog)
        self.radioButtonCanceled.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButtonCanceled.setObjectName(_fromUtf8("radioButtonCanceled"))
        self.radioButtonTba = QtGui.QRadioButton(SelectDateDialog)
        self.radioButtonTba.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButtonTba.setObjectName(_fromUtf8("radioButtonTba"))
        self.radioButtonYear = QtGui.QRadioButton(SelectDateDialog)
        self.radioButtonYear.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButtonYear.setObjectName(_fromUtf8("radioButtonYear"))
        self.pushButtonOk = QtGui.QPushButton(SelectDateDialog)
        self.pushButtonOk.setGeometry(QtCore.QRect(10, 110, 75, 23))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.pushButtonCancel = QtGui.QPushButton(SelectDateDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(90, 110, 75, 23))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.sliderYear = QtGui.QSlider(SelectDateDialog)
        self.sliderYear.setGeometry(QtCore.QRect(10, 80, 151, 22))
        self.sliderYear.setOrientation(QtCore.Qt.Horizontal)
        self.sliderYear.setObjectName(_fromUtf8("sliderYear"))
        self.lineEditYear = QtGui.QLineEdit(SelectDateDialog)
        self.lineEditYear.setGeometry(QtCore.QRect(60, 50, 41, 20))
        self.lineEditYear.setText(_fromUtf8(""))
        self.lineEditYear.setMaxLength(4)
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

