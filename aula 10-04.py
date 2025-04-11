sexo = str(input("Sexo: ")).upper()
if sexo == "F":
    print("Feminino")
elif sexo == "M":
    print("Masculino")
elif sexo == "O":
    print("Outros")
else:
    print("Inválido")

letra = input("Digite uma letra: ").upper()
if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print("Vogal")
else:
    print("Consoante")

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num3 and num2 > num1:
    print(num2)
elif num3 > num1 and num3 > num2:
    print(num3)
if num1 < num2 and num1 < num3:
    print(num1)
elif num2 < num3 and num2 < num1:
    print(num2)
elif num3 < num1 and num3 < num2:
    print(num3)
else:
    print("Números iguais")

prod1 = float(input("Digite o valor do produto 1: "))
prod2 = float(input("Digite o valor do produto 2: "))
prod3 = float(input("Digite o valor do produto 3: "))
if prod1 < prod2 and prod1 < prod3:
    print("Produto1 é o mais barato: ", prod1)
elif prod2 < prod1 and prod2 < prod3:
    print("Produto 2 é o mais barato: ", prod2)
elif prod3 < prod1 and prod3 < prod2:
    print("Produto 3 é o mais barato: ", prod3)
else:
    print("Compre o que você gostou mais")

num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite mais um  número: "))
num_3 = int(input("Digite outro número: "))
if num_1 > num_2 and num_2 > num_3:
    print(num_1, ",", num_2, ",", num_3)
elif num_1 > num_3 and num_3 > num_2:
    print(num_1, ",", num_3, ",", num_2)
elif num_2 > num_1 and num_1 > num_3:
    print(num_2, ",", num_1, ",", num_3)
elif num_2 > num_3 and num_3 > num_1:
    print(num_2, ",", num_3, ",", num_1)
elif num_3 > num_1 and num_1 > num_2:
    print(num_3, ",", num_1, ",", num_2)
elif num_3 > num_2 and num_2 > num_1:
    print(num_3, ",", num_2, ",", num_1)

salarioatual = float(input("Digite o salário atual: "))
if salarioatual <= 280.55:
    porcent = "22.51%"
    reajuste = salarioatual*(22.51/100)
elif salarioatual >= 280.56 and salarioatual <= 709.72:
    porcent = "15.39%"
    reajuste = salarioatual*(15.39/100)
elif salarioatual >= 709.73 and salarioatual <= 1501.33:
    porcent = "10.97%"
    reajuste = salarioatual*(10.97/100)
elif salarioatual >= 1501.34:
    porcent = "5.19%"
    reajuste = salarioatual*(5.19/100)
salariocorrigido = salarioatual + reajuste
print("Seu salário é: ", salarioatual)
print("O percentual de aumento aplicado foi", porcent)
print("A correção do seu salário é de R$ %.2f"%reajuste)
print("Seu salário corrigido é R$ %.2f"%salariocorrigido)







   

    



