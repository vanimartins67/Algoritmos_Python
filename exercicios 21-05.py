print("PASSAGENS AÉREAS")
print("----------------\n")
#Menu
while True:
    print("1 - Cadastros")
    print("2 - Relatórios")
    print("3 - Encerrar")
    try:
        menu = int(input("\nDigite a opção desejada: "))
    except ValueError:
        print("Digite apenas o número da opção correta.")
        continue
    
    if menu == 1:
        print("\n1 - Cadastro de Clientes")
        print("2 - Cadastro de Passagens")
        print("3 - Cadastro de Aviões")
        print("4 - Cadastro de Tripulação")
        try:
            menu2 = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("Digite apenas números.")
            continue
            
        if menu2 == 1:
            print("\nCADASTRO DE CLIENTES")
            nome = str(input("Nome: "))
            sobrenome = str(input("Sobrenome: "))
            try:
                rg = int(input("RG (somente números): "))
                cpf = int(input("CPF (somente números): "))
                idade = int(input("Idade: "))
                telefone = input("Telefone (com DDD): ")
            except ValueError:
                print("Digite apenas números.")
                continue
            endereco = input("Endereço: ")
            
        elif menu2 == 2:
            print("\nCADASTRO DE PASSAGENS")
            destino = input("Destino: ")
            origem = input("Origem: ")
            try:
                duracao = float(input("Duração do voo (em minutos): "))
                valorpass = float(input("Digite o valor da passagem: R$ "))
                desconto = valorpass * 0.05  # 5% de desconto
                print(f"Desconto à vista de 5%: R$ {desconto:.2f}")
            except ValueError:
                print("Digite valores numéricos válidos.")
                continue
                
        elif menu2 == 3:
            print("CADASTRO DA AERONAVE")
            modelo = input("Modelo: ")
            ano = int(input("Ano de fabricação: "))
            horas = input("Horas de voo: ")
            cor = input("Cor da aeronave: ")
            lotacao = int(input("Quantidade de passageiros: "))
        
    elif menu == 3:
        print("Encerrando o programa...")
        break










