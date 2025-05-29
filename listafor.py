#1
for num in range(1, 51):
    if num % 2 != 0:
        print(num)

#2
times = ["Palmeiras", "Flamengo", "São Paulo"]
for i in range(len(times)):
    print(f"{i + 1} - {times[i]}")

#3
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
for num in range(min(num1, num2) + 1, max(num1, num2)):
    print(num)

#4
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = 0
for num in range(min(num1, num2) + 1, max(num1, num2)):
    soma += num
print(f"Soma: {soma}")

#5
# Vertical
for num in range(1, 21):
    print(num)

# Horizontal
for num in range(1, 21):
    print(num, end=" ")
print()

#6
soma = 0
for i in range(5):
    num = float(input(f"Digite o {i + 1}º número: "))
    soma += num
print(f"Soma: {soma}")
print(f"Média: {soma / 5}")

#7
n = int(input("Quantos números? "))
menor = float("inf")
maior = float("-inf")
soma = 0
for i in range(n):
    num = float(input(f"Digite o {i + 1}º número: "))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    soma += num
print(f"Menor: {menor}")
print(f"Maior: {maior}")
print(f"Soma: {soma}")

#8
n = int(input("Quantas pessoas? "))
soma = 0
for i in range(n):
    idade = int(input(f"Idade da {i + 1}ª pessoa: "))
    soma += idade
media = soma / n
print(f"Média: {media:.1f}")
if media <= 25:
    print("Turma jovem")
elif media <= 60:
    print("Turma adulta")
else:
    print("Turma idosa")

#9
candidatos = {"Candidato 1": 0, "Candidato 2": 0, "Candidato 3": 0}
eleitores = int(input("Total de eleitores: "))
for i in range(eleitores):
    print(f"Eleitor {i + 1}:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    voto = input("Digite o número do candidato: ")
    if voto == "1":
        candidatos["Candidato 1"] += 1
    elif voto == "2":
        candidatos["Candidato 2"] += 1
    elif voto == "3":
        candidatos["Candidato 3"] += 1
print("\nResultado da Eleição:")
print(f"Candidato 1: {candidatos['Candidato 1']} votos")
print(f"Candidato 2: {candidatos['Candidato 2']} votos")
print(f"Candidato 3: {candidatos['Candidato 3']} votos")
vencedor = "Candidato 1"
maior_votos = candidatos["Candidato 1"]
if candidatos["Candidato 2"] > maior_votos:
    vencedor = "Candidato 2"
    maior_votos = candidatos["Candidato 2"]
if candidatos["Candidato 3"] > maior_votos:
    vencedor = "Candidato 3"
print(f"\nCandidato campeão: {vencedor}")

#10
print("Lojas Quase Dois - Tabela de preços")
for i in range(1, 51):
    print(f"{i} - R$ {1.99 * i:.2f}")

#11
preco = float(input("Preço do pão: R$ "))
print("Panificadora Pão de Ontem - Tabela de preços")
for i in range(1, 51):
    print(f"{i} - R$ {preco * i:.2f}")

#12
maior_acidentes = -1
menor_acidentes = float("inf")
cidade_maior = ""
cidade_menor = ""
total_veiculos = 0
total_cid_menos2000 = 0
soma_acidentes_menos2000 = 0
quant_cid_menos2000 = 0
for i in range(5):
    print(f"\nCidade {i+1}:")
    codigo = input("Código da cidade: ")
    veiculos = int(input("Número de veículos de passeio: "))
    acidentes = int(input("Número de acidentes com vítimas: "))
    if acidentes > maior_acidentes:
        maior_acidentes = acidentes
        cidade_maior = codigo
    if acidentes < menor_acidentes:
        menor_acidentes = acidentes
        cidade_menor = codigo
        total_veiculos += veiculos
        if veiculos < 2000:
            soma_acidentes_menos2000 += acidentes
            quant_cid_menos2000 += 1
media_veiculos = total_veiculos / 5
if quant_cid_menos2000 > 0:
    media_acidentes_menos2000 = soma_acidentes_menos2000 / quant_cid_menos2000
else:
    media_acidentes_menos2000 = 0
print("\nResultados:")
print(f"Maior índice de acidentes: Cidade {cidade_maior} com {maior_acidentes} acidentes")
print(f"Menor índice de acidentes: Cidade {cidade_menor} com {menor_acidentes} acidentes")
print(f"Média de veículos nas 5 cidades: {media_veiculos:.2f}")
if quant_cid_menos2000 > 0:
    print(f"Média de acidentes em cidades com <2000 veículos: {media_acidentes_menos2000:.2f}")
else:
    print("Não há cidades com menos de 2000 veículos para calcular a média de acidentes")

#13
pares = impares = 0
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Pares: {pares}, Ímpares: {impares}")

#14
temperaturas = []
while True:
    entrada = input("Digite a temperatura (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        break
    temp = float(entrada)
    mes = input("Digite o mês: ")
    ano = input("Digite o ano: ")
    temperaturas.append({"temp": temp, "mes": mes, "ano": ano})
if temperaturas:
    menor_temp = temperaturas[0]["temp"]
    maior_temp = temperaturas[0]["temp"]
    mes_menor = temperaturas[0]["mes"]
    ano_menor = temperaturas[0]["ano"]
    mes_maior = temperaturas[0]["mes"]
    ano_maior = temperaturas[0]["ano"]
    total_temp = 0
    quantidade = 0
    for registro in temperaturas:
        if registro["temp"] < menor_temp:
            menor_temp = registro["temp"]
            mes_menor = registro["mes"]
            ano_menor = registro["ano"]
        if registro["temp"] > maior_temp:
            maior_temp = registro["temp"]
            mes_maior = registro["mes"]
            ano_maior = registro["ano"]
            total_temp += registro["temp"]
        quantidade += 1
    media = total_temp / quantidade
    print("\nResultados:")
    print(f"Menor temperatura: {menor_temp}°C (em {mes_menor}/{ano_menor})")
    print(f"Maior temperatura: {maior_temp}°C (em {mes_maior}/{ano_maior})")
    print(f"Média das temperaturas: {media:.2f}°C")
else:
    print("Nenhuma temperatura foi registrada.")

#15
n = int(input("Número: "))
fatorial = 1
for i in range(n, 0, -1):
    fatorial *= i
print(f"{n}! = {fatorial}")

#16
n = int(input("Quantos termos da sequência Fibonacci você quer? "))
a, b = 1, 1
print("Sequência Fibonacci:")
print(a, end=" ")
print(b, end=" ")
for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c