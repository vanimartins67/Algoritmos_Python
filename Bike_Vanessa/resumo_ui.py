# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resumo.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QVBoxLayout, QWidget)
class Ui_Resumo(object):
    def setupUi(self, Resumo):
        if not Resumo.objectName():
            Resumo.setObjectName(u"Resumo")
        self.centralwidget = QWidget(Resumo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelResumo = QLabel(self.centralwidget)
        self.labelResumo.setObjectName(u"labelResumo")

        self.vboxLayout.addWidget(self.labelResumo)

        Resumo.setCentralWidget(self.centralwidget)

        self.retranslateUi(Resumo)

        QMetaObject.connectSlotsByName(Resumo)
    # setupUi

    def retranslateUi(self, Resumo):
        Resumo.setWindowTitle(QCoreApplication.translate("Resumo", u"Resumo", None))
        self.labelResumo.setText(QCoreApplication.translate("Resumo", u"Resumo aparecer\u00e1 aqui", None))
    # retranslateUi

