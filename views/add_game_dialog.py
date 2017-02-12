# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_game_dialog.ui'
#
# Created: Sun Jan 29 08:57:08 2017
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

class Ui_AddGameDialog(object):
    def setupUi(self, AddGameDialog):
        AddGameDialog.setObjectName(_fromUtf8("AddGameDialog"))
        AddGameDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AddGameDialog.resize(249, 116)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddGameDialog.sizePolicy().hasHeightForWidth())
        AddGameDialog.setSizePolicy(sizePolicy)
        AddGameDialog.setMinimumSize(QtCore.QSize(249, 116))
        AddGameDialog.setMaximumSize(QtCore.QSize(249, 116))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/app_icon/shelf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddGameDialog.setWindowIcon(icon)
        AddGameDialog.setSizeGripEnabled(False)
        AddGameDialog.setModal(True)
        self.radioButtonUrl = QtGui.QRadioButton(AddGameDialog)
        self.radioButtonUrl.setGeometry(QtCore.QRect(10, 10, 101, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonUrl.sizePolicy().hasHeightForWidth())
        self.radioButtonUrl.setSizePolicy(sizePolicy)
        self.radioButtonUrl.setChecked(True)
        self.radioButtonUrl.setObjectName(_fromUtf8("radioButtonUrl"))
        self.radioButtonSearch = QtGui.QRadioButton(AddGameDialog)
        self.radioButtonSearch.setGeometry(QtCore.QRect(10, 30, 141, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonSearch.sizePolicy().hasHeightForWidth())
        self.radioButtonSearch.setSizePolicy(sizePolicy)
        self.radioButtonSearch.setObjectName(_fromUtf8("radioButtonSearch"))
        self.lineEditSearch = QtGui.QLineEdit(AddGameDialog)
        self.lineEditSearch.setEnabled(True)
        self.lineEditSearch.setGeometry(QtCore.QRect(10, 54, 231, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSearch.sizePolicy().hasHeightForWidth())
        self.lineEditSearch.setSizePolicy(sizePolicy)
        self.lineEditSearch.setObjectName(_fromUtf8("lineEditSearch"))
        self.pushButtonOk = QtGui.QPushButton(AddGameDialog)
        self.pushButtonOk.setEnabled(False)
        self.pushButtonOk.setGeometry(QtCore.QRect(80, 80, 75, 23))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.pushButtonCancel = QtGui.QPushButton(AddGameDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(160, 80, 75, 23))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))

        self.retranslateUi(AddGameDialog)
        QtCore.QMetaObject.connectSlotsByName(AddGameDialog)

    def retranslateUi(self, AddGameDialog):
        AddGameDialog.setWindowTitle(_translate("AddGameDialog", "Add game by", None))
        self.radioButtonUrl.setText(_translate("AddGameDialog", "GameFAQs\' url", None))
        self.radioButtonSearch.setText(_translate("AddGameDialog", "GameFAQs\' game search", None))
        self.pushButtonOk.setText(_translate("AddGameDialog", "Ok", None))
        self.pushButtonCancel.setText(_translate("AddGameDialog", "Cancel", None))

import app_icon_rc
