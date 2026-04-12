class Pessoa_class:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def mostrar_nome(self):
        return self.nome
    
    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
    
    def imprimir_endereco(self):
        return self.endereco
    
pessoa1 = Pessoa_class("João Silva", 25, "Rua A, 123")
print(f"Nome: {pessoa1.mostrar_nome()}")
pessoa1.alterar_idade(26)
print(f"Endereço: {pessoa1.imprimir_endereco()}")
print()