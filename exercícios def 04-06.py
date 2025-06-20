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
def inverter_string(s):
    invertida = ""
    for i in s:
        invertida = i + invertida
    return invertida

# 9.	Crie uma função que receba uma lista de nomes e retorne apenas os nomes com mais de 5 letras.
def nomes_longos(lista_nomes):
    resultado = []    
    for nome in lista_nomes: 
        if len(nome) > 5:     
            resultado.append(nome)    
    return resultado 

# 10.	Escreva uma função que conte quantas vogais há em uma string.
def contar_vogais(s):
    vogais = "aeiouAEIOU"  
    contador = 0           
    for i in s:         
        if i in vogais:
            contador += 1 
        return contador        

# 11.	Crie uma função que receba um número e retorne uma lista com todos os divisores dele.
def divisores(num):
    lista = []
    for i in range(1, num + 1):
        if num % i == 0:
            lista.append(i)
    return lista

# 12.	Crie uma função que converta graus Celsius para Fahrenheit.
def celsius_para_fahrenheit(c):
    return c * 1.8 + 32 

# 13.	Crie uma função que receba uma string e retorne a mesma string sem espaços.
def remover_espacos(s):
    resultado = ""
    for i in s:
        if i != " ":
            resultado += i
    return resultado

# 14.	Crie uma função que receba uma lista e retorne a média dos elementos.
def media_lista(lista):
    total = 0
    contagem = 0
    for num in lista:
        total += num
        contagem += 1
    return total / contagem

# 15.	Escreva uma função que receba uma palavra e retorne True se ela for um palíndromo.
def eh_palindromo(palavra):
    palavra = palavra.lower()       
    palavra = palavra.replace(" ", "")  
    inicio = 0
    fim = len(palavra) - 1
    while inicio < fim:
        if palavra[inicio] != palavra[fim]:
            return False
        inicio += 1
        fim -= 1
    return True

# 16.	Crie uma função que gere uma lista com os n primeiros números pares.
def n_pares(n):
    pares = []
    num = 0
    while len(pares) < n:
        pares.append(num)
        num += 2
    return pares

# 17.	Escreva uma função que receba um número e retorne a tabuada dele (de 1 a 10).
def tabuada(num):
    tabuada = []
    for i in range(1, 11):
        tabuada.append(num * i)
    return tabuada

# 18.	Crie uma função que calcule a área de um retângulo (base × altura).
def area_retangulo(base, altura):
    return base * altura

# 19.	Crie uma função que retorne o menor valor entre três números.
def menor_de_tres(a, b, c):
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    return menor

# 20.	Escreva uma função que simule o lançamento de um dado de 6 faces (use random.randint).
import random
def lancar_dado():
  return random.randint(1, 6)

# 21. Crie uma função que receba uma lista de números e retorne uma nova lista com os números elevados ao quadrado.

# 22. Crie uma função que calcule a soma dos dígitos de um número inteiro.

# 23. Escreva uma função que receba uma frase e retorne a quantidade de palavras.

# 24. Crie uma função que substitua todas as vogais de uma string por "*".

# 25. Crie uma função que receba uma lista e retorne os elementos únicos (sem usar set).

# 26. Crie uma função que receba uma lista e um número n, e retorne os n maiores valores da lista.

# 27. Escreva uma função que calcule a área de um triângulo (base × altura ÷ 2).

# 28. Crie uma função recursiva para calcular o fatorial de um número.

# 29. Crie uma função recursiva que calcule o n-ésimo número da sequência de Fibonacci.

# 30. Escreva uma função que embaralhe os caracteres de uma string (use random.shuffle).

# 31. Crie uma função que simule uma calculadora simples (operações: +, -, *, /), com três parâmetros: número 1, número 2 e operação.

# 32. Crie uma função que retorne os números pares de uma lista usando list comprehension.

# 33. Escreva uma função que recebe um número decimal e retorna sua representação binária.

# 34. Escreva uma função que receba uma lista e retorne um dicionário com a contagem de cada elemento.

# 35. Crie uma função que receba uma data (dia, mês, ano) e diga se ela é válida (considere apenas datas do calendário gregoriano, sem considerar anos bissextos).

# 36. Escreva uma função que identifique o segundo maior número em uma lista.

# 37. Crie uma função que receba uma lista de strings e retorne a maior delas.

# 38. Escreva uma função que calcule a distância entre dois pontos (x1, y1) e (x2, y2).

# 39. Crie uma função que receba o valor de uma compra e retorne o valor com 10% de desconto.

# 40. Crie uma função que calcule juros compostos: montante = capital * (1 + taxa) ** tempo.
