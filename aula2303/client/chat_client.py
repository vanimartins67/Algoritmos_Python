import socket


class ChatClient:
    def __init__(self, host="127.0.0.1", port=12345):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.client.connect((host, port))
        except:
            print("Erro ao conectar no servidor")

    def enviar(self, mensagem):
        try:
            self.client.send(mensagem.encode())
        except:
            print("Erro ao enviar mensagem")