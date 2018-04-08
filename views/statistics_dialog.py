# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatisticsWindow(object):
    def setupUi(self, StatisticsWindow):
        StatisticsWindow.setObjectName("StatisticsWindow")
        StatisticsWindow.resize(512, 447)
        self.horizontalLayoutWidget = QtWidgets.QWidget(StatisticsWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 0, 491, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonSystem = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonSystem.setObjectName("pushButtonSystem")
        self.horizontalLayout.addWidget(self.pushButtonSystem)
        self.pushButtonYear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonYear.setObjectName("pushButtonYear")
        self.horizontalLayout.addWidget(self.pushButtonYear)
        self.pushButtonLabel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonLabel.setObjectName("pushButtonLabel")
        self.horizontalLayout.addWidget(self.pushButtonLabel)
        self.pushButtonStatus = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonStatus.setObjectName("pushButtonStatus")
        self.horizontalLayout.addWidget(self.pushButtonStatus)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(StatisticsWindow)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 30, 491, 381))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(StatisticsWindow)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 410, 491, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonClose = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.horizontalLayout_2.addWidget(self.pushButtonClose)

        self.retranslateUi(StatisticsWindow)
        QtCore.QMetaObject.connectSlotsByName(StatisticsWindow)

    def retranslateUi(self, StatisticsWindow):
        _translate = QtCore.QCoreApplication.translate
        StatisticsWindow.setWindowTitle(_translate("StatisticsWindow", "Dialog"))
        self.pushButtonSystem.setText(_translate("StatisticsWindow", "System"))
        self.pushButtonYear.setText(_translate("StatisticsWindow", "Year"))
        self.pushButtonLabel.setText(_translate("StatisticsWindow", "Label"))
        self.pushButtonStatus.setText(_translate("StatisticsWindow", "Status"))
        self.pushButtonClose.setText(_translate("StatisticsWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StatisticsWindow = QtWidgets.QDialog()
    ui = Ui_StatisticsWindow()
    ui.setupUi(StatisticsWindow)
    StatisticsWindow.show()
    sys.exit(app.exec_())

