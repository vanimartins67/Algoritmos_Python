# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bike.ui'
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
class Ui_Bicicleta(object):
    def setupUi(self, Bicicleta):
        if not Bicicleta.objectName():
            Bicicleta.setObjectName(u"Bicicleta")
        self.centralwidget = QWidget(Bicicleta)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.inputMarca = QLineEdit(self.centralwidget)
        self.inputMarca.setObjectName(u"inputMarca")

        self.vboxLayout.addWidget(self.inputMarca)

        self.inputModelo = QLineEdit(self.centralwidget)
        self.inputModelo.setObjectName(u"inputModelo")

        self.vboxLayout.addWidget(self.inputModelo)

        self.inputCor = QLineEdit(self.centralwidget)
        self.inputCor.setObjectName(u"inputCor")

        self.vboxLayout.addWidget(self.inputCor)

        self.btnProximo = QPushButton(self.centralwidget)
        self.btnProximo.setObjectName(u"btnProximo")

        self.vboxLayout.addWidget(self.btnProximo)

        Bicicleta.setCentralWidget(self.centralwidget)

        self.retranslateUi(Bicicleta)

        QMetaObject.connectSlotsByName(Bicicleta)
    # setupUi

    def retranslateUi(self, Bicicleta):
        Bicicleta.setWindowTitle(QCoreApplication.translate("Bicicleta", u"Bicicleta", None))
        self.inputMarca.setPlaceholderText(QCoreApplication.translate("Bicicleta", u"Marca", None))
        self.inputModelo.setPlaceholderText(QCoreApplication.translate("Bicicleta", u"Modelo", None))
        self.inputCor.setPlaceholderText(QCoreApplication.translate("Bicicleta", u"Cor", None))
        self.btnProximo.setText(QCoreApplication.translate("Bicicleta", u"Pr\u00f3ximo", None))
    # retranslateUi

