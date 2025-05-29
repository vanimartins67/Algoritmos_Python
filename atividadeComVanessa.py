cpf = []
nome = []
idade = []
sexo = []
endereco = []
cidade = []
estado = []


while True:
    print("-----MENU-----")
    print("0 - Cadastro")
    print("1 - Relatorio")
    print("2 - Sair")
    try:
        acao = int(input("Informe a ação desejada: "))

        try:
            if acao == 0:
                cpfCadastro = input("Informe o CPF: ")
                nomeCadastro = input("informe o nome: ")
                sexoCadastro = input("Informe o Sexo: ")
                enderecoCadastro = input("Informe o endereço: ")
                cidadeCadastro = input("Informe a cidade: ")
                estadoCadastro = input("Informe o Estado: ")

                try:
                    idadeCadastro = int(input("Informe a Idade: "))
                except:
                    print("Informe uma idade valida: ")

                cpf.append(cpfCadastro)
                nome.append(nomeCadastro)
                idade.append(idadeCadastro)
                sexo.append(sexoCadastro)
                endereco.append(enderecoCadastro)
                cidade.append(cidadeCadastro)
                estado.append(estadoCadastro)

                with open("cadastro.txt", "a") as cadastro:
                    cadastro.writelines("\n")
                    cadastro.writelines(cpf)
                    cadastro.writelines(nome)
                    cadastro.writelines(idade)
                    cadastro.writelines(sexo)
                    cadastro.writelines(endereco)
                    cadastro.writelines(cidade)
                    cadastro.writelines(estado)

                    
        

                


            # elif acao == 1
            
        except: 
            print("Informe uma ação valida: ")

    except:
        print("Informe uma ação Valida")

    
    
