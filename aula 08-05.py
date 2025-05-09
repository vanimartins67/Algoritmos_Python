for i in range(1,50,2):
    print(i)

times = ["Palmeiras", "Flamengo", "São Paulo"]
for t in range(len(times)):
    print(f"{t+1} - {times[t]}")

x = int(input("Digite um número: "))
y = int(input("Digite mais um número: "))
for i in range(x+1, y):
    print(i)

x = int(input("Digite um número: "))
y = int(input("Digite mais um número: "))
for i in range(x+1, y):
    soma = sum(range(x+1, y))
print(soma)

for i in range(1,21):
    print(i)

for i in range(1,21):
    print(i,end=" ")    

soma = 0
acumulador = 0
for i in range(5):
    num = int(input("Digite um número: "))
    soma = soma + num
    acumulador = acumulador + 1
media = soma / acumulador
print("Média = ", media)

soma  = 0
maior = -99999999999999
menor = 999999999999999
n = int(input("Digite quantos números serão utilizados: "))
for i in range(n):
    num = int(input("Digite o número: "))
    soma = soma + num
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
print("Maior: ", maior)
print("Menor: ", menor)
print("Soma: ", soma)

    



    
