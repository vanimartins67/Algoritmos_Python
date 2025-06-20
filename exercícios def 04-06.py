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
def quadrados(lista):
    return [x**2 for x in lista]

# 22. Crie uma função que calcule a soma dos dígitos de um número inteiro.
def soma_digitos(numero):
    soma = 0
    while numero > 0:
        soma += numero % 10
        numero //= 10
    return soma

# 23. Escreva uma função que receba uma frase e retorne a quantidade de palavras.
def contar_palavras(frase):
    return len(frase.split())

# 24. Crie uma função que substitua todas as vogais de uma string por "*".
def substituir_vogais(s):
    vogais = "aeiouAEIOU"
    resultado = ""
    for i in s:
        if i in vogais:
            resultado += "*"
        else:
            resultado += i
    return resultado

# 25. Crie uma função que receba uma lista e retorne os elementos únicos (sem usar set).
def elementos_unicos(lista):
    unicos = []
    for item in lista:
        if item not in unicos:
            unicos.append(item)
    return unicos

# 26. Crie uma função que receba uma lista e um número n, e retorne os n maiores valores da lista.
def n_maiores(lista, n):
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada[:n]

# 27. Escreva uma função que calcule a área de um triângulo (base × altura ÷ 2).
def area_triangulo(base, altura):
    return (base * altura) / 2

# 28. Crie uma função recursiva para calcular o fatorial de um número.
def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

# 29. Crie uma função recursiva que calcule o n-ésimo número da sequência de Fibonacci.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 30. Escreva uma função que embaralhe os caracteres de uma string (use random.shuffle).
import random
def embaralhar_string(s):
    lista = list(s)
    random.shuffle(lista)
    return ''.join(lista)

# 31. Crie uma função que simule uma calculadora simples (operações: +, -, *, /), com três parâmetros: número 1, número 2 e operação.
def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"

# 32. Crie uma função que retorne os números pares de uma lista usando list comprehension.
def numeros_pares(lista):
    return [x for x in lista if x % 2 == 0]

# 33. Escreva uma função que recebe um número decimal e retorna sua representação binária.
def decimal_para_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    return binario

# 34. Escreva uma função que receba uma lista e retorne um dicionário com a contagem de cada elemento.
def contar_elementos(lista):
    contagem = {}
    for item in lista:
        if item in contagem:
            contagem[item] += 1
        else:
            contagem[item] = 1
    return contagem

# 35. Crie uma função que receba uma data (dia, mês, ano) e diga se ela é válida (considere apenas datas do calendário gregoriano, sem considerar anos bissextos).
def data_valida(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or (mes == 2 and dia > 28) or (mes in [4, 6, 9, 11] and dia > 30) or (mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31):
        return False
    return True

# 36. Escreva uma função que identifique o segundo maior número em uma lista.
def segundo_maior(lista):
    if len(lista) < 2:
        return None
    lista_ordenada = sorted(list(set(lista)))
    return lista_ordenada[-2]  

# 37. Crie uma função que receba uma lista de strings e retorne a maior delas.
def maior_string(lista):
    if not lista:
        return None
    maior = lista[0]
    for string in lista:
        if len(string) > len(maior):
            maior = string
    return maior

# 38. Escreva uma função que calcule a distância entre dois pontos (x1, y1) e (x2, y2).
import math
def distancia_pontos(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 39. Crie uma função que receba o valor de uma compra e retorne o valor com 10% de desconto.
def calcular_desconto(valor):
    desconto = valor * 0.10
    return valor - desconto

# 40. Crie uma função que calcule juros compostos: montante = capital * (1 + taxa) ** tempo.
def juros_compostos(capital, taxa, tempo):
    return capital * (1 + taxa) ** tempo

# 41. Crie uma função decoradora que registre o tempo de execução de outra função.
import time
def decorador_tempo(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

# 42. Crie uma função que retorne uma função interna (closure) que acumula valores.
def acumulador():
    total = 0
    def adicionar(valor):
        nonlocal total
        total += valor
        return total
    return adicionar

# 43. Crie uma função que receba um CPF em formato string e valide-o.
def validar_cpf(cpf):
    cpf = ''.join(c for c in cpf if c.isdigit())
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = (soma * 10) % 11
    digito1 = digito1 if digito1 < 10 else 0
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = (soma * 10) % 11
    digito2 = digito2 if digito2 < 10 else 0
    return cpf[-2:] == f"{digito1}{digito2}"

# 44. Escreva uma função que leia um arquivo texto e conte quantas palavras ele possui.
def contar_palavras_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            palavras = conteudo.split()
            return len(palavras)
    except FileNotFoundError:
        return "Arquivo não encontrado."

# 45. Crie uma função que use filter() e lambda para filtrar números maiores que 10 de uma lista.
def filtrar_maiores_que_dez(lista):
    return list(filter(lambda x: x > 10, lista))

# 46. Escreva uma função que utilize zip para unir duas listas em um dicionário.
def unir_listas_em_dicionario(lista1, lista2):
    return dict(zip(lista1, lista2))

# 47. Escreva uma função que leia uma matriz (lista de listas) e retorne sua transposta.
def transposta(matriz):
    return [list(linha) for linha in zip(*matriz)]

# 48.Crie uma função que gere senhas seguras com letras, números e símbolos (use random.choice).
import random
def gerar_senha(tamanho=12):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# 49. Crie uma função que detecte anagramas entre duas palavras.
def sao_anagramas(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)

# 50. Crie uma função que verifique se uma Sudoku 9x9 está corretamente preenchida (sem números repetidos por linha, coluna e região 3x3).
def validar_sudoku(tabuleiro):
    for linha in tabuleiro:
        if tem_repeticao(linha):
            return False
    for coluna in zip(*tabuleiro):
        if tem_repeticao(coluna):
            return False
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            bloco = [tabuleiro[x][y] for x in range(i, i+3) 
                                for y in range(j, j+3)]
            if tem_repeticao(bloco):
                return False
    return True

