# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_game_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddGameDialog(object):
    def setupUi(self, AddGameDialog):
        AddGameDialog.setObjectName("AddGameDialog")
        AddGameDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AddGameDialog.resize(249, 116)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddGameDialog.sizePolicy().hasHeightForWidth())
        AddGameDialog.setSizePolicy(sizePolicy)
        AddGameDialog.setMinimumSize(QtCore.QSize(249, 116))
        AddGameDialog.setMaximumSize(QtCore.QSize(249, 116))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/app_icon/shelf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddGameDialog.setWindowIcon(icon)
        AddGameDialog.setSizeGripEnabled(False)
        AddGameDialog.setModal(True)
        self.radioButtonUrl = QtWidgets.QRadioButton(AddGameDialog)
        self.radioButtonUrl.setGeometry(QtCore.QRect(10, 10, 101, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonUrl.sizePolicy().hasHeightForWidth())
        self.radioButtonUrl.setSizePolicy(sizePolicy)
        self.radioButtonUrl.setChecked(True)
        self.radioButtonUrl.setObjectName("radioButtonUrl")
        self.radioButtonSearch = QtWidgets.QRadioButton(AddGameDialog)
        self.radioButtonSearch.setGeometry(QtCore.QRect(10, 30, 141, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonSearch.sizePolicy().hasHeightForWidth())
        self.radioButtonSearch.setSizePolicy(sizePolicy)
        self.radioButtonSearch.setObjectName("radioButtonSearch")
        self.lineEditSearch = QtWidgets.QLineEdit(AddGameDialog)
        self.lineEditSearch.setEnabled(True)
        self.lineEditSearch.setGeometry(QtCore.QRect(10, 54, 231, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSearch.sizePolicy().hasHeightForWidth())
        self.lineEditSearch.setSizePolicy(sizePolicy)
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.pushButtonOk = QtWidgets.QPushButton(AddGameDialog)
        self.pushButtonOk.setEnabled(False)
        self.pushButtonOk.setGeometry(QtCore.QRect(80, 80, 75, 23))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.pushButtonCancel = QtWidgets.QPushButton(AddGameDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(160, 80, 75, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")

        self.retranslateUi(AddGameDialog)
        QtCore.QMetaObject.connectSlotsByName(AddGameDialog)

    def retranslateUi(self, AddGameDialog):
        _translate = QtCore.QCoreApplication.translate
        AddGameDialog.setWindowTitle(_translate("AddGameDialog", "Add game by"))
        self.radioButtonUrl.setText(_translate("AddGameDialog", "GameFAQs\' url"))
        self.radioButtonSearch.setText(_translate("AddGameDialog", "GameFAQs\' game search"))
        self.pushButtonOk.setText(_translate("AddGameDialog", "Ok"))
        self.pushButtonCancel.setText(_translate("AddGameDialog", "Cancel"))

import views.app_icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddGameDialog = QtWidgets.QDialog()
    ui = Ui_AddGameDialog()
    ui.setupUi(AddGameDialog)
    AddGameDialog.show()
    sys.exit(app.exec_())

