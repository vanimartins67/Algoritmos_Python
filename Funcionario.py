class Funcionario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha

    
    def logar(self):
        print(f" {self.nome} logado com sucesso!")


    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        return True
    

f1 = Funcionario("Eliandro", "lili@eli.com", "1234")
f2 = Funcionario("Felix", "felix@gmail.com", "4321")
f1.logar()


class Gerente(Funcionario):
    def __init__(self, nome, login, senha, setor):
        super().__init__(nome, login, senha)
        self.setor = setor

luan = Gerente ("Luan Victor", "lulu@gmail.com", "1234", "Vendas")
luan.logar()
luan.alterar_senha("7890")
print(luan.senha)
