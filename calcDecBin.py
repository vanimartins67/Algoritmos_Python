import os

valor  = float(input("Digite um valor em decimal para converter em binário: "))
valor_binario = []
cont = 0

while valor > 0:
    cont += 1
    novovalor = valor % 2
    novovalor = int(novovalor)
    print("Resto: ", novovalor)
    valor = valor / 2
    print("Dividendo: ", valor)
    valor = int(valor)
    valor_binario.insert(0, novovalor)
    print("")
print(valor_binario)
print(valor)
print(cont)

output = "".join(map(str, valor_binario))
print(output)