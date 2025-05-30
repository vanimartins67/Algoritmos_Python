# Dicionário de Estoque Aprimorado (sem o operador 'not')

# 1. Criação do dicionário inicial para representar o estoque da loja.
estoque = {
    'martelo': 50,
    'chave de fenda': 75,
    'parafuso': 500,
    'prego': 1000,
    'serrote': 25,
    'trena': 30,
    'alicate': 40,
    'fita isolante': 100,
    'nível': 15,
    'luvas de proteção': 60
}

# Loop principal do programa
while True:
    # Exibe o menu de opções para o usuário
    print("\n--- Sistema de Gerenciamento de Estoque ---")
    print("Escolha uma opção:")
    print("1. Consultar Produto")
    print("2. Cadastrar Novo Produto / Atualizar Quantidade")
    print("3. Gerar Relatório de Estoque")
    print("4. Sair")
    opcao = input("Opção: ")

    if opcao == '1':
        # Consultar Produto
        produto_desejado = input("\nDigite o nome do produto que você deseja consultar: ").lower()
        quantidade = estoque.get(produto_desejado)

        # Verificamos se a quantidade é None (produto não encontrado)
        if quantidade is None:
            print(f"\nDesculpe, o produto '{produto_desejado}' não está disponível em nosso estoque. 👎")
        else:
            # Se não for None, o produto está em estoque
            print(f"\nProduto em estoque! 👍")
            print(f"Temos {quantidade} unidades de '{produto_desejado}' disponíveis.")

    elif opcao == '2':
        # Cadastrar Novo Produto / Atualizar Quantidade
        print("\n--- Cadastro de Novo Produto / Atualização ---")
        nome_produto = input("Digite o nome do produto: ").lower()
        
        while True:
            try:
                quantidade_produto = int(input(f"Digite a quantidade de '{nome_produto}': "))
                if quantidade_produto < 0:
                    print("A quantidade deve ser um número positivo ou zero. Tente novamente.")
                else:
                    break # Sai do loop se a quantidade for válida
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para a quantidade.")

        if nome_produto in estoque:
            print(f"\nO produto '{nome_produto}' já existe no estoque com {estoque[nome_produto]} unidades.")
            atualizar = input("Deseja ATUALIZAR a quantidade existente? (s/n): ").lower()
            if atualizar == 's':
                estoque[nome_produto] = quantidade_produto
                print(f"Quantidade de '{nome_produto}' atualizada para {quantidade_produto} unidades.")
            else:
                print(f"A quantidade de '{nome_produto}' permaneceu {estoque[nome_produto]} unidades.")
        else:
            estoque[nome_produto] = quantidade_produto
            print(f"\nProduto '{nome_produto}' cadastrado com sucesso com {quantidade_produto} unidades! 🎉")

    elif opcao == '3':
        # Gerar Relatório de Estoque
        print("\n--- Relatório de Estoque ---")
        # Verificamos se o tamanho do dicionário é 0 (estoque vazio)
        if len(estoque) == 0:
            print("O estoque está vazio no momento.")
        else:
            print(f"{'Produto':<25} | {'Quantidade':<10}")
            print("-" * 40) # Linha divisória
            total_itens = 0
            for produto, quantidade in estoque.items():
                print(f"{produto.capitalize():<25} | {quantidade:<10}")
                total_itens += quantidade
            print("-" * 40)
            print(f"Total de tipos de produtos: {len(estoque)}")
            print(f"Total geral de itens no estoque: {total_itens}")
        print("-" * 40)

    elif opcao == '4':
        # Sair
        print("\nSaindo do sistema de estoque. Até logo! 👋")
        break # Interrompe o loop while, encerrando o programa

    else:
        # Opção inválida
        print("\nOpção inválida. Por favor, escolha uma opção de 1 a 4.")

    # Pausa para o usuário ler a saída antes de mostrar o menu novamente
    # (exceto quando está saindo)
    if opcao != '4': # Aqui '!=' (diferente) é usado, o que é comum e geralmente não é o 'not' que se evita em fases iniciais.
                     # Se '!=' também for um problema, podemos reestruturar.
        input("\nPressione Enter para continuar...")