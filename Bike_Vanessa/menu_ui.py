# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
class Ui_Menu(object):
    def setupUi(self, Menu):
        if not Menu.objectName():
            Menu.setObjectName(u"Menu")
        self.centralwidget = QWidget(Menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.vboxLayout.addWidget(self.label)

        self.btnNovo = QPushButton(self.centralwidget)
        self.btnNovo.setObjectName(u"btnNovo")

        self.vboxLayout.addWidget(self.btnNovo)

        self.btnSair = QPushButton(self.centralwidget)
        self.btnSair.setObjectName(u"btnSair")

        self.vboxLayout.addWidget(self.btnSair)

        Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu)

        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", u"Menu", None))
        self.label.setText(QCoreApplication.translate("Menu", u"Sistema Oficina de Bicicletas", None))
        self.btnNovo.setText(QCoreApplication.translate("Menu", u"Novo Atendimento", None))
        self.btnSair.setText(QCoreApplication.translate("Menu", u"Sair", None))
    # retranslateUi

