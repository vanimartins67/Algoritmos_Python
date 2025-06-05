# 1.	Crie uma função que receba um nome e imprima uma saudação personalizada.
def hello(nome):
    print("Seja Bem-Vindo(a)", nome)
a = input("Digite seu nome: ")
hello(a)

# 2.	Crie uma função que receba dois números e retorne sua soma.
def soma(a, b):
    resultado = a + b
    print("Resultado da soma:", resultado)
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
soma(a, b)

# 3.	Escreva uma função que calcule o quadrado de um número.
def quadrado(numero):
    return numero ** 2
num = float(input("Digite um número: "))
print("O quadrado de", num, "é", quadrado(num))

# 4.	Escreva uma função que verifique se um número é par.
def par(numero):
    return numero % 2 == 0
num = int(input("Digite um número: "))
if par(num):
    print(num, "é par")
else:
    print(num, "é ímpar")

# 5.	Escreva uma função que receba uma lista de números e retorne o maior elemento.
lista = [20, 10, 50, 40, 30]
def maior(lista):
    return max(lista)
print("O maior número é:", maior(lista))

# 6.	Crie uma função que calcule o fatorial de um número (sem usar recursão).
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
n = int(input("Digite um número: "))
print(fatorial(n)) 
        
# 7.	Crie uma função que receba um número e retorne True se ele for primo.
def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0: 
            return False     
    return True
numero = int(input("Digite um número: "))
print(primo(numero))


# 8.	Crie uma função que inverta uma string.

# 9.	Crie uma função que receba uma lista de nomes e retorne apenas os nomes com mais de 5 letras.

# 10.	Escreva uma função que conte quantas vogais há em uma string.

# 11.	Crie uma função que receba um número e retorne uma lista com todos os divisores dele.

# 12.	Crie uma função que converta graus Celsius para Fahrenheit.

# 13.	Crie uma função que receba uma string e retorne a mesma string sem espaços.

# 14.	Crie uma função que receba uma lista e retorne a média dos elementos.

# 15.	Escreva uma função que receba uma palavra e retorne True se ela for um palíndromo.

# 16.	Crie uma função que gere uma lista com os n primeiros números pares.

# 17.	Escreva uma função que receba um número e retorne a tabuada dele (de 1 a 10).

# 18.	Crie uma função que calcule a área de um retângulo (base × altura).

# 19.	Crie uma função que retorne o menor valor entre três números.

# 20.	Escreva uma função que simule o lançamento de um dado de 6 faces (use random.randint).
