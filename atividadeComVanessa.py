# cpf = []
# nome = []
# idade = []
# sexo = []
# endereco = []
# cidade = []
# estado = []
respostas = ["sim", "s", "desejo"]

while True:
    print("-----MENU-----")
    print("0 - Cadastro")
    print("1 - Relatorio")
    print("2 - Sair")
    try:
        acao = int(input("Informe a ação desejada: "))

        try:
            
            if acao == 0:
                while True:
                        
                    cpfCadastro = input("Informe o CPF: ")
                    nomeCadastro = input("informe o nome: ")
                    sexoCadastro = input("Informe o Sexo: ")
                    enderecoCadastro = input("Informe o endereço: ")
                    cidadeCadastro = input("Informe a cidade: ")
                    estadoCadastro = input("Informe o Estado: ")
                    idadeCadastro = int(input("Informe a Idade: "))

                    # try:
                    # except:
                    #     print("Informe uma idade valida: ")

                    # cpf.append(cpfCadastro)
                    # nome.append(nomeCadastro)
                    # idade.append(idadeCadastro)
                    # sexo.append(sexoCadastro)
                    # endereco.append(enderecoCadastro)
                    # cidade.append(cidadeCadastro)
                    # estado.append(estadoCadastro)

                    with open("cadastro.txt", "a") as cadastro:
                        cadastro.writelines("\n")
                        cadastro.writelines("Cpf: ")
                        cadastro.writelines(cpfCadastro)
                        cadastro.writelines("\n")
                        cadastro.writelines("Nome: ")
                        cadastro.writelines(nomeCadastro)
                        cadastro.writelines("\n")
                        cadastro.writelines("Sexo: ")
                        cadastro.writelines(sexoCadastro)
                        cadastro.writelines("\n")
                        cadastro.writelines("Endereco: ")
                        cadastro.writelines(enderecoCadastro)
                        cadastro.writelines("\n")
                        cadastro.writelines("Cidade: ")
                        cadastro.writelines(cidadeCadastro)
                        cadastro.writelines("\n")
                        cadastro.writelines("Estado: ")
                        cadastro.writelines(estadoCadastro)
                        # cadastro.writelines("\n")
                        # cadastro.writelines("Idade: ")
                        # cadastro.writelines(idade)
                    novoCadastro = input("Deseja fazer um novo cadastro? ")
                    if novoCadastro in respostas:
                        continue
                    else:
                        break
                        
            elif acao == 1:
                buscaCPF = input("Informe o CPF para a busca: ")
                with open("cadastro.txt", "r") as buscar:
                    busca = buscar.read().split()
                    try:
                        indice = busca.index(buscaCPF)
                        print(indice)
                        print(indice + 1)
                        print(indice + 2)
                        print(indice + 3)
                        print(indice + 4)
                        print(indice + 5)
                        
                    except:
                        print("Informe um cpf valido!!!")

            elif acao == 2:
                print("Bye-Bye")
                break

            else:
                print("Informe uma ação valida ")
            
        except: 
            print("Informe uma ação valida: ")

    except:
        print("Informe uma ação Valida")
