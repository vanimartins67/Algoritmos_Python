class Conta:
    def __init__(self, nome, cpf, numero, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
            return True
        print("Valor de depósito inválido!")
        return False
    
    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
            return True
        print("Saldo insuficiente ou valor inválido!")
        return False
    
    def imprimir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        return self.saldo

conta1 = Conta("Carlos Oliveira", "123.456.789-00", "001", 1000.00)
print(f"Titular: {conta1.nome}")
conta1.depositar(500.00)
conta1.sacar(200.00)
conta1.imprimir_saldo()
conta1.sacar(2000.00) 
print()