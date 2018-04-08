# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilterDialog(object):
    def setupUi(self, FilterDialog):
        FilterDialog.setObjectName("FilterDialog")
        FilterDialog.resize(255, 368)
        FilterDialog.setMinimumSize(QtCore.QSize(255, 368))
        FilterDialog.setMaximumSize(QtCore.QSize(255, 368))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/app_icon/shelf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FilterDialog.setWindowIcon(icon)
        self.tabCategory = QtWidgets.QTabWidget(FilterDialog)
        self.tabCategory.setGeometry(QtCore.QRect(0, 0, 401, 321))
        self.tabCategory.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabCategory.setObjectName("tabCategory")
        self.tabSystem = QtWidgets.QWidget()
        self.tabSystem.setObjectName("tabSystem")
        self.pushButtonDeselectAllSystem = QtWidgets.QPushButton(self.tabSystem)
        self.pushButtonDeselectAllSystem.setGeometry(QtCore.QRect(90, 7, 75, 23))
        self.pushButtonDeselectAllSystem.setObjectName("pushButtonDeselectAllSystem")
        self.pushButtonSelectAllSystem = QtWidgets.QPushButton(self.tabSystem)
        self.pushButtonSelectAllSystem.setGeometry(QtCore.QRect(10, 7, 75, 23))
        self.pushButtonSelectAllSystem.setObjectName("pushButtonSelectAllSystem")
        self.listSystem = QtWidgets.QListView(self.tabSystem)
        self.listSystem.setGeometry(QtCore.QRect(10, 40, 231, 241))
        self.listSystem.setObjectName("listSystem")
        self.tabCategory.addTab(self.tabSystem, "")
        self.tabStatus = QtWidgets.QWidget()
        self.tabStatus.setObjectName("tabStatus")
        self.pushButtonDeselectAllStatus = QtWidgets.QPushButton(self.tabStatus)
        self.pushButtonDeselectAllStatus.setGeometry(QtCore.QRect(90, 7, 75, 23))
        self.pushButtonDeselectAllStatus.setObjectName("pushButtonDeselectAllStatus")
        self.pushButtonSelectAllStatus = QtWidgets.QPushButton(self.tabStatus)
        self.pushButtonSelectAllStatus.setGeometry(QtCore.QRect(10, 7, 75, 23))
        self.pushButtonSelectAllStatus.setObjectName("pushButtonSelectAllStatus")
        self.listStatus = QtWidgets.QListView(self.tabStatus)
        self.listStatus.setGeometry(QtCore.QRect(10, 40, 231, 241))
        self.listStatus.setObjectName("listStatus")
        self.tabCategory.addTab(self.tabStatus, "")
        self.tabLabel = QtWidgets.QWidget()
        self.tabLabel.setObjectName("tabLabel")
        self.pushButtonDeselectAllLabel = QtWidgets.QPushButton(self.tabLabel)
        self.pushButtonDeselectAllLabel.setGeometry(QtCore.QRect(90, 7, 75, 23))
        self.pushButtonDeselectAllLabel.setObjectName("pushButtonDeselectAllLabel")
        self.pushButtonSelectAllLabel = QtWidgets.QPushButton(self.tabLabel)
        self.pushButtonSelectAllLabel.setGeometry(QtCore.QRect(10, 7, 75, 23))
        self.pushButtonSelectAllLabel.setObjectName("pushButtonSelectAllLabel")
        self.listLabel = QtWidgets.QListView(self.tabLabel)
        self.listLabel.setGeometry(QtCore.QRect(10, 40, 231, 241))
        self.listLabel.setObjectName("listLabel")
        self.tabCategory.addTab(self.tabLabel, "")
        self.pushButtonCancel = QtWidgets.QPushButton(FilterDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(170, 330, 75, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.pushButtonOk = QtWidgets.QPushButton(FilterDialog)
        self.pushButtonOk.setGeometry(QtCore.QRect(90, 330, 75, 23))
        self.pushButtonOk.setObjectName("pushButtonOk")

        self.retranslateUi(FilterDialog)
        self.tabCategory.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FilterDialog)

    def retranslateUi(self, FilterDialog):
        _translate = QtCore.QCoreApplication.translate
        FilterDialog.setWindowTitle(_translate("FilterDialog", "Filter"))
        self.pushButtonDeselectAllSystem.setText(_translate("FilterDialog", "Deselect all"))
        self.pushButtonSelectAllSystem.setText(_translate("FilterDialog", "Select all"))
        self.tabCategory.setTabText(self.tabCategory.indexOf(self.tabSystem), _translate("FilterDialog", "System"))
        self.pushButtonDeselectAllStatus.setText(_translate("FilterDialog", "Deselect all"))
        self.pushButtonSelectAllStatus.setText(_translate("FilterDialog", "Select all"))
        self.tabCategory.setTabText(self.tabCategory.indexOf(self.tabStatus), _translate("FilterDialog", "Status"))
        self.pushButtonDeselectAllLabel.setText(_translate("FilterDialog", "Deselect all"))
        self.pushButtonSelectAllLabel.setText(_translate("FilterDialog", "Select all"))
        self.tabCategory.setTabText(self.tabCategory.indexOf(self.tabLabel), _translate("FilterDialog", "Label"))
        self.pushButtonCancel.setText(_translate("FilterDialog", "Cancel"))
        self.pushButtonOk.setText(_translate("FilterDialog", "Ok"))

import views.app_icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FilterDialog = QtWidgets.QDialog()
    ui = Ui_FilterDialog()
    ui.setupUi(FilterDialog)
    FilterDialog.show()
    sys.exit(app.exec_())

