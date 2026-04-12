from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from client.chat_client import ChatClient


class MainWindow:
    def __init__(self):
        # Carrega UI do Qt Designer
        loader = QUiLoader()
        ui_file = QFile("ui/tela.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()

        # Cliente
        self.client = ChatClient()

        # Conectar botão
        self.ui.enviar.clicked.connect(self.enviar_mensagem)

    def enviar_mensagem(self):
        msg = self.ui.input_msg.text()

        if msg:
            self.client.enviar(msg)
            self.ui.chat.append(f"Você: {msg}")
            self.ui.input_msg.clear()