import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

from login_ui import Ui_Login
from menu_ui import Ui_Menu
from cliente_ui import Ui_Cliente
from bike_ui import Ui_Bicicleta
from service_ui import Ui_Servico
from resumo_ui import Ui_Resumo


dados = {}


# ===== LOGIN =====
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.btnEntrar.clicked.connect(self.abrir_menu)

    def abrir_menu(self):
        self.menu = Menu()
        self.menu.show()
        self.close()


# ===== MENU =====
class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)

        self.ui.btnNovo.clicked.connect(self.abrir_cliente)

        self.ui.btnSair.clicked.connect(self.voltar)

    def abrir_cliente(self):
        self.cliente = Cliente()
        self.cliente.show()
        self.close()

    def voltar(self):
        self.login = Login()
        self.login.show()
        self.close()


# ===== CLIENTE =====
class Cliente(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Cliente()
        self.ui.setupUi(self)

        self.ui.btnProximo.clicked.connect(self.salvar)

        # botão voltar
        self.btnVoltar = QPushButton("Voltar", self)
        self.btnVoltar.move(10, 10)
        self.btnVoltar.clicked.connect(self.voltar)

    def salvar(self):
        nome = self.ui.inputNome.text()
        telefone = self.ui.inputTelefone.text()
        cpf = self.ui.inputCpf.text()

        if nome == "" or telefone == "" or cpf == "":
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")
            return

        dados["nome"] = nome
        dados["telefone"] = telefone
        dados["cpf"] = cpf

        self.bike = Bike()
        self.bike.show()
        self.close()

    def voltar(self):
        self.menu = Menu()
        self.menu.show()
        self.close()


# ===== BIKE =====
class Bike(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Bicicleta()
        self.ui.setupUi(self)

        self.ui.btnProximo.clicked.connect(self.salvar)

        # botão voltar
        self.btnVoltar = QPushButton("Voltar", self)
        self.btnVoltar.move(10, 10)
        self.btnVoltar.clicked.connect(self.voltar)

    def salvar(self):
        marca = self.ui.inputMarca.text()
        modelo = self.ui.inputModelo.text()
        cor = self.ui.inputCor.text()

        if marca == "" or modelo == "" or cor == "":
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")
            return

        dados["marca"] = marca
        dados["modelo"] = modelo
        dados["cor"] = cor

        self.service = Service()
        self.service.show()
        self.close()

    def voltar(self):
        self.cliente = Cliente()
        self.cliente.show()
        self.close()


# ===== SERVICE =====
class Service(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Servico()
        self.ui.setupUi(self)

        self.ui.btnFinalizar.clicked.connect(self.salvar)

        # botão voltar
        self.btnVoltar = QPushButton("Voltar", self)
        self.btnVoltar.move(10, 10)
        self.btnVoltar.clicked.connect(self.voltar)

    def salvar(self):
        servico = self.ui.inputServico.toPlainText()

        if servico == "":
            QMessageBox.warning(self, "Erro", "Descreva o serviço!")
            return

        dados["servico"] = servico

        self.resumo = Resumo()
        self.resumo.show()
        self.close()

    def voltar(self):
        self.bike = Bike()
        self.bike.show()
        self.close()


# ===== RESUMO =====
class Resumo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Resumo()
        self.ui.setupUi(self)

        texto = f"""
Cliente: {dados.get("nome")}
Telefone: {dados.get("telefone")}
CPF: {dados.get("cpf")}

Bicicleta:
Marca: {dados.get("marca")}
Modelo: {dados.get("modelo")}
Cor: {dados.get("cor")}

Serviço:
{dados.get("servico")}
"""

        self.ui.labelResumo.setText(texto)

        # salvar em arquivo
        with open("atendimento.txt", "a", encoding="utf-8") as f:
            f.write(texto + "\n" + "-"*30 + "\n")

        # botão voltar
        self.btnVoltar = QPushButton("Voltar", self)
        self.btnVoltar.move(10, 10)
        self.btnVoltar.clicked.connect(self.voltar)

    def voltar(self):
        self.menu = Menu()
        self.menu.show()
        self.close()


# ===== MAIN =====
app = QApplication(sys.argv)

window = Login()
window.show()

sys.exit(app.exec())
