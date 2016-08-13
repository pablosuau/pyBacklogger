# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'status_dialog.ui'
#
# Created: Sat Aug 13 09:13:30 2016
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(172, 72)
        Dialog.setMinimumSize(QtCore.QSize(172, 72))
        Dialog.setMaximumSize(QtCore.QSize(172, 72))
        self.pushButtonOk = QtGui.QPushButton(Dialog)
        self.pushButtonOk.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.pushButtonCancel = QtGui.QPushButton(Dialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(90, 40, 75, 23))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.comboBoxStatus = QtGui.QComboBox(Dialog)
        self.comboBoxStatus.setGeometry(QtCore.QRect(10, 10, 151, 22))
        self.comboBoxStatus.setObjectName(_fromUtf8("comboBoxStatus"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Status", None))
        self.pushButtonOk.setText(_translate("Dialog", "Ok", None))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel", None))

