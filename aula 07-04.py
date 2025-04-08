idade = 18
if idade < 20: #dois pontos para dar os espaços (identação) 4 espaços.
    print("Você é jovem!")

Age = 18
if(Age > 17):
    print("Você é maior, já pode dirigir")
print("Fim. Fora do if")

idade = int(input("Digite sua idade: "))
if idade >= 18: #caso verdadeiro
    print("Maior de idade")
else: #caso falso
    print("Menor de idade")

idade = int(input("Digite sua idade: "))
if idade >=16 and idade < 18:
    print("Pode votar")
elif idade < 16: #if else (se senão em portugol) na mesma linha
    print("Apenas estude")
else:
    print("Pode dirigir")

