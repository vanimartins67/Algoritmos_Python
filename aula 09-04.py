number1 = (input("Digite um número: "))
number2 = (input("Digite outro número: "))
if number1 > number2:
   print(number1)
else:
   print(number2)

number = int(input("Digite um número: "))
if number > 0:
    print("Número positivo")
elif number < 0:
    print("Número negativo")
elif number == 0:
    print("Número neutro")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(media)
if media >= 7:
    print("Aprovado")
elif media < 7 and media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

salarioatual = float(input("Digite o salário atual: "))
print("Seu salário atual é R$", salarioatual)
if salarioatual < 500:
    reajuste = salarioatual*(15/100)
elif salarioatual >= 500 < 1000:
    reajuste = salarioatual*(10/100)
elif salarioatual > 1000:
    reajuste = salarioatual*(5/100)
salariocorrigido = salarioatual + reajuste
print("A correção do seu salário é R$", reajuste)
print("Seu salário corrigido é R$", salariocorrigido)


