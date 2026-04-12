class Pessoa:
    def __init__(self, nome, cpf, fone, email, cidade, estado):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.email = email
        self.cidade = cidade
        self.estado = estado

    def Oi(self):
        print(f'{self.nome} Vanessa ')
    
    def doc(self):
        print(f'{self.cpf} 94970165149 ')
        