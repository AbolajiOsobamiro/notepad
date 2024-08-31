# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notepad3.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QScrollBar, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Padnote(object):
    def setupUi(self, Padnote):
        if not Padnote.objectName():
            Padnote.setObjectName(u"Padnote")
        Padnote.resize(779, 251)
        self.actionquit = QAction(Padnote)
        self.actionquit.setObjectName(u"actionquit")
        self.actioncopy = QAction(Padnote)
        self.actioncopy.setObjectName(u"actioncopy")
        self.actionpaste = QAction(Padnote)
        self.actionpaste.setObjectName(u"actionpaste")
        self.actioncut = QAction(Padnote)
        self.actioncut.setObjectName(u"actioncut")
        self.actionundo = QAction(Padnote)
        self.actionundo.setObjectName(u"actionundo")
        self.actionredo = QAction(Padnote)
        self.actionredo.setObjectName(u"actionredo")
        self.actionhelp = QAction(Padnote)
        self.actionhelp.setObjectName(u"actionhelp")
        self.actionAbout = QAction(Padnote)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAboutQt = QAction(Padnote)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        self.actionSave = QAction(Padnote)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSaveas = QAction(Padnote)
        self.actionSaveas.setObjectName(u"actionSaveas")
        self.centralwidget = QWidget(Padnote)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalScrollBar = QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalScrollBar)

        Padnote.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Padnote)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 779, 22))
        self.file_menu = QMenu(self.menubar)
        self.file_menu.setObjectName(u"file_menu")
        self.edit_menu = QMenu(self.menubar)
        self.edit_menu.setObjectName(u"edit_menu")
        self.help_menu = QMenu(self.menubar)
        self.help_menu.setObjectName(u"help_menu")
        self.about_menu = QMenu(self.menubar)
        self.about_menu.setObjectName(u"about_menu")
        Padnote.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Padnote)
        self.statusbar.setObjectName(u"statusbar")
        Padnote.setStatusBar(self.statusbar)

        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.edit_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())
        self.menubar.addAction(self.about_menu.menuAction())
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.actionquit)
        self.file_menu.addAction(self.actionSave)
        self.file_menu.addAction(self.actionSaveas)
        self.edit_menu.addSeparator()
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.actioncopy)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.actionpaste)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.actioncut)
        self.edit_menu.addAction(self.actionundo)
        self.edit_menu.addAction(self.actionredo)
        self.help_menu.addSeparator()
        self.help_menu.addAction(self.actionhelp)
        self.about_menu.addSeparator()
        self.about_menu.addAction(self.actionAbout)
        self.about_menu.addSeparator()
        self.about_menu.addAction(self.actionAboutQt)

        self.retranslateUi(Padnote)

        QMetaObject.connectSlotsByName(Padnote)
    # setupUi

    def retranslateUi(self, Padnote):
        Padnote.setWindowTitle(QCoreApplication.translate("Padnote", u"MainWindow", None))
        self.actionquit.setText(QCoreApplication.translate("Padnote", u"Quit", None))
        self.actioncopy.setText(QCoreApplication.translate("Padnote", u"Copy", None))
        self.actionpaste.setText(QCoreApplication.translate("Padnote", u"Paste", None))
        self.actioncut.setText(QCoreApplication.translate("Padnote", u"Cut", None))
        self.actionundo.setText(QCoreApplication.translate("Padnote", u"undo", None))
        self.actionredo.setText(QCoreApplication.translate("Padnote", u"redo", None))
        self.actionhelp.setText(QCoreApplication.translate("Padnote", u"Help", None))
        self.actionAbout.setText(QCoreApplication.translate("Padnote", u"About", None))
        self.actionAboutQt.setText(QCoreApplication.translate("Padnote", u"AboutQt", None))
        self.actionSave.setText(QCoreApplication.translate("Padnote", u"Save", None))
        self.actionSaveas.setText(QCoreApplication.translate("Padnote", u"Saveas", None))
        self.file_menu.setTitle(QCoreApplication.translate("Padnote", u"File", None))
        self.edit_menu.setTitle(QCoreApplication.translate("Padnote", u"Edit", None))
        self.help_menu.setTitle(QCoreApplication.translate("Padnote", u"Help", None))
        self.about_menu.setTitle(QCoreApplication.translate("Padnote", u"About", None))
    # retranslateUi

