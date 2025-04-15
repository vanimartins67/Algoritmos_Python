nota1 = float (input("Digite a primeira nota: "))
nota2 = float (input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("A Média é:", media)
if media < 7:
    print("Reprovado")
elif media >= 7 and media < 10:
    print("Aprovado")
elif media == 10:
    print("Aprovado com Distinção")


print("FOLHA DE PAGAMENTO")
valorhora = float(input("Digite o valor da hora trabalhada: "))
hora = float(input("Digite as horas trabalhadas: "))
salariobruto = valorhora * hora
print("Salário Bruto: R$", salariobruto)
if salariobruto >= 900 and salariobruto < 1500:
    ir = salariobruto * (5/100)
    print("IR   (5%)                : R$", ir)
elif salariobruto >= 1500 and salariobruto < 2500:
    ir = (10/100) * salariobruto
    print("IR   (10%)               : R$", ir)
elif salariobruto > 2500:
    ir = (20/100) * salariobruto
    print("IR   (20%)               : R$", ir)
else:
    ir = 0 * salariobruto
    print("IR   (ISENTO)            : R$", ir)
inss = (10/100) * salariobruto
print("INSS (10%)               : R$", inss)
fgts = (11/100) * salariobruto
print("FGTS (11%)               : R$", fgts)
descontos = inss + ir
print("Total de Descontos       : R$", descontos)
salarioliquido = salariobruto - descontos
print("Salário Líquido          : R$", salarioliquido)








