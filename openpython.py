nomes = []
idades = []
sexos = []
cpfs = []
enderecos = []
cidades = []
estados = []

while True:
    print("\nMenu Principal")
    print("1. Cadastrar novo")
    print("2. Consultar")
    print("3. Sair")
    
    op = input("Opção: ")

    if op == "1":
        while True:
            print("\nNovo Cadastro")
            nomes.append(input("Nome: "))
            
            while True:
                try:
                    idades.append(int(input("Idade: ")))
                    break
                except:
                    print("Idade deve ser número")
            
            while True:
                s = input("Sexo (M/F): ").upper()
                if s == "M" or s == "F":
                    sexos.append(s)
                    break
                print("Digite M ou F")
            
            cpfs.append(input("CPF: "))
            enderecos.append(input("Endereço: "))
            cidades.append(input("Cidade: "))
            
            while True:
                e = input("Estado (sigla): ").upper()
                if len(e) == 2:
                    estados.append(e)
                    break
                print("Digite 2 letras")
            
            cont = input("\nCadastrar outro? (S/N): ").upper()
            if cont != "S":
                with open('cadastro.txt', 'w') as f:
                    for i in range(len(nomes)):
                        print(f"Nome: {nomes[i]}, Idade: {idades[i]}, Sexo: {sexos[i]}, "
                              f"CPF: {cpfs[i]}, Endereço: {enderecos[i]}, "
                              f"Cidade: {cidades[i]}, Estado: {estados[i]}", file=f)
                        print("-" * 80, file=f)
                print("Dados salvos!")
                break

    elif op == "2":
        while True:
            print("\nConsultar por:")
            print("1. Nome")
            print("2. CPF")
            print("3. Voltar")
            
            sub = input("Opção: ")
            
            if sub == "1":
                busca = input("\nNome: ").lower()
                achou = False
                for i in range(len(nomes)):
                    if busca in nomes[i].lower():
                        print(f"\nNome: {nomes[i]}")
                        print(f"Idade: {idades[i]}")
                        print(f"Sexo: {sexos[i]}")
                        print(f"CPF: {cpfs[i]}")
                        print(f"Endereço: {enderecos[i]}")
                        print(f"Cidade: {cidades[i]}")
                        print(f"Estado: {estados[i]}")
                        achou = True
                        break
                if not achou:
                    print("Não encontrado")
            
            elif sub == "2":
                busca = input("\nCPF: ")
                achou = False
                for i in range(len(cpfs)):
                    if busca == cpfs[i]:
                        print(f"\nNome: {nomes[i]}")
                        print(f"Idade: {idades[i]}")
                        print(f"Sexo: {sexos[i]}")
                        print(f"CPF: {cpfs[i]}")
                        print(f"Endereço: {enderecos[i]}")
                        print(f"Cidade: {cidades[i]}")
                        print(f"Estado: {estados[i]}")
                        achou = True
                        break
                if not achou:
                    print("Não encontrado")
            
            elif sub == "3":
                break
            
            else:
                print("Opção inválida")

    elif op == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida")