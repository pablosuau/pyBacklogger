# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics_dialog.ui'
#
# Created: Sun Apr 30 10:58:13 2017
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

class Ui_StatisticsWindow(object):
    def setupUi(self, StatisticsWindow):
        StatisticsWindow.setObjectName(_fromUtf8("StatisticsWindow"))
        StatisticsWindow.resize(512, 447)
        self.horizontalLayoutWidget = QtWidgets.QWidget(StatisticsWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 0, 491, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonSystem = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonSystem.setObjectName(_fromUtf8("pushButtonSystem"))
        self.horizontalLayout.addWidget(self.pushButtonSystem)
        self.pushButtonYear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonYear.setObjectName(_fromUtf8("pushButtonYear"))
        self.horizontalLayout.addWidget(self.pushButtonYear)
        self.pushButtonLabel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonLabel.setObjectName(_fromUtf8("pushButtonLabel"))
        self.horizontalLayout.addWidget(self.pushButtonLabel)
        self.pushButtonStatus = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonStatus.setObjectName(_fromUtf8("pushButtonStatus"))
        self.horizontalLayout.addWidget(self.pushButtonStatus)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(StatisticsWindow)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 30, 491, 381))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(StatisticsWindow)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 410, 491, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButtonClose = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonClose.setObjectName(_fromUtf8("pushButtonClose"))
        self.horizontalLayout_2.addWidget(self.pushButtonClose)

        self.retranslateUi(StatisticsWindow)
        QtCore.QMetaObject.connectSlotsByName(StatisticsWindow)

    def retranslateUi(self, StatisticsWindow):
        StatisticsWindow.setWindowTitle(_translate("StatisticsWindow", "Dialog", None))
        self.pushButtonSystem.setText(_translate("StatisticsWindow", "System", None))
        self.pushButtonYear.setText(_translate("StatisticsWindow", "Year", None))
        self.pushButtonLabel.setText(_translate("StatisticsWindow", "Label", None))
        self.pushButtonStatus.setText(_translate("StatisticsWindow", "Status", None))
        self.pushButtonClose.setText(_translate("StatisticsWindow", "Close", None))

