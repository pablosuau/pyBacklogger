# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'status_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatusDialog(object):
    def setupUi(self, StatusDialog):
        StatusDialog.setObjectName("StatusDialog")
        StatusDialog.resize(172, 72)
        StatusDialog.setMinimumSize(QtCore.QSize(172, 72))
        StatusDialog.setMaximumSize(QtCore.QSize(172, 72))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/app_icon/shelf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StatusDialog.setWindowIcon(icon)
        self.pushButtonOk = QtWidgets.QPushButton(StatusDialog)
        self.pushButtonOk.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.pushButtonCancel = QtWidgets.QPushButton(StatusDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(90, 40, 75, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.comboBoxStatus = QtWidgets.QComboBox(StatusDialog)
        self.comboBoxStatus.setGeometry(QtCore.QRect(10, 10, 151, 22))
        self.comboBoxStatus.setObjectName("comboBoxStatus")

        self.retranslateUi(StatusDialog)
        QtCore.QMetaObject.connectSlotsByName(StatusDialog)

    def retranslateUi(self, StatusDialog):
        _translate = QtCore.QCoreApplication.translate
        StatusDialog.setWindowTitle(_translate("StatusDialog", "Status"))
        self.pushButtonOk.setText(_translate("StatusDialog", "Ok"))
        self.pushButtonCancel.setText(_translate("StatusDialog", "Cancel"))

import views.app_icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StatusDialog = QtWidgets.QDialog()
    ui = Ui_StatusDialog()
    ui.setupUi(StatusDialog)
    StatusDialog.show()
    sys.exit(app.exec_())

