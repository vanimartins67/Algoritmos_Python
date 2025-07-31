clientes = []
passagens = []
avioes = []
tripulacao = []

while True:
    print("\n--- SISTEMA DE VENDAS AÉREAS ---")
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Passagem")
    print("3 - Cadastrar Avião")
    print("4 - Cadastrar Tripulação")
    print("5 - Relatórios")
    print("6 - Sair")

    opcao = input("\nDigite a opção: ")

    if opcao == "1":
        print("\nCadastro de Cliente:")
        try:
            novo_cliente = {
                "nome": input("Nome: "),
                "sobrenome": input("Sobrenome: "),
                "rg": input("RG: "),
                "cpf": input("CPF: "),
                "endereco": input("Endereço: "),
                "fone": input("Telefone: "),
                "idade": int(input("Idade: "))
            }
            clientes.append(novo_cliente)
            print("Cliente Cadastrado!")
        except:
            print("Erro: Idade deve ser número!")

    elif opcao == "2":
        print("\nCadastro de Passagem:")
        try:
            nova_passagem = {
                "destino": input("Destino: "),
                "origem": input("Origem: "),
                "duracao": input("Duração: "),
                "valor": float(input("Valor: ")),
                "desconto": 0.05
            }
            nova_passagem["valor_final"] = nova_passagem["valor"] * 0.95
            passagens.append(nova_passagem)
            print("Passagem Cadastrada!")
        except:
            print("Erro: valor deve ser número!")

    elif opcao == "3":
        print("\nCadastro de Avião:")
        try:
            novo_aviao = {
                "modelo": input("Modelo: "),
                "ano": int(input("Ano: ")),
                "horas_voo": float(input("Horas de Voo: ")),
                "cor": input("Cor: "),
                "passageiros": int(input("Passageiros: "))
            }
            avioes.append(novo_aviao)
            print("Avião Cadastrado!")
        except:
            print("Erro: Dados numéricos inválidos")

    elif opcao == "4":
        print("\nCadastro de Tripulante:")
        try:
            novo_tripulante = {
                "nome": input("Nome: "),
                "cargo": input("Cargo: "),
                "idade": int(input("Idade: ")),
                "admissao": input("Admissão (dd/mm/aaaa): "),
                "fone": input("Telefone: ")
            }
            tripulacao.append(novo_tripulante)
            print("Tripulante Cadastrado!")
        except:
            print("Erro: Idade deve ser número")

    elif opcao == "5":
        while True:
            print("\nRelatórios:")
            print("1. Clientes")
            print("2. Passagens")
            print("3. Aviões")
            print("4. Tripulantes")
            print("5. Voltar")

            sub_opcao = input("\nDigite a opção: ")

            if sub_opcao == "1":
                print("\nClientes Cadastrados:")
                i = 1
                for c in clientes:
                    print(f"\ncliente {i}:")
                    for k, v in c.items():
                        print(f"{k}: {v}")
                    i += 1

            elif sub_opcao == "2":
                print("\nPassagens Vendidas:")
                i = 1
                for p in passagens:
                    print(f"\npassagem {i}:")
                    print(f"de {p['origem']} para {p['destino']}")
                    print(f"duracao: {p['duracao']}")
                    print(f"valor: {p['valor']:.2f}")
                    print(f"desconto: 5%")
                    print(f"total: {p['valor_final']:.2f}")
                    i += 1

            elif sub_opcao == "3":
                print("\nAviões Cadastrados:")
                i = 1
                for a in avioes:
                    print(f"\naviao {i}:")
                    for k, v in a.items():
                        print(f"{k}: {v}")
                    i += 1

            elif sub_opcao == "4":
                print("\nTripulantes Cadastrados:")
                i = 1
                for t in tripulacao:
                    print(f"\ntripulante {i}:")
                    for k, v in t.items():
                        print(f"{k}: {v}")
                    i += 1

            elif sub_opcao == "5":
                break

            else:
                print("Opção inválida!")

    elif opcao == "6":
        print("Saindo do Sistema...")
        break

    else:
        print("Opção inválida!")