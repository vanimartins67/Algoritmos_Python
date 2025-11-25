# TELA DE INTERAÇÃO COM O USUÁRIO
from Cliente import Cliente

while True:
    print("SysPerkal")
    print("*"*30)
    print("Selecione uma opção")
    opcao = input("1 - Cadastrar \n2 - Listar Clientes \n3 - Excluir Cliente \n4 - Atualizar \n0 - SAIR\n")

    if opcao == "0":
        break
    elif opcao == "1":
        cli = Cliente()
        cli.nome = input("Digite o nome do cliente: ")
        cli.cpf = input("Digite o CPF: ")
        cli.fone = input("Digite o telefone: ")
        cli.cidade = input("Digite sua cidade: ")
        result = cli.cadastrar()
        if result == True:
            print("Cadastrado com sucesso!")

    elif opcao == "2":
        cli = Cliente()
        result = cli.buscar()
        for cliente in result:
            print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} | CIDADE: {cliente[4]}')

    elif opcao == "3":
        cli = Cliente()
        result = cli.buscar()
        for cliente in result:
            print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} | CIDADE: {cliente[4]}')

        id_excluir = int(input("Digite o ID qe deseja excluir: "))
        result = cli.excluir(id_excluir)
        if result == True:
            print("Excluído(a) com sucesso!")

    elif opcao == "4":
        cli = Cliente()
        result = cli.buscar()
        for cliente in result:
            print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} | CIDADE: {cliente[4]}')
        
        id_atualiza = int(input("Digite o ID a ser atualizado:"))
        result = list(cli.buscar_por_id(id_atualiza))
        result[1] = input("Digite novo Nome: ")
        result[2] = input("Digite novo CPF: ")
        result[3] = input("Digite novo telefone: ")
        result[4] = input("Digite nova cidade: ")
        atualizacao = cli.atualizar(tuple(result))
        if atualizacao == True:
            print("Cliente atualizado com sucesso!")