#1 - Verifique se um número é positivo
num = int(input("Digite um número: "))
if num > 0:
    print("Positivo")
else:
    print("Não é positivo")

#2 - Verifique se um número é negativo
num = int(input("Digite um número: "))
if num < 0:
    print("Negativo")
else:
    print("Não é negativo")

#3 - Verifique se um número é zero
num = int(input("Digite um número: "))
if num == 0:
    print("Zero")
else:
    print("Não é zero")

#4 - Verifique se um número é par ou ímpar
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")

#5 - Verifique se um número é múltiplo de 5
num = int(input("Digite um número: "))
if num % 5 == 0:
    print("Múltiplo de 5")
else:
    print("Não é múltiplo de 5")

#6 - Verifique se um número é maior que 10
num = int(input("Digite um número: "))
if num > 10:
    print("Maior que 10")
else:
    print("Não é maior que 10")

#7 - Verifique se um número é menor que 100
num = int(input("Digite um número: "))
if num < 100:
    print("Menor que 100")
else:
    print("Não é menor que 100")

#8 - Verifique se um número é maior ou igual a 20
num = int(input("Digite um número: "))
if num >= 20:
    print("Maior ou igual a 20")
else:
    print("Menor que 20")

#9 - Verifique se um número é menor ou igual a 50
num = int(input("Digite um número: "))
if num <= 50:
    print("Menor ou igual a 50")
else:
    print("Maior que 50")

#10 - Verifique se um número está entre 10 e 20
num = int(input("Digite um número: "))
if 10 < num < 20:
    print("Está entre 10 e 20")
else:
    print("Não está entre 10 e 20")

#11 - Verifique se um número é divisível por 3
num = int(input("Digite um número: "))
if num % 3 == 0:
    print("Divisível por 3")
else:
    print("Não é divisível por 3")

#12 - Verifique se um número é divisível por 2 ou 3
num = int(input("Digite um número: "))
if num % 2 == 0 or num % 3 == 0:
    print("Divisível por 2 ou 3")
else:
    print("Não é divisível por 2 ou 3")

#13 - Verifique se um número é positivo e maior que 100
num = int(input("Digite um número: "))
if num > 0 and num > 100:
    print("Positivo e maior que 100")
else:
    print("Não atende aos critérios")

#14 - Verifique se um número é negativo ou menor que -10
num = int(input("Digite um número: "))
if num < 0 or num < -10:
    print("Negativo ou menor que -10")
else:
    print("Não atende aos critérios")

#15 - Verifique se um número é múltiplo de 2 e 3
num = int(input("Digite um número: "))
if num % 2 == 0 and num % 3 == 0:
    print("Múltiplo de 2 e 3")
else:
    print("Não é múltiplo de 2 e 3")

#16 - Verifique se um número é maior que 0 e menor que 100
num = int(input("Digite um número: "))
if 0 < num < 100:
    print("Maior que 0 e menor que 100")
else:
    print("Não atende aos critérios")

#17 - Verifique se um número é menor ou igual a 0
num = int(input("Digite um número: "))
if num <= 0:
    print("Menor ou igual a 0")
else:
    print("Maior que 0")

#18 - Verifique se a idade permite votar (maior de 18 anos)
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Pode votar")
else:
    print("Não pode votar")

#19 - Verifique se a idade permite dirigir (maior de 18 anos)
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Pode dirigir")
else:
    print("Não pode dirigir")

#20 - Verifique se a idade permite beber legalmente (maior de 21 anos)
idade = int(input("Digite sua idade: "))
if idade >= 21:
    print("Pode beber legalmente")
else:
    print("Não pode beber legalmente")

#21 - Verifique se um número é maior que 0 e par
num = int(input("Digite um número: "))
if num > 0 and num % 2 == 0:
    print("Maior que 0 e par")
else:
    print("Não atende aos critérios")

#22 - Verifique se um número é negativo e ímpar
num = int(input("Digite um número: "))
if num < 0 and num % 2 != 0:
    print("Negativo e ímpar")
else:
    print("Não atende aos critérios")

#23 - Verifique se a soma de dois números é maior que 50
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 + n2 > 50:
    print("Soma maior que 50")
else:
    print("Soma não é maior que 50")

#24 - Verifique se a soma de dois números é igual a 100
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 + n2 == 100:
    print("Soma igual a 100")
else:
    print("Soma diferente de 100")

#25 - Verifique se um número é menor que 10 ou maior que 100
num = int(input("Digite um número: "))
if num < 10 or num > 100:
    print("Menor que 10 ou maior que 100")
else:
    print("Não atende aos critérios")

#26 - Verifique se um número é maior que 0, mas não é múltiplo de 5
num = int(input("Digite um número: "))
if num > 0 and num % 5 != 0:
    print("Maior que 0 e não é múltiplo de 5")
else:
    print("Não atende aos critérios")

#27 - Verifique se a idade é menor que 18 ou maior que 65
idade = int(input("Digite sua idade: "))
if idade < 18 or idade > 65:
    print("Menor que 18 ou maior que 65")
else:
    print("Entre 18 e 65 anos")

#28 - Verifique se uma pessoa é adulta (18-64 anos)
idade = int(input("Digite sua idade: "))
if 18 <= idade <= 64:
    print("Adulto")
else:
    print("Não é adulto")

#29 - Verifique se a pessoa tem mais de 60 anos ou é menor que 18 anos
idade = int(input("Digite sua idade: "))
if idade > 60 or idade < 18:
    print("Mais de 60 ou menor que 18")
else:
    print("Entre 18 e 60 anos")

#30 - Verifique se uma pessoa é idosa (maior que 60 anos)
idade = int(input("Digite sua idade: "))
if idade > 60:
    print("Idoso")
else:
    print("Não é idoso")

#31 - Verifique se um número é negativo ou zero
num = int(input("Digite um número: "))
if num <= 0:
    print("Negativo ou zero")
else:
    print("Positivo")

#32 - Verifique se a média de três números é maior que 50
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
media = (n1 + n2 + n3) / 3
if media > 50:
    print("Média maior que 50")
else:
    print("Média não é maior que 50")

#33 - Verifique se a média de três números é menor que 20
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
media = (n1 + n2 + n3) / 3
if media < 20:
    print("Média menor que 20")
else:
    print("Média não é menor que 20")

#34 - Verifique se a soma de três números é maior que 100
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 + n2 + n3 > 100:
    print("Soma maior que 100")
else:
    print("Soma não é maior que 100")

#35 - Verifique se a soma de três números é menor que 50
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 + n2 + n3 < 50:
    print("Soma menor que 50")
else:
    print("Soma não é menor que 50")

#36 - Verifique se a multiplicação de dois números é maior que 100
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 * n2 > 100:
    print("Multiplicação maior que 100")
else:
    print("Multiplicação não é maior que 100")

#37 - Verifique se a multiplicação de dois números é menor que 100
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 * n2 < 100:
    print("Multiplicação menor que 100")
else:
    print("Multiplicação não é menor que 100")

#38 - Verifique se um número é múltiplo de 10
num = int(input("Digite um número: "))
if num % 10 == 0:
    print("Múltiplo de 10")
else:
    print("Não é múltiplo de 10")

#39 - Verifique se a diferença entre dois números é maior que 20
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if abs(n1 - n2) > 20:
    print("Diferença maior que 20")
else:
    print("Diferença não é maior que 20")

#40 - Verifique se a diferença entre dois números é menor que 10
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if abs(n1 - n2) < 10:
    print("Diferença menor que 10")
else:
    print("Diferença não é menor que 10")

#41 - Verifique se um número é menor que 10 e maior que 0
num = int(input("Digite um número: "))
if 0 < num < 10:
    print("Entre 0 e 10")
else:
    print("Não está entre 0 e 10")

#42 - Verifique se a idade está entre 16 e 21 anos
idade = int(input("Digite sua idade: "))
if 16 <= idade <= 21:
    print("Idade entre 16 e 21 anos")
else:
    print("Idade fora do intervalo")

#43 - Verifique se um número é menor que 100 e maior que 50
num = int(input("Digite um número: "))
if 50 < num < 100:
    print("Entre 50 e 100")
else:
    print("Não está entre 50 e 100")

#44 - Verifique se um número é maior que 100 e menor que 200
num = int(input("Digite um número: "))
if 100 < num < 200:
    print("Entre 100 e 200")
else:
    print("Não está entre 100 e 200")

#45 - Verifique se um número é menor que 1000 e maior que 500
num = int(input("Digite um número: "))
if 500 < num < 1000:
    print("Entre 500 e 1000")
else:
    print("Não está entre 500 e 1000")

#46 - Verifique se um número é múltiplo de 4
num = int(input("Digite um número: "))
if num % 4 == 0:
    print("Múltiplo de 4")
else:
    print("Não é múltiplo de 4")

#47 - Verifique se um número é múltiplo de 7
num = int(input("Digite um número: "))
if num % 7 == 0:
    print("Múltiplo de 7")
else:
    print("Não é múltiplo de 7")

#48 - Verifique se um número é múltiplo de 2 e 5
num = int(input("Digite um número: "))
if num % 2 == 0 and num % 5 == 0:
    print("Múltiplo de 2 e 5")
else:
    print("Não é múltiplo de 2 e 5")

#49 - Verifique se um número é maior que 100 e múltiplo de 3
num = int(input("Digite um número: "))
if num > 100 and num % 3 == 0:
    print("Maior que 100 e múltiplo de 3")
else:
    print("Não atende aos critérios")

#50 - Verifique se a soma de dois números é menor que 20 e maior que 10
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
if 10 < soma < 20:
    print("Soma entre 10 e 20")
else:
    print("Soma fora do intervalo")

#51 - Verifique se um número é maior que 50, mas menor que 60
num = int(input("Digite um número: "))
if 50 < num < 60:
    print("Entre 50 e 60")
else:
    print("Não está entre 50 e 60")

#52 - Verifique se a idade é maior que 21 e menor que 30
idade = int(input("Digite sua idade: "))
if 21 < idade < 30:
    print("Entre 21 e 30 anos")
else:
    print("Fora do intervalo")

#53 - Verifique se a idade é maior que 30, mas menor que 40
idade = int(input("Digite sua idade: "))
if 30 < idade < 40:
    print("Entre 30 e 40 anos")
else:
    print("Fora do intervalo")

#54 - Verifique se um número é menor que 100 e par
num = int(input("Digite um número: "))
if num < 100 and num % 2 == 0:
    print("Menor que 100 e par")
else:
    print("Não atende aos critérios")

#55 - Verifique se um número é negativo e divisível por 5
num = int(input("Digite um número: "))
if num < 0 and num % 5 == 0:
    print("Negativo e divisível por 5")
else:
    print("Não atende aos critérios")

#56 - Verifique se um número é positivo, múltiplo de 3, mas não de 5
num = int(input("Digite um número: "))
if num > 0 and num % 3 == 0 and num % 5 != 0:
    print("Positivo, múltiplo de 3 e não de 5")
else:
    print("Não atende aos critérios")

#57 - Verifique se a soma de dois números é igual a 20 ou maior que 50
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
if soma == 20 or soma > 50:
    print("Soma igual a 20 ou maior que 50")
else:
    print("Soma não atende aos critérios")

#58 - Verifique se a soma de dois números é menor que 10 ou maior que 100
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
if soma < 10 or soma > 100:
    print("Soma menor que 10 ou maior que 100")
else:
    print("Soma entre 10 e 100")

#59 - Verifique se um número é maior que 200 e menor que 500
num = int(input("Digite um número: "))
if 200 < num < 500:
    print("Entre 200 e 500")
else:
    print("Fora do intervalo")

#60 - Verifique se um número é menor que 10 ou maior que 200
num = int(input("Digite um número: "))
if num < 10 or num > 200:
    print("Menor que 10 ou maior que 200")
else:
    print("Entre 10 e 200")

#61 - Verifique se a média de dois números é maior que 50
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
media = (n1 + n2) / 2
if media > 50:
    print("Média maior que 50")
else:
    print("Média não é maior que 50")

#62 - Verifique se a média de dois números é menor que 30
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
media = (n1 + n2) / 2
if media < 30:
    print("Média menor que 30")
else:
    print("Média não é menor que 30")

#63 - Verifique se a multiplicação de dois números é maior que 500
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 * n2 > 500:
    print("Multiplicação maior que 500")
else:
    print("Multiplicação não é maior que 500")

#64 - Verifique se a multiplicação de dois números é menor que 1000
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 * n2 < 1000:
    print("Multiplicação menor que 1000")
else:
    print("Multiplicação não é menor que 1000")

#65 - Verifique se a soma de três números é maior que 500
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 + n2 + n3 > 500:
    print("Soma maior que 500")
else:
    print("Soma não é maior que 500")

#66 - Verifique se um número é maior que 50 e divisível por 4
num = int(input("Digite um número: "))
if num > 50 and num % 4 == 0:
    print("Maior que 50 e divisível por 4")
else:
    print("Não atende aos critérios")

#67 - Verifique se um número é divisível por 6 e maior que 100
num = int(input("Digite um número: "))
if num % 6 == 0 and num > 100:
    print("Divisível por 6 e maior que 100")
else:
    print("Não atende aos critérios")

#68 - Verifique se um número é menor que 10 e divisível por 5
num = int(input("Digite um número: "))
if num < 10 and num % 5 == 0:
    print("Menor que 10 e divisível por 5")
else:
    print("Não atende aos critérios")

#69 - Verifique se um número é maior que 50 e divisível por 3
num = int(input("Digite um número: "))
if num > 50 and num % 3 == 0:
    print("Maior que 50 e divisível por 3")
else:
    print("Não atende aos critérios")

#70 - Verifique se um número é maior que 0 e múltiplo de 9
num = int(input("Digite um número: "))
if num > 0 and num % 9 == 0:
    print("Maior que 0 e múltiplo de 9")
else:
    print("Não atende aos critérios")

#71 - Verifique se um número é maior que 50, mas não é múltiplo de 5
num = int(input("Digite um número: "))
if num > 50 and num % 5 != 0:
    print("Maior que 50 e não é múltiplo de 5")
else:
    print("Não atende aos critérios")

#72 - Verifique se a soma de três números é menor que 100
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 + n2 + n3 < 100:
    print("Soma menor que 100")
else:
    print("Soma não é menor que 100")

#73 - Verifique se a soma de três números é maior que 200
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 + n2 + n3 > 200:
    print("Soma maior que 200")
else:
    print("Soma não é maior que 200")

#74 - Verifique se a média de três números é maior que 40
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
media = (n1 + n2 + n3) / 3
if media > 40:
    print("Média maior que 40")
else:
    print("Média não é maior que 40")

#75 - Verifique se a média de três números é menor que 25
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
media = (n1 + n2 + n3) / 3
if media < 25:
    print("Média menor que 25")
else:
    print("Média não é menor que 25")

#76 - Verifique se um número é múltiplo de 5 e 7
num = int(input("Digite um número: "))
if num % 5 == 0 and num % 7 == 0:
    print("Múltiplo de 5 e 7")
else:
    print("Não é múltiplo de 5 e 7")

#77 - Verifique se um número é múltiplo de 3 ou 5, mas não de 7
num = int(input("Digite um número: "))
if (num % 3 == 0 or num % 5 == 0) and num % 7 != 0:
    print("Múltiplo de 3 ou 5, mas não de 7")
else:
    print("Não atende aos critérios")

#78 - Verifique se a soma de três números é maior que 100 e menor que 200
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
soma = n1 + n2 + n3
if 100 < soma < 200:
    print("Soma entre 100 e 200")
else:
    print("Soma fora do intervalo")

#79 - Verifique se a soma de dois números é par
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if (n1 + n2) % 2 == 0:
    print("Soma par")
else:
    print("Soma ímpar")

#80 - Verifique se a soma de dois números é ímpar
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if (n1 + n2) % 2 != 0:
    print("Soma ímpar")
else:
    print("Soma par")

#81 - Verifique se a multiplicação de dois números é par
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if (n1 * n2) % 2 == 0:
    print("Multiplicação par")
else:
    print("Multiplicação ímpar")

#82 - Verifique se a multiplicação de dois números é ímpar
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if (n1 * n2) % 2 != 0:
    print("Multiplicação ímpar")
else:
    print("Multiplicação par")

#83 - Verifique se um número é maior que 100, mas menor que 200
num = int(input("Digite um número: "))
if 100 < num < 200:
    print("Entre 100 e 200")
else:
    print("Fora do intervalo")

#84 - Verifique se um número é maior que 10 e menor que 50
num = int(input("Digite um número: "))
if 10 < num < 50:
    print("Entre 10 e 50")
else:
    print("Fora do intervalo")

#85 - Verifique se a idade é maior que 18 e menor que 30 anos
idade = int(input("Digite sua idade: "))
if 18 < idade < 30:
    print("Entre 18 e 30 anos")
else:
    print("Fora do intervalo")

#86 - Verifique se a idade é maior que 30 e menor que 50 anos
idade = int(input("Digite sua idade: "))
if 30 < idade < 50:
    print("Entre 30 e 50 anos")
else:
    print("Fora do intervalo")

#87 - Verifique se a idade é maior que 50 e menor que 60 anos
idade = int(input("Digite sua idade: "))
if 50 < idade < 60:
    print("Entre 50 e 60 anos")
else:
    print("Fora do intervalo")

#88 - Verifique se a idade é maior que 60 anos
idade = int(input("Digite sua idade: "))
if idade > 60:
    print("Maior que 60 anos")
else:
    print("Não é maior que 60 anos")

#89 - Verifique se a idade é menor que 18 anos
idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Menor que 18 anos")
else:
    print("Não é menor que 18 anos")

#90 - Verifique se um número é divisível por 3 e 5
num = int(input("Digite um número: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisível por 3 e 5")
else:
    print("Não é divisível por 3 e 5")

#91 - Verifique se a soma de dois números é maior que 100 e múltiplo de 10
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
if soma > 100 and soma % 10 == 0:
    print("Soma maior que 100 e múltiplo de 10")
else:
    print("Não atende aos critérios")

#92 - Verifique se um número é maior que 10 e múltiplo de 4
num = int(input("Digite um número: "))
if num > 10 and num % 4 == 0:
    print("Maior que 10 e múltiplo de 4")
else:
    print("Não atende aos critérios")

#93 - Verifique se a soma de dois números é maior que 50 e múltiplo de 3
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
if soma > 50 and soma % 3 == 0:
    print("Soma maior que 50 e múltiplo de 3")
else:
    print("Não atende aos critérios")

#94 - Verifique se a média de dois números é maior que 100
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
media = (n1 + n2) / 2
if media > 100:
    print("Média maior que 100")
else:
    print("Média não é maior que 100")

#95 - Verifique se um número é menor que 10 ou maior que 1000
num = int(input("Digite um número: "))
if num < 10 or num > 1000:
    print("Menor que 10 ou maior que 1000")
else:
    print("Entre 10 e 1000")

#96 - Verifique se um número é divisível por 2, 3 e 5
num = int(input("Digite um número: "))
if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
    print("Divisível por 2, 3 e 5")
else:
    print("Não é divisível por 2, 3 e 5")

#97 - Verifique se um número é maior que 10 e divisível por 2
num = int(input("Digite um número: "))
if num > 10 and num % 2 == 0:
    print("Maior que 10 e divisível por 2")
else:
    print("Não atende aos critérios")

#98 - Verifique se a diferença entre dois números é maior que 50
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if abs(n1 - n2) > 50:
    print("Diferença maior que 50")
else:
    print("Diferença não é maior que 50")

#99 - Verifique se a diferença entre dois números é menor que 20
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if abs(n1 - n2) < 20:
    print("Diferença menor que 20")
else:
    print("Diferença não é menor que 20")

#100 - Verifique se a soma de dois números é igual a 0
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 + n2 == 0:
    print("Soma igual a 0")
else:
    print("Soma diferente de 0")