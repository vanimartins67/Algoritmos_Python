def hello():
    print("Olá!!")
hello()

def hello(nome):
    print("Olá", nome)

hello("Ederson")


def hello(nome):
    print("Seja Bem-Vindo", nome)
a = input("Digite seu nome: ")
hello(a)

def hello(nome):
    print("Olá", nome)
hello("Ederson")
hello("João")
hello("Maria")

def hello(nome, idade):
    print("Olá", nome, "\nSua idade é:", idade)

hello("Vanessa", 44)

def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario = horas * taxa
    else:
        h_excd = horas - 40
        salario = 40 * taxa + (h_excd*(1.5*taxa))
    print(salario)
a = float(input("Horas: "))
b = float(input("Valor da hora: "))
calcular_pagamento(a,b)

def soma(x,y):
    result= x + y
    return result
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
res = soma(a,b)
print("Soma:", res)


