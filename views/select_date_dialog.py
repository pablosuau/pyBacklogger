# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_date_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelectDateDialog(object):
    def setupUi(self, SelectDateDialog):
        SelectDateDialog.setObjectName("SelectDateDialog")
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
        icon.addPixmap(QtGui.QPixmap(":/app_icon/shelf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SelectDateDialog.setWindowIcon(icon)
        self.radioButtonCanceled = QtWidgets.QRadioButton(SelectDateDialog)
        self.radioButtonCanceled.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButtonCanceled.setObjectName("radioButtonCanceled")
        self.radioButtonTba = QtWidgets.QRadioButton(SelectDateDialog)
        self.radioButtonTba.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButtonTba.setObjectName("radioButtonTba")
        self.radioButtonYear = QtWidgets.QRadioButton(SelectDateDialog)
        self.radioButtonYear.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButtonYear.setObjectName("radioButtonYear")
        self.pushButtonOk = QtWidgets.QPushButton(SelectDateDialog)
        self.pushButtonOk.setGeometry(QtCore.QRect(10, 110, 75, 23))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.pushButtonCancel = QtWidgets.QPushButton(SelectDateDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(90, 110, 75, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.sliderYear = QtWidgets.QSlider(SelectDateDialog)
        self.sliderYear.setGeometry(QtCore.QRect(10, 80, 151, 22))
        self.sliderYear.setOrientation(QtCore.Qt.Horizontal)
        self.sliderYear.setObjectName("sliderYear")
        self.lineEditYear = QtWidgets.QLineEdit(SelectDateDialog)
        self.lineEditYear.setGeometry(QtCore.QRect(60, 50, 51, 20))
        self.lineEditYear.setText("")
        self.lineEditYear.setMaxLength(8)
        self.lineEditYear.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditYear.setObjectName("lineEditYear")

        self.retranslateUi(SelectDateDialog)
        QtCore.QMetaObject.connectSlotsByName(SelectDateDialog)

    def retranslateUi(self, SelectDateDialog):
        _translate = QtCore.QCoreApplication.translate
        SelectDateDialog.setWindowTitle(_translate("SelectDateDialog", "Date"))
        self.radioButtonCanceled.setText(_translate("SelectDateDialog", "Canceled"))
        self.radioButtonTba.setText(_translate("SelectDateDialog", "TBA"))
        self.radioButtonYear.setText(_translate("SelectDateDialog", "Year:"))
        self.pushButtonOk.setText(_translate("SelectDateDialog", "Ok"))
        self.pushButtonCancel.setText(_translate("SelectDateDialog", "Cancel"))

import views.app_icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SelectDateDialog = QtWidgets.QDialog()
    ui = Ui_SelectDateDialog()
    ui.setupUi(SelectDateDialog)
    SelectDateDialog.show()
    sys.exit(app.exec_())

