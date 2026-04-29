# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
class Ui_Cliente(object):
    def setupUi(self, Cliente):
        if not Cliente.objectName():
            Cliente.setObjectName(u"Cliente")
        self.centralwidget = QWidget(Cliente)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.inputNome = QLineEdit(self.centralwidget)
        self.inputNome.setObjectName(u"inputNome")

        self.vboxLayout.addWidget(self.inputNome)

        self.inputTelefone = QLineEdit(self.centralwidget)
        self.inputTelefone.setObjectName(u"inputTelefone")

        self.vboxLayout.addWidget(self.inputTelefone)

        self.inputCpf = QLineEdit(self.centralwidget)
        self.inputCpf.setObjectName(u"inputCpf")

        self.vboxLayout.addWidget(self.inputCpf)

        self.btnProximo = QPushButton(self.centralwidget)
        self.btnProximo.setObjectName(u"btnProximo")

        self.vboxLayout.addWidget(self.btnProximo)

        Cliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(Cliente)

        QMetaObject.connectSlotsByName(Cliente)
    # setupUi

    def retranslateUi(self, Cliente):
        Cliente.setWindowTitle(QCoreApplication.translate("Cliente", u"Cliente", None))
        self.inputNome.setPlaceholderText(QCoreApplication.translate("Cliente", u"Nome", None))
        self.inputTelefone.setPlaceholderText(QCoreApplication.translate("Cliente", u"Telefone", None))
        self.inputCpf.setPlaceholderText(QCoreApplication.translate("Cliente", u"CPF", None))
        self.btnProximo.setText(QCoreApplication.translate("Cliente", u"Pr\u00f3ximo", None))
    # retranslateUi

