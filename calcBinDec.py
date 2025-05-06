valor = input("Digite o número em Binário: ")
valor_decimal = []

x = len(valor)
for i in valor:
    x = x - 1
    if i == "1":
        z = 2 ** x
        valor_decimal.append(z)

print(valor_decimal)
print("Dec ", sum(valor_decimal))
