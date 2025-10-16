class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Conta(Pessoa):
    def __init__(self, nome, numero_conta, agencia, senha):
        super().__init__(nome)
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.saldo = 0.0
        self.extrato = []
        self.__senha = senha
    
    def autenticar(self, agencia, conta, senha):
        return self.agencia == agencia and self.numero_conta == conta and self.__senha == senha
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R$ {valor:.2f}")
            return True
        return False
    
    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R$ {valor:.2f}")
            return True
        return False
    
    def consultar_saldo(self):
        return self.saldo
    
    def consultar_extrato(self):
        return self.extrato

class Banco:
    def __init__(self):
        self.contas = []
    
    def encontrar_conta(self, agencia, conta):
        for conta_obj in self.contas:
            if conta_obj.agencia == agencia and conta_obj.numero_conta == conta:
                return conta_obj
        return None
    
    def cadastrar_conta(self):
        print("\nCADASTRO")
        nome = input("Nome do titular: ")
        numero_conta = input("Número da conta: ")
        agencia = input("Agência: ")
        senha = input("Senha: ")
        
        if self.encontrar_conta(agencia, numero_conta):
            print("Conta já existe!")
            return
        
        nova_conta = Conta(nome, numero_conta, agencia, senha)
        self.contas.append(nova_conta)
        print("Conta cadastrada com sucesso!")
    
    def autenticar_conta(self):
        print("\nLOGIN")
        agencia = input("Agência: ")
        conta = input("Conta: ")
        senha = input("Senha: ")
        
        conta_obj = self.encontrar_conta(agencia, conta)
        if conta_obj and conta_obj.autenticar(agencia, conta, senha):
            return conta_obj
        else:
            print("Agência, conta ou senha inválidos!")
            return None
    
    def consultar_saldo(self):
        conta = self.autenticar_conta()
        if conta:
            print(f"\nSALDO")
            print(f"Saldo: R$ {conta.consultar_saldo():.2f}")
    
    def consultar_extrato(self):
        conta = self.autenticar_conta()
        if conta:
            print(f"\nEXTRATO")
            print(f"Cliente: {conta.nome}")
            for movimentacao in conta.consultar_extrato():
                print(movimentacao)
            print(f"Saldo: R$ {conta.consultar_saldo():.2f}")
    
    def sacar_dinheiro(self):
        conta = self.autenticar_conta()
        if conta:
            print(f"\nSAQUE")
            valor = float(input("Valor para sacar: R$ "))
            if conta.sacar(valor):
                print("Saque realizado!")
            else:
                print("Saldo insuficiente!")
    
    def depositar_dinheiro(self):
        print(f"\nDEPÓSITO")
        agencia = input("Agência: ")
        conta_numero = input("Conta: ")
        
        conta = self.encontrar_conta(agencia, conta_numero)
        if conta:
            valor = float(input("Valor para depositar: R$ "))
            if conta.depositar(valor):
                print("Depósito realizado!")
            else:
                print("Valor inválido!")
        else:
            print("Conta não encontrada!")
    
    def menu(self):
        print("\nEDERSON'S BANK")
        print("1. Cadastrar conta")
        print("2. Saldo")
        print("3. Extrato")
        print("4. Saque")
        print("5. Depósito")
        print("6. Sair")
    
    def executar(self):
        while True:
            self.menu()
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.cadastrar_conta()
            elif opcao == "2":
                self.consultar_saldo()
            elif opcao == "3":
                self.consultar_extrato()
            elif opcao == "4":
                self.sacar_dinheiro()
            elif opcao == "5":
                self.depositar_dinheiro()
            elif opcao == "6":
                print("Obrigado por usar o Ederson's Bank!")
                break
            else:
                print("Opção inválida!")

banco = Banco()
banco.executar()