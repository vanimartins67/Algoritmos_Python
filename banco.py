clientes = []
while True:
    print("         Banco SENAC")
    print("== Cadastro de Novo Cliente ==")
    nome = str(input("Nome completo: "))
    cpf = input("CPF: ")
    rg = input("RG: ")
    telefone = input("Telefone: ")
    agencia = input("Número da agência: ")
    conta = input("Número da conta: ")
    saldo = float(input("Saldo inicial (R$): "))

    cliente = [nome, cpf, rg, telefone, agencia, conta, saldo]
    clientes.append(cliente)

    print("\nCliente cadastrado com sucesso")
    print("Nome:", cliente[0])
    print("CPF:", cliente[1])
    print("RG:", cliente[2])
    print("Telefone:", cliente[3])
    print("Agência:", cliente[4])
    print("Conta:", cliente[5])
    print("Saldo: R$", cliente[6])

    opcao = ""
    while opcao != "4":
        print("\n== Menu ==")
        print("1 - Ver Saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Sair")
        opcao = input('Escolha uma opção: ')
        if opcao == "1":
            print("Saldo atual: R$ ", cliente[6])
            
        elif opcao == "2":
            valor = float(input("Valor para depósito: "))
            if valor > 0:
                cliente[6] += valor
                print("Depósito realizado com sucesso.")
            else:
                print("Valor inválido.")
                
        elif opcao == "3":
            valor = float(input("Valor para saque: "))
            if valor > 0:
                if valor <= cliente[6]:
                    cliente[6] -= valor
                    print("Saque realizado com sucesso.")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Valor inválido.")
                
        elif opcao == "4":
            print("Sessão Encerrada.\n")
            break
        else:
            print("Opção inválida. Tente novamente.")