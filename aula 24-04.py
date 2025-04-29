# while True:
#     print("Loop Infinito \n")

# while True:
#     valor = int(input("Digite 1 ou 0 para fim: "))
#     if valor == 1:
#         print("Valor Correto")
#     else:
#         print("Valor para sair")
#         break

# while True:
#     valor = int(input("Digite o valor 1 ou 0 para encerrar: "))
#     if valor <= 1:
#         continue
#         print("Maior que um")
#     if valor > 1:
#         print("Maior que um")

# n = int(input("Digite um número: "))
# contador = 0
# if n > 0:
#     while n > 0:
#         n = n -1
#         contador = contador + 1
#     print("O número pode ser reduzido a zero em", contador, "passos.")
# elif n < 0:
#     print("O número é menor que 0")
# else:
#     print("O número é zero.")

# while True:
#     print("Escolha sua operação matemática:")
#     print("A para adição")
#     print("S para subtração")
#     print("M para multiplicação")
#     print("D para divisão")
#     print("X para encerrar")
#     op = input("Digite a letra para sua operação: ").upper()
#     if op == "X":
#         print("Calculadora encerrada.")
#         break
#     if op == "A":
#         print("Operação escolhida foi adição.")
#         n1 = int(input("Digite o primeiro número: "))
#         n2 = int(input("Digite o segundo número: "))
#         resultado = n1 + n2
#         print(n1, "+", n2, "=" , resultado)
#         break
#     elif op == "S":
#         print("Operação escolhida foi subtração.")
#         n1 = int(input("Digite o primeiro número: "))
#         n2 = int(input("Digite o segundo número: "))
#         resultado = n1 - n2
#         print(n1, "-", n2, "=" , resultado)
#         break
#     elif op == "M":
#         print("Operação escolhida foi multiplicação.")
#         n1 = int(input("Digite o primeiro número: "))
#         n2 = int(input("Digite o segundo número: "))
#         resultado = n1 * n2
#         print(n1, "*", n2, "=" , resultado)
#         break
#     elif op == "D":
#         print("Operação escolhida foi divisão.")
#         n1 = int(input("Digite o primeiro número: "))
#         n2 = int(input("Digite o segundo número: "))
#         resultado = n1 / n2
#         print(n1, "/", n2, "=" , resultado)
#         break

# while True:
#     n = float(input("Digite uma nota entre zero e 10: "))
#     if n < 0 or n > 10:
#         print("Nota inválida")
#     else:
#         break

# while True:
#     nome = input("Digite o nome do usuário: ").upper()
#     senha = input("Escolha uma senha de quatro dígitos: ").upper()
#     if sorted(senha) == sorted(nome):
#         print("Erro! A senha não pode ser o nome de usuário.")
#     else:
#         print("Cadastro realizado com sucesso!")
#         break   

while True:
    while True:
        nm = input("Digite seu nome: ").upper()
        if len(nm) < 3:
            print("Erro! O nome deve ter mais de 3 caracteres.")
        else:
            break
    while True:    
        id = int(input("Digite sua idade: "))
        if id < 0 or id > 150:
            print("Erro! A idade deve ser válida.")
        else:
            break
    while True: 
        sal = float(input("Digite seu salário: R$"))
        if sal <= 0:
            print("Erro! Salário deve ser válido.")
        else:
            break
    while True:
        sex = input("Digite seu sexo: M(masculino), F(feminino), O(outro): ").upper()
        if sex != ("F").upper() and sex != ("M").upper() and sex != ("O").upper():
            print("Erro! Sexo deve ser válido.")
        else:
            break
    while True:
        estcv = input("Digite seu estado civil: S(solteiro), C(casado), V(viúvo), D (divorciado): ").upper()
        if estcv != ("S").upper() and estcv != ("C").upper() and estcv != ("V").upper() and estcv != ("D").upper():
            print("Erro! Estado Civil deve ser válido.")
        else:
             print("Cadastro efetuado com sucesso.")
        break
    break



    


    