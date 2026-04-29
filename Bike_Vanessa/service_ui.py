# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'service.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
class Ui_Servico(object):
    def setupUi(self, Servico):
        if not Servico.objectName():
            Servico.setObjectName(u"Servico")
        self.centralwidget = QWidget(Servico)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.inputServico = QTextEdit(self.centralwidget)
        self.inputServico.setObjectName(u"inputServico")

        self.vboxLayout.addWidget(self.inputServico)

        self.btnFinalizar = QPushButton(self.centralwidget)
        self.btnFinalizar.setObjectName(u"btnFinalizar")

        self.vboxLayout.addWidget(self.btnFinalizar)

        Servico.setCentralWidget(self.centralwidget)

        self.retranslateUi(Servico)

        QMetaObject.connectSlotsByName(Servico)
    # setupUi

    def retranslateUi(self, Servico):
        Servico.setWindowTitle(QCoreApplication.translate("Servico", u"Servi\u00e7o", None))
        self.btnFinalizar.setText(QCoreApplication.translate("Servico", u"Finalizar", None))
    # retranslateUi

