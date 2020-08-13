/********************************************************************************
** Form generated from reading UI file 'select_system_dialog.ui'
**
** Created by: Qt User Interface Compiler version 5.9.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SELECT_SYSTEM_DIALOG_H
#define UI_SELECT_SYSTEM_DIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QListView>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_SelectSystemDialog
{
public:
    QLabel *label;
    QListView *listViewGames;
    QPushButton *pushButtonOk;
    QPushButton *pushButtonCancel;

    void setupUi(QDialog *SelectSystemDialog)
    {
        if (SelectSystemDialog->objectName().isEmpty())
            SelectSystemDialog->setObjectName(QStringLiteral("SelectSystemDialog"));
        SelectSystemDialog->resize(270, 286);
        SelectSystemDialog->setMinimumSize(QSize(270, 286));
        SelectSystemDialog->setMaximumSize(QSize(270, 286));
        QIcon icon;
        icon.addFile(QStringLiteral(":/app_icon/shelf.png"), QSize(), QIcon::Normal, QIcon::Off);
        SelectSystemDialog->setWindowIcon(icon);
        label = new QLabel(SelectSystemDialog);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(10, 10, 301, 16));
        listViewGames = new QListView(SelectSystemDialog);
        listViewGames->setObjectName(QStringLiteral("listViewGames"));
        listViewGames->setGeometry(QRect(10, 30, 251, 221));
        pushButtonOk = new QPushButton(SelectSystemDialog);
        pushButtonOk->setObjectName(QStringLiteral("pushButtonOk"));
        pushButtonOk->setEnabled(true);
        pushButtonOk->setGeometry(QRect(95, 257, 75, 23));
        pushButtonCancel = new QPushButton(SelectSystemDialog);
        pushButtonCancel->setObjectName(QStringLiteral("pushButtonCancel"));
        pushButtonCancel->setGeometry(QRect(185, 257, 75, 23));

        retranslateUi(SelectSystemDialog);

        QMetaObject::connectSlotsByName(SelectSystemDialog);
    } // setupUi

    void retranslateUi(QDialog *SelectSystemDialog)
    {
        SelectSystemDialog->setWindowTitle(QApplication::translate("SelectSystemDialog", "System selection", Q_NULLPTR));
        label->setText(QApplication::translate("SelectSystemDialog", "Select the system:", Q_NULLPTR));
        pushButtonOk->setText(QApplication::translate("SelectSystemDialog", "Ok", Q_NULLPTR));
        pushButtonCancel->setText(QApplication::translate("SelectSystemDialog", "Cancel", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class SelectSystemDialog: public Ui_SelectSystemDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SELECT_SYSTEM_DIALOG_H
