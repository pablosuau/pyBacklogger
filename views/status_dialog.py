# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'status_dialog.ui'
#
# Created: Sun Jan 29 08:58:27 2017
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

class Ui_StatusDialog(object):
    def setupUi(self, StatusDialog):
        StatusDialog.setObjectName(_fromUtf8("StatusDialog"))
        StatusDialog.resize(172, 72)
        StatusDialog.setMinimumSize(QtCore.QSize(172, 72))
        StatusDialog.setMaximumSize(QtCore.QSize(172, 72))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/app_icon/shelf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StatusDialog.setWindowIcon(icon)
        self.pushButtonOk = QtGui.QPushButton(StatusDialog)
        self.pushButtonOk.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.pushButtonCancel = QtGui.QPushButton(StatusDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(90, 40, 75, 23))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.comboBoxStatus = QtGui.QComboBox(StatusDialog)
        self.comboBoxStatus.setGeometry(QtCore.QRect(10, 10, 151, 22))
        self.comboBoxStatus.setObjectName(_fromUtf8("comboBoxStatus"))

        self.retranslateUi(StatusDialog)
        QtCore.QMetaObject.connectSlotsByName(StatusDialog)

    def retranslateUi(self, StatusDialog):
        StatusDialog.setWindowTitle(_translate("StatusDialog", "Status", None))
        self.pushButtonOk.setText(_translate("StatusDialog", "Ok", None))
        self.pushButtonCancel.setText(_translate("StatusDialog", "Cancel", None))

import app_icon_rc
