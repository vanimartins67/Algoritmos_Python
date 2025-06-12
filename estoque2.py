estoque = {"cimento": 500, "tijolos": 10000, "areia": 200, "telhas": 800, "tinta": 150, "ferro": 300}
while True:
    print("\nMENU:")
    print("1 - Ver material")
    print("2 - Add/atualizar")
    print("3 - Listar tudo")
    print("4 - Sair")
    op = input("> ")
    if op == "1":
        mat = input("\nMaterial: ").lower()
        if mat in estoque:
            print("Quantidade:", estoque[mat])
        else:
            print("Nao tem")
    elif op == "2":
        mat = input("\nMaterial: ").lower()
        qtd = input("Quantidade: ")
        if qtd.isdigit():
            estoque[mat] = int(qtd)
            print("Atualizado!")
        else:
            print("Numero invalido")
    elif op == "3":
        print("\nESTOQUE:")
        total = 0
        for mat in estoque:
            print(mat, "=", estoque[mat])
            total += estoque[mat]
        print("\nTotal geral:", total)
    elif op == "4":
        print("Saindo...")
        break
    else:
        print("Opcao invalida!")