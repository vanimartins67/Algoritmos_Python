#Faça um algoritmo em linguagem Python que o nome,idade, sexo, e receba duas notas e calcule a média aritmética e mostre o resultado.

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
sexo = input("Digite o seu sexo: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("\nDados do usuário:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Sexo: {sexo}")
print(f"Média das notas: {media:.2f}")


#Faça um programa que receba uma temperatura e transforme de Fahrenheit para Celsius. A formula de conversão de Fahrenheit para Celsius é a seguinte: C = (5/9) * (F 32).

f = float(input("Digite a temperatura em Fahrenheit: "))
c = (5 / 9) * (f - 32)
print(f"A temperatura em Celsius é: {c:.2f}")


#Faça um programa que leia o nome de um produto, a quantidade comprada, o valor unitário e o percentual de desconto a ser aplicado para o pagamento. Imprima na tela o nome do produto e o valor total da venda.

produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade comprada: "))
valor = float(input("Digite o valor unitário: "))
desconto = float(input("Digite o percentual de desconto: "))
valor_sem_desconto = quantidade * valor
desconto = valor_sem_desconto * (desconto / 100)
valor_com_desconto = valor_sem_desconto - desconto
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Valor unitário: R$ {valor:.2f}")
print(f"Desconto: {desconto}%")
print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")


#Faça um programa que leia um valor em reais e calcule o valor equivalente em dólares. O usuário deve informar, além do valor em reais da compra, o valor da cotação do dólar.

reais = float(input("Digite o valor em reais: "))
cotacao = float(input("Digite a cotação do dólar: "))
dolar = reais / cotacao
print(f"\nValor em reais: R$ {reais:.2f}")
print(f"Cotação do dólar: R$ {cotacao:.2f}")
print(f"Valor equivalente em dólares: US$ {dolar:.2f}")


#Escrever um programa na linguagem Python que conte o número de palavras em um texto. Como entrada, um texto será digitado de forma interativa no teclado. Como saída será impresso o texto, bem como a quantidade de caracteres desse texto.

texto = input("Digite um texto: ")
palavras = len(texto.split())
caracteres = len(texto)
print(texto)
print(f"\nNúmero de palavras: {palavras}")
print(f"Número de caracteres: {caracteres}")


#Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
print(f"String 1: {string1}")
print(f"Comprimento: {len(string1)}")
print(f"String 2: {string2}")
print(f"Comprimento: {len(string2)}")


#Faça um programa que leia um nome e imprima as 4 primeiras letras do nome.

nome = input("Digite o seu nome: ")
print(f"4 primeiras letras do nome: {nome[:4]}")


#Faça um programa que leia um nome e imprima apenas a letra do primeiro nome em maiúsculo.

nome = input("Digite o seu nome: ")
print(f"Primeira letra do nome em maiúsculo: {nome[0].upper()}")


#Faça um programa que leia um nome e imprima o nome todo em maiúsculo.

nome = input("Digite o seu nome: ")
print(f"Nome em maiúsculo: {nome.upper()}")


#Faça um programa que leia um nome completo de uma pessoa e imprima do índice 0 ao índice 8 (inclusive).

nome = input("Digite o seu nome completo: ")
parte_do_nome = nome[0:9]
print(f"\nNome completo: {nome}")
print(f"Do índice 0 ao 8: {parte_do_nome}")

#Faça um programa que leia um nome completo de uma pessoa e imprima a frequência de ocorrência da letra a.

nome = input("Digite o seu nome completo: ")
print(f"Frequência de ocorrência da letra 'a': {nome.count('a')}")



#A empresa Umbrella Corporation está desenvolvendo seu sistema de cadastro de pacientes, e a primeira fase do projeto consiste um desenvolver um algoritmo que capte os dados de cadastro.
#Tal cadastro solicitará os seguintes dados: (nome, cpf, rg, data de nascimento, sexo, peso, tipo sanguíneo, renda, endereço, telefone, cidade e estado)
#Após capturar todos os dados, imprimir em forma de relatório.

nome = input("Digite o seu nome: ")
cpf = input("Digite o seu CPF: ")
rg = input("Digite o seu RG: ")
data_nascimento = input("Digite a sua data de nascimento: ")
sexo = input("Digite o seu sexo: ")
peso = float(input("Digite o seu peso: "))
tipo_sanguineo = input("Digite o seu tipo sanguíneo: ")
renda = float(input("Digite a sua renda: "))
endereco = input("Digite o seu endereço: ")
telefone = input("Digite o seu telefone: ")
cidade = input("Digite a sua cidade: ")
estado = input("Digite o seu estado: ")
print("\nRelatório de cadastro:")
print(f"Nome: {nome}")
print(f"CPF: {cpf}")
print(f"RG: {rg}")
print(f"Data de nascimento: {data_nascimento}")
print(f"Sexo: {sexo}")
print(f"Peso: {peso} kg")
print(f"Tipo Sanguíneo: {tipo_sanguineo}")
print(f"Renda: R$ {renda}")
print(f"Endereço: {endereco}")
print(f"Telefone: {telefone}")
print(f"Cidade: {cidade}")
print(f"Estado: {estado}")




