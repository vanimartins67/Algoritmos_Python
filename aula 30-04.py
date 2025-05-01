# Fulano = 0
# Sicrano = 0
# Beltrano = 0
# Cipriano = 0
# Nulo = 0
# Branco = 0 
# while True:
#     print("Escolha seu candidato:")
#     print("1 para Fulano")
#     print("2 para Sicrano")
#     print("3 para Beltrano")
#     print("4 para Cipriano")
#     print("5 para Voto Nulo")
#     print("6 para Voto em Branco")
#     voto = input("Digite seu voto: ")
#     if voto == "1":
#         Fulano = Fulano + 1
#         print("Você votou em Fulano.")
#     elif voto =="2":
#         Sicrano = Sicrano + 1
#         print("Você votou em Sicrano")
#     elif voto == "3":
#         Beltrano = Beltrano + 1  
#         print("Você votou em Beltrano")
#     elif voto == "4":
#         Cipriano = Cipriano + 1
#         print("Você votou em Cipriano")
#     elif voto == "5":
#         Nulo = Nulo + 1
#         print("Você votou Nulo")
#     elif voto == "6":
#         Branco = Branco + 1
#         print("Você votou em branco")
#     elif voto == "0":
#         print("Votação Terminada.")
#         break
#     else:
#         print("Digite um voto válido.")
# print("Resultado da Votação")
# print("Fulano:" , Fulano)
# print("Beltrano:" , Sicrano)
# print("Sicrano:" , Beltrano)
# print("Cipriano:" , Cipriano)
# print("Votos Nulos:" , Nulo)
# print("Votos em Branco:" , Branco)


Fulano = 0
Sicrano = 0
Beltrano = 0
Cipriano = 0
Nulo = 0
Branco = 0 
while True:
    print("Escolha seu candidato:")
    print("1 para Fulano")
    print("2 para Sicrano")
    print("3 para Beltrano")
    print("4 para Cipriano")
    voto = input("Digite seu voto: ")
    if voto == "1":
        Fulano = Fulano + 1
        print("Você votou em Fulano.")
    elif voto =="2":
        Sicrano = Sicrano + 1
        print("Você votou em Sicrano")
    elif voto == "3":
        Beltrano = Beltrano + 1  
        print("Você votou em Beltrano")
    elif voto == "4":
        Cipriano = Cipriano + 1
        print("Você votou em Cipriano")
    elif voto > "5":
        Nulo = Nulo + 1
        print("Você votou Nulo")
    elif voto == "":
        Branco = Branco + 1
        print("Você votou em branco")
    elif voto == "0":
        print("Votação Terminada.")
        break
print("Resultado da Votação")
print("Fulano:" , Fulano)
print("Sicrano:" , Sicrano)
print("Beltrano:" , Beltrano)
print("Cipriano:" , Cipriano)
print("Votos Nulos:" , Nulo)
print("Votos em Branco:" , Branco)
if Fulano > Beltrano and Fulano > Sicrano and Fulano > Cipriano:
    print("Fulano ganhou.")
elif Beltrano > Fulano and Beltrano > Sicrano and Beltrano > Cipriano:
    print("Beltrano ganhou.")
elif Sicrano > Fulano and Sicrano > Beltrano and Sicrano > Cipriano:
    print("Sicrano ganhou.")
elif Cipriano > Fulano and Cipriano > Beltrano and Cipriano > Sicrano:
    print("Cripriano ganhou.")
else:
    print("Empate entre os candidatos.")





