codigos = [10, 20, 30, 40, 50]
nomes = ["Caderno", "Caneta", "Lápis", "Borracha", "Régua"]
estoque = [0, 0, 0, 0, 0]
print("Digite a quantidade inicial em estoque de cada produto:")
estoque[0] = int(input(nomes[0] + " (" + str(codigos[0]) + "): "))
estoque[1] = int(input(nomes[1] + " (" + str(codigos[1]) + "): "))
estoque[2] = int(input(nomes[2] + " (" + str(codigos[2]) + "): "))
estoque[3] = int(input(nomes[3] + " (" + str(codigos[3]) + "): "))
estoque[4] = int(input(nomes[4] + " (" + str(codigos[4]) + "): "))

opcao = ""
while opcao != "X":
    print("\nEscolha a operação:")
    print("E - Entrada no estoque")
    print("S - Saída no estoque")
    print("R - Relatório")
    print("X - Sair")
    opcao = input("Opção: ").upper()
    if opcao == "E":
        cod = int(input("Digite o código do produto: "))
        i = 0
        while i < 5:
            if cod == codigos[i]:
                qtd = int(input("Quantidade a adicionar: "))
                estoque[i] = estoque[i] + qtd
                break
            i = i + 1
    elif opcao == "S":
        cod = int(input("Digite o código do produto: "))
        i = 0
        while i < 5:
            if cod == codigos[i]:
                qtd = int(input("Quantidade a retirar: "))
                if estoque[i] >= qtd:
                    estoque[i] = estoque[i] - qtd
                else:
                    print("Estoque insuficiente. Operação cancelada.")
                break
            i = i + 1
    elif opcao == "R":
        print("\nRelatório de Estoque:")
        i = 0
        while i < 5:
            print(nomes[i] + " (" + str(codigos[i]) + "): " + str(estoque[i]) + " unidades")
            i = i + 1
    elif opcao == "X":
        print("Programa Encerrado.")

