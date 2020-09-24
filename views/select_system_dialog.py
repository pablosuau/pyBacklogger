# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_system_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelectSystemDialog(object):
    def setupUi(self, SelectSystemDialog):
        SelectSystemDialog.setObjectName("SelectSystemDialog")
        SelectSystemDialog.resize(270, 286)
        SelectSystemDialog.setMinimumSize(QtCore.QSize(270, 286))
        SelectSystemDialog.setMaximumSize(QtCore.QSize(270, 286))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/app_icon/shelf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SelectSystemDialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(SelectSystemDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 16))
        self.label.setObjectName("label")
        self.listViewSystems = QtWidgets.QListView(SelectSystemDialog)
        self.listViewSystems.setGeometry(QtCore.QRect(10, 30, 251, 221))
        self.listViewSystems.setObjectName("listViewSystems")
        self.pushButtonOk = QtWidgets.QPushButton(SelectSystemDialog)
        self.pushButtonOk.setEnabled(True)
        self.pushButtonOk.setGeometry(QtCore.QRect(95, 257, 75, 23))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.pushButtonCancel = QtWidgets.QPushButton(SelectSystemDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(185, 257, 75, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")

        self.retranslateUi(SelectSystemDialog)
        QtCore.QMetaObject.connectSlotsByName(SelectSystemDialog)

    def retranslateUi(self, SelectSystemDialog):
        _translate = QtCore.QCoreApplication.translate
        SelectSystemDialog.setWindowTitle(_translate("SelectSystemDialog", "System selection"))
        self.label.setText(_translate("SelectSystemDialog", "Select the system:"))
        self.pushButtonOk.setText(_translate("SelectSystemDialog", "Ok"))
        self.pushButtonCancel.setText(_translate("SelectSystemDialog", "Cancel"))
import views.app_icon_rc
