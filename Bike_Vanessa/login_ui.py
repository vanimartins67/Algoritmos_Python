# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.vboxLayout.addWidget(self.label)

        self.inputUsuario = QLineEdit(self.centralwidget)
        self.inputUsuario.setObjectName(u"inputUsuario")

        self.vboxLayout.addWidget(self.inputUsuario)

        self.inputSenha = QLineEdit(self.centralwidget)
        self.inputSenha.setObjectName(u"inputSenha")
        self.inputSenha.setEchoMode(QLineEdit.Password)

        self.vboxLayout.addWidget(self.inputSenha)

        self.btnEntrar = QPushButton(self.centralwidget)
        self.btnEntrar.setObjectName(u"btnEntrar")

        self.vboxLayout.addWidget(self.btnEntrar)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label.setText(QCoreApplication.translate("Login", u"Login", None))
        self.inputUsuario.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.inputSenha.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.btnEntrar.setText(QCoreApplication.translate("Login", u"Entrar", None))
    # retranslateUi

