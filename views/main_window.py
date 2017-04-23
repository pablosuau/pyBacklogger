# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sun Apr 09 09:29:41 2017
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/app_icon/shelf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonAddGame = QtGui.QPushButton(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddGame.sizePolicy().hasHeightForWidth())
        self.pushButtonAddGame.setSizePolicy(sizePolicy)
        self.pushButtonAddGame.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButtonAddGame.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButtonAddGame.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAddGame.setIcon(icon1)
        self.pushButtonAddGame.setObjectName(_fromUtf8("pushButtonAddGame"))
        self.horizontalLayout.addWidget(self.pushButtonAddGame)
        self.pushButtonRemoveGame = QtGui.QPushButton(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRemoveGame.sizePolicy().hasHeightForWidth())
        self.pushButtonRemoveGame.setSizePolicy(sizePolicy)
        self.pushButtonRemoveGame.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButtonRemoveGame.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButtonRemoveGame.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRemoveGame.setIcon(icon2)
        self.pushButtonRemoveGame.setObjectName(_fromUtf8("pushButtonRemoveGame"))
        self.horizontalLayout.addWidget(self.pushButtonRemoveGame)
        self.pushButtonLoadBacklog = QtGui.QPushButton(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLoadBacklog.sizePolicy().hasHeightForWidth())
        self.pushButtonLoadBacklog.setSizePolicy(sizePolicy)
        self.pushButtonLoadBacklog.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButtonLoadBacklog.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButtonLoadBacklog.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/load.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLoadBacklog.setIcon(icon3)
        self.pushButtonLoadBacklog.setObjectName(_fromUtf8("pushButtonLoadBacklog"))
        self.horizontalLayout.addWidget(self.pushButtonLoadBacklog)
        self.pushButtonSaveBacklog = QtGui.QPushButton(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSaveBacklog.sizePolicy().hasHeightForWidth())
        self.pushButtonSaveBacklog.setSizePolicy(sizePolicy)
        self.pushButtonSaveBacklog.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButtonSaveBacklog.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButtonSaveBacklog.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSaveBacklog.setIcon(icon4)
        self.pushButtonSaveBacklog.setObjectName(_fromUtf8("pushButtonSaveBacklog"))
        self.horizontalLayout.addWidget(self.pushButtonSaveBacklog)
        self.pushButtonReloadScores = QtGui.QPushButton(MainWindow)
        self.pushButtonReloadScores.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonReloadScores.sizePolicy().hasHeightForWidth())
        self.pushButtonReloadScores.setSizePolicy(sizePolicy)
        self.pushButtonReloadScores.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButtonReloadScores.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButtonReloadScores.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/reload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonReloadScores.setIcon(icon5)
        self.pushButtonReloadScores.setObjectName(_fromUtf8("pushButtonReloadScores"))
        self.horizontalLayout.addWidget(self.pushButtonReloadScores)
        self.pushButtonSortData = QtGui.QPushButton(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSortData.sizePolicy().hasHeightForWidth())
        self.pushButtonSortData.setSizePolicy(sizePolicy)
        self.pushButtonSortData.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButtonSortData.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButtonSortData.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/sort.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSortData.setIcon(icon6)
        self.pushButtonSortData.setCheckable(True)
        self.pushButtonSortData.setChecked(False)
        self.pushButtonSortData.setObjectName(_fromUtf8("pushButtonSortData"))
        self.horizontalLayout.addWidget(self.pushButtonSortData)
        self.pushButtonFilterData = QtGui.QPushButton(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonFilterData.sizePolicy().hasHeightForWidth())
        self.pushButtonFilterData.setSizePolicy(sizePolicy)
        self.pushButtonFilterData.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButtonFilterData.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButtonFilterData.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/filter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonFilterData.setIcon(icon7)
        self.pushButtonFilterData.setCheckable(True)
        self.pushButtonFilterData.setObjectName(_fromUtf8("pushButtonFilterData"))
        self.horizontalLayout.addWidget(self.pushButtonFilterData)
        self.label = QtGui.QLabel(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(46, 13))
        self.label.setMaximumSize(QtCore.QSize(46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEditSearchGame = QtGui.QLineEdit(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSearchGame.sizePolicy().hasHeightForWidth())
        self.lineEditSearchGame.setSizePolicy(sizePolicy)
        self.lineEditSearchGame.setMinimumSize(QtCore.QSize(201, 20))
        self.lineEditSearchGame.setMaximumSize(QtCore.QSize(201, 20))
        self.lineEditSearchGame.setObjectName(_fromUtf8("lineEditSearchGame"))
        self.horizontalLayout.addWidget(self.lineEditSearchGame)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(208, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.table = Table(MainWindow)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout.addWidget(self.table)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog", None))
        self.pushButtonAddGame.setToolTip(_translate("MainWindow", "Add game/s", None))
        self.pushButtonRemoveGame.setToolTip(_translate("MainWindow", "Delete game/s", None))
        self.pushButtonLoadBacklog.setToolTip(_translate("MainWindow", "Load backlog", None))
        self.pushButtonSaveBacklog.setToolTip(_translate("MainWindow", "Save backlog", None))
        self.pushButtonReloadScores.setToolTip(_translate("MainWindow", "Reload scores", None))
        self.pushButtonSortData.setToolTip(_translate("MainWindow", "Sort games", None))
        self.pushButtonFilterData.setToolTip(_translate("MainWindow", "Filter games", None))
        self.label.setText(_translate("MainWindow", "Search:", None))

from table import Table
import main_window_rc
import app_icon_rc
