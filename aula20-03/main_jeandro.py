from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        ui_file = QFile("tela.ui")
        ui_file.open(QFile.ReadOnly)

        self.ui = loader.load(ui_file)
        ui_file.close()

        # BOTÃO CORRETO
        self.ui.pushButton_calcular.clicked.connect(self.acao_botao)

    def acao_botao(self):
        try:
            # PEGANDO OS VALORES CERTOS
            v1 = float(self.ui.lineEdit_valor1.text())
            v2 = float(self.ui.lineEdit_valor2.text())

            resultado = v1 + v2

            # MOSTRANDO RESULTADO
            self.ui.lineEdit_3_result.setText(str(resultado))

        except ValueError:
            # CASO DIGITE TEXTO OU DEIXE VAZIO
            self.ui.lineEdit_3_result.setText("Erro")


app = QApplication(sys.argv)
window = MainWindow()
window.ui.show()
sys.exit(app.exec())