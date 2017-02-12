# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter_dialog.ui'
#
# Created: Sun Jan 29 08:59:16 2017
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

class Ui_FilterDialog(object):
    def setupUi(self, FilterDialog):
        FilterDialog.setObjectName(_fromUtf8("FilterDialog"))
        FilterDialog.resize(255, 368)
        FilterDialog.setMinimumSize(QtCore.QSize(255, 368))
        FilterDialog.setMaximumSize(QtCore.QSize(255, 368))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/app_icon/shelf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FilterDialog.setWindowIcon(icon)
        self.tabCategory = QtGui.QTabWidget(FilterDialog)
        self.tabCategory.setGeometry(QtCore.QRect(0, 0, 401, 321))
        self.tabCategory.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabCategory.setObjectName(_fromUtf8("tabCategory"))
        self.tabSystem = QtGui.QWidget()
        self.tabSystem.setObjectName(_fromUtf8("tabSystem"))
        self.pushButtonDeselectAllSystem = QtGui.QPushButton(self.tabSystem)
        self.pushButtonDeselectAllSystem.setGeometry(QtCore.QRect(90, 7, 75, 23))
        self.pushButtonDeselectAllSystem.setObjectName(_fromUtf8("pushButtonDeselectAllSystem"))
        self.pushButtonSelectAllSystem = QtGui.QPushButton(self.tabSystem)
        self.pushButtonSelectAllSystem.setGeometry(QtCore.QRect(10, 7, 75, 23))
        self.pushButtonSelectAllSystem.setObjectName(_fromUtf8("pushButtonSelectAllSystem"))
        self.listSystem = QtGui.QListView(self.tabSystem)
        self.listSystem.setGeometry(QtCore.QRect(10, 40, 231, 241))
        self.listSystem.setObjectName(_fromUtf8("listSystem"))
        self.tabCategory.addTab(self.tabSystem, _fromUtf8(""))
        self.tabStatus = QtGui.QWidget()
        self.tabStatus.setObjectName(_fromUtf8("tabStatus"))
        self.pushButtonDeselectAllStatus = QtGui.QPushButton(self.tabStatus)
        self.pushButtonDeselectAllStatus.setGeometry(QtCore.QRect(90, 7, 75, 23))
        self.pushButtonDeselectAllStatus.setObjectName(_fromUtf8("pushButtonDeselectAllStatus"))
        self.pushButtonSelectAllStatus = QtGui.QPushButton(self.tabStatus)
        self.pushButtonSelectAllStatus.setGeometry(QtCore.QRect(10, 7, 75, 23))
        self.pushButtonSelectAllStatus.setObjectName(_fromUtf8("pushButtonSelectAllStatus"))
        self.listStatus = QtGui.QListView(self.tabStatus)
        self.listStatus.setGeometry(QtCore.QRect(10, 40, 231, 241))
        self.listStatus.setObjectName(_fromUtf8("listStatus"))
        self.tabCategory.addTab(self.tabStatus, _fromUtf8(""))
        self.tabLabel = QtGui.QWidget()
        self.tabLabel.setObjectName(_fromUtf8("tabLabel"))
        self.pushButtonDeselectAllLabel = QtGui.QPushButton(self.tabLabel)
        self.pushButtonDeselectAllLabel.setGeometry(QtCore.QRect(90, 7, 75, 23))
        self.pushButtonDeselectAllLabel.setObjectName(_fromUtf8("pushButtonDeselectAllLabel"))
        self.pushButtonSelectAllLabel = QtGui.QPushButton(self.tabLabel)
        self.pushButtonSelectAllLabel.setGeometry(QtCore.QRect(10, 7, 75, 23))
        self.pushButtonSelectAllLabel.setObjectName(_fromUtf8("pushButtonSelectAllLabel"))
        self.listLabel = QtGui.QListView(self.tabLabel)
        self.listLabel.setGeometry(QtCore.QRect(10, 40, 231, 241))
        self.listLabel.setObjectName(_fromUtf8("listLabel"))
        self.tabCategory.addTab(self.tabLabel, _fromUtf8(""))
        self.pushButtonCancel = QtGui.QPushButton(FilterDialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(170, 330, 75, 23))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.pushButtonOk = QtGui.QPushButton(FilterDialog)
        self.pushButtonOk.setGeometry(QtCore.QRect(90, 330, 75, 23))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))

        self.retranslateUi(FilterDialog)
        self.tabCategory.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FilterDialog)

    def retranslateUi(self, FilterDialog):
        FilterDialog.setWindowTitle(_translate("FilterDialog", "Filter", None))
        self.pushButtonDeselectAllSystem.setText(_translate("FilterDialog", "Deselect all", None))
        self.pushButtonSelectAllSystem.setText(_translate("FilterDialog", "Select all", None))
        self.tabCategory.setTabText(self.tabCategory.indexOf(self.tabSystem), _translate("FilterDialog", "System", None))
        self.pushButtonDeselectAllStatus.setText(_translate("FilterDialog", "Deselect all", None))
        self.pushButtonSelectAllStatus.setText(_translate("FilterDialog", "Select all", None))
        self.tabCategory.setTabText(self.tabCategory.indexOf(self.tabStatus), _translate("FilterDialog", "Status", None))
        self.pushButtonDeselectAllLabel.setText(_translate("FilterDialog", "Deselect all", None))
        self.pushButtonSelectAllLabel.setText(_translate("FilterDialog", "Select all", None))
        self.tabCategory.setTabText(self.tabCategory.indexOf(self.tabLabel), _translate("FilterDialog", "Label", None))
        self.pushButtonCancel.setText(_translate("FilterDialog", "Cancel", None))
        self.pushButtonOk.setText(_translate("FilterDialog", "Ok", None))

import app_icon_rc
