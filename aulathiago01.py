
dia = input("Digite o dia da semana: ")

if dia == "Quarta":
    print("Assitir jogo do SPFC")
else:
    print("Estudar!!")


letra = input("digite uma letra:").upper() #upper() deixa a letra maiuscula

if letra == "S":
    print("SIM")


nome = input("Digite seu nome: ")
genero = input("Digite seu genero: ").upper()
idade = int(input("Digite sua idade: "))

if idade >= 17:
    if genero == "M":
        print("Obrugatório o alistamento militar")
    else:
        print("Não é obrigatório se alistar")
else:
    print("Calma, Jovem Gafanhoto!")





