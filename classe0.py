class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def mostrar_endereco(self):
        return self.endereco
    
    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco
        print(f"Endereço alterado para: {novo_endereco}")

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
    
    def mostrar_curso(self):
        return self.curso
    
    def alterar_curso(self, novo_curso):
        self.curso = novo_curso
        print(f"Curso alterado para: {novo_curso}")

class AlunoComNotas(Pessoa):
    def __init__(self, nome, idade, endereco, matricula, curso, n1, n2, n3):
        super().__init__(nome, idade, endereco)
        self.matricula = matricula
        self.curso = curso
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def calcular_media(self):
        return (self.n1 + self.n2 + self.n3) / 3

    def situacao(self):
        media = self.calcular_media()
        if media >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

class NumeroComplexo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario
    
    def somar(self, outro):
        real = self.real + outro.real
        imaginario = self.imaginario + outro.imaginario
        return NumeroComplexo(real, imaginario)
    
    def subtrair(self, outro):
        real = self.real - outro.real
        imaginario = self.imaginario - outro.imaginario
        return NumeroComplexo(real, imaginario)
    
    def __str__(self):
        return f"{self.real} + {self.imaginario}i"

class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def exibir(self):
        print(f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}")

    def incrementar(self, segundos):
        self.segundo += segundos
        while self.segundo >= 60:
            self.segundo -= 60
            self.minuto += 1
        while self.minuto >= 60:
            self.minuto -= 60
            self.hora += 1

class Vetor3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def soma(self, outro):
        return Vetor3D(self.x + outro.x, self.y + outro.y, self.z + outro.z)
    
    def produto_escalar(self, outro):
        return self.x * outro.x + self.y * outro.y + self.z * outro.z
    
    def modulo(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco
    
    def exibir_dados(self):
        return f"Marca: {self.marca}, Ano: {self.ano}, Preço: R$ {self.preco:.2f}"

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    
    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado")
    
    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado")
            return True
        else:
            print("Saldo insuficiente")
            return False

print("=== PESSOA ===")
p1 = Pessoa("Vanessa", 45, "Rua Imaginária")
print(f"Endereço: {p1.mostrar_endereco()}")
p1.alterar_endereco("Rua Nova, 123")

print("\n=== ALUNO ===")
a1 = Aluno("Vanessa", "123456", "ADS")
print(f"Curso: {a1.mostrar_curso()}")
a1.alterar_curso("Sistemas de Informação")

print("\n=== ALUNO COM NOTAS ===")
aluno1 = AlunoComNotas("Ana", 22, "Rua Central", "2024001", "Engenharia", 8.0, 7.5, 9.0)
print(f"Média: {aluno1.calcular_media():.2f}")
print(f"Situação: {aluno1.situacao()}")

print("\n=== NÚMERO COMPLEXO ===")
c1 = NumeroComplexo(2, 3)
c2 = NumeroComplexo(1, 4)
c3 = c1.somar(c2)
print(f"Soma: {c3}")

print("\n=== HORÁRIO ===")
h1 = Horario(14, 30, 20)
print("Horário inicial:", end=" ")
h1.exibir()
h1.incrementar(100)
print("Horário após incremento:", end=" ")
h1.exibir()

print("\n=== VETOR ===")
v1 = Vetor3D(1, 2, 3)
v2 = Vetor3D(4, 5, 6)
v3 = v1.soma(v2)
print(f"Soma: {v3}")
print(f"Módulo de v1: {v1.modulo():.2f}")

print("\n=== CARRO ===")
carro1 = Carro("Fiat", 2020, 45000.00)
print(carro1.exibir_dados())

print("\n=== CONTA CORRENTE ===")
conta1 = ContaCorrente("12345", "João Silva")
conta1.deposito(1000)
conta1.saque(300)
print(f"Saldo final: R$ {conta1.saldo:.2f}")

print("\n=== CADASTRO DE ALUNOS ===")
alunos = []
for i in range(2):
    print(f"Aluno {i+1}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    endereco = input("Endereço: ")
    matricula = input("Matrícula: ")
    curso = input("Curso: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))

    aluno = AlunoComNotas(nome, idade, endereco, matricula, curso, n1, n2, n3)
    alunos.append(aluno)

print("\n=== RESULTADOS ===")
for aluno in alunos:
    media = aluno.calcular_media()
    situacao = aluno.situacao()
    print(f"{aluno.nome} - Média: {media:.2f} - {situacao}")

print("\n=== LISTA DE CARROS ===")
carros = [
    Carro("Fiat", 2020, 45000),
    Carro("Ford", 2022, 65000),
    Carro("Chevrolet", 2019, 38000)
]

valor = float(input("\nDigite um valor para filtrar carros: "))
print("Carros com preço menor que R$", valor)
for carro in carros:
    if carro.preco < valor:
        print(carro.exibir_dados())