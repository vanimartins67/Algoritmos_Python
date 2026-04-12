#01
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_endereco(self):
        print(self.endereco)

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco

pessoa1 = Pessoa("Vanessa", 45, "Rua 12, 65")
print("Endereço atual: ")
pessoa1.mostrar_endereco() 
pessoa1.alterar_endereco("Rua 13, 68")
print("Novo endereço: ")
pessoa1.mostrar_endereco()
print()

#02
class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mostrar_curso(self):
        self.curso  

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso
        return True 

aluno1 = Aluno("Vanessa", "2025001", "ADS")
print("Curso atual:", aluno1.mostrar_curso()) 
resultado = aluno1.alterar_curso("Medicina")
print("Resultado da alteração:", resultado)  
print("Novo curso:", aluno1.mostrar_curso())
print()

#03
class AlunoCurso:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def situacao(self):
        media = self.media()
        if media >= 6.0:  
            return "Aprovado"
        else:
            return "Reprovado"

alunos = [
    AlunoCurso("001", "Ana", 7.5, 8.0, 6.5),
    AlunoCurso("002", "João", 5.0, 4.5, 6.0),
    AlunoCurso("003", "Maria", 8.0, 8.5, 7.5),
    AlunoCurso("004", "Pedro", 6.0, 5.5, 6.5),
    AlunoCurso("005", "Carla", 7.0, 7.5, 7.0)
]

maior_media = alunos[0]
for aluno in alunos:
    if aluno.media() > maior_media.media():
        maior_media = aluno

menor_media = alunos[0]
for aluno in alunos:
    if aluno.media() < menor_media.media():
        menor_media = aluno

print(f"Aluno com maior média: {maior_media.nome} - Média: {maior_media.media()}") 
print(f"Aluno com menor média: {menor_media.nome} - Média: {menor_media.media()}")  

print("\nSituação dos alunos:")
for aluno in alunos:
    print(f"{aluno.nome}: Média = {aluno.media()} - {aluno.situacao()}")  
print()

#04
class NumeroComplexo:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, outro):
        return NumeroComplexo(self.real + outro.real, self.imag + outro.imag)

    def __sub__(self, outro):
        return NumeroComplexo(self.real - outro.real, self.imag - outro.imag)

    def __mul__(self, outro):
        real = self.real * outro.real - self.imag * outro.imag
        imag = self.real * outro.imag + self.imag * outro.real
        return NumeroComplexo(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = NumeroComplexo(2, 3)
c2 = NumeroComplexo(1, 4)
print(f"c1 = {c1}")
print(f"c2 = {c2}")
soma = c1 + c2
print(f"Soma: {soma}")
subtracao = c1 - c2
print(f"Subtração: {subtracao}")
multiplicacao = c1 * c2
print(f"Multiplicação: {multiplicacao}")
print()

#05
class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto  
        self.segundo = segundo

    def incrementar_segundos(self, segundos):
        total_segundos = self.hora * 3600 + self.minuto * 60 + self.segundo + segundos
        self.hora = total_segundos // 3600
        self.minuto = (total_segundos % 3600) // 60
        self.segundo = total_segundos % 60
        # ERRO: não trata caso onde hora > 23

    def diferenca(self, outro):
        segundos_self = self.hora * 3600 + self.minuto * 60 + self.segundo
        segundos_outro = outro.hora * 3600 + outro.minuto * 60 + outro.segundo
        return abs(segundos_self - segundos_outro)

    def __str__(self):
        return f"{self.hora}:{self.minuto}:{self.segundo}"

h1 = Horario(8, 5, 30)
h2 = Horario(14, 20, 15)
print(f"Horário 1: {h1}")
print(f"Horário 2: {h2}")
h1.incrementar_segundos(7200)
print(f"Horário 1 após incremento: {h1}")
print(f"Diferença em segundos: {h1.diferenca(h2)}")
h3 = Horario(23, 59, 59)
h3.incrementar_segundos(3600) 
print(f"Horário 3 após incremento: {h3}")
print()

#06
class Vetor3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def soma(self, outro):
        return Vetor3D(self.x + outro.x, self.y + outro.y, self.z + outro.z)

    def subtracao(self, outro):
        return Vetor3D(self.x - outro.x, self.y - outro.y, self.z - outro.z)

    def produto_escalar(self, outro):
        return self.x * self.x + self.y * self.y + self.z * self.z  

    def produto_vetorial(self, outro):
        x = self.y * outro.z - self.z * outro.y
        y = self.z * outro.x - self.x * outro.z
        z = self.x * outro.y - self.y * outro.x
        return Vetor3D(x, y, z)

    def modulo(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

v1 = Vetor3D(1, 2, 3)
v2 = Vetor3D(4, 5, 6)
print(f"Vetor 1: {v1}")
print(f"Vetor 2: {v2}")
print(f"Soma: {v1.soma(v2)}")
print(f"Subtração: {v1.subtracao(v2)}")
print(f"Produto escalar: {v1.produto_escalar(v2)}") 
print(f"Produto vetorial: {v1.produto_vetorial(v2)}")
print(f"Módulo do vetor 1: {v1.modulo()}")
print()

#07
class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def mostrar_preco(self):
        return self.preco

    def exibir_dados(self):
        return f"Marca: {self.marca}, Ano: {self.ano}, Preço: R${self.preco:.2f}"

carros = [
    Carro("Fiat", 2020, 50000.0),
    Carro("Ford", 2021, 75000.0),
    Carro("VW", 2019, 45000.0),
    Carro("Chevrolet", 2022, 80000.0),
    Carro("Hyundai", 2020, 55000.0)
]

p = 60000.0
print(f"Carros com preço menor que R$ {p:.2f}:")
for carro in carros:
    if carro.preco < p:
        print(carro.exibir_dados())

carro_teste = Carro("Teste", 2020, 0.1 + 0.2)
print(f"\nPreço teste: {carro_teste.preco}")
if carro_teste.preco == 0.3: 
    print("Preço é exatamente 0.3")
else:
    print("Preço NÃO é exatamente 0.3")
print()

#08
class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado.")

    def saque(self, valor):
        self.saldo -= valor  

    def exibir_saldo(self):
        return f"Saldo atual: R$ {self.saldo:.2f}"

conta1 = ContaCorrente("12345", "Vanessa Martins", 1000)
print(f"Conta: {conta1.numero_conta}, Correntista: {conta1.nome_correntista}")
print(conta1.exibir_saldo())
conta1.deposito(500)
conta1.saque(200) 
print(conta1.exibir_saldo()) 
conta1.alterar_nome("Vanessa Almeida")
print(f"Novo nome: {conta1.nome_correntista}")
print()

#09
class Racional:
    def __init__(self, p, q):
        if q == 0:
            raise ValueError("Denominador não pode ser zero")
        self.p = p
        self.q = q

    def inverter_sinal(self):
        self.p = -self.p
        
    def somar(self, outro):
        denominador = self.q * outro.q
        numerador = self.p * outro.q + outro.p * self.q
        return Racional(numerador, denominador)

    def subtrair(self, outro):
        denominador = self.q * outro.q
        numerador = self.p * outro.q - outro.p * self.q
        return Racional(numerador, denominador)

    def multiplicar(self, outro):
        return Racional(self.p * outro.p, self.q * outro.q)

    def dividir(self, outro):
        if outro.p == 0:
            raise ValueError("Divisão por zero")
        return Racional(self.p * outro.q, self.q * outro.p)

    def __str__(self):
        return f"{self.p}/{self.q}"

r1 = Racional(1, 2)
r2 = Racional(3, 4)
print(f"r1 = {r1}")
print(f"r2 = {r2}")
print(f"Soma: {r1.somar(r2)}")
print(f"Subtração: {r1.subtrair(r2)}")
print(f"Multiplicação: {r1.multiplicar(r2)}")
print(f"Divisão: {r1.dividir(r2)}")
r1.inverter_sinal()
print(f"r1 com sinal invertido: {r1}")