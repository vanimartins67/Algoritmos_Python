# Sistema Básico para Construção Fácil com tratamento de erros

# Dados iniciais
estoque = {}
vendedores = {}
clientes = {}
vendas = []
comissoes = {}
controle_fiscal = []

def obter_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Por favor, digite um número válido.")

def obter_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def obter_texto(mensagem, permitir_numeros=False):
    while True:
        texto = input(mensagem).strip()
        if not texto:
            print("Este campo não pode estar vazio. Tente novamente.")
            continue
        if not permitir_numeros and any(c.isdigit() for c in texto):
            print("Este campo não deve conter números. Tente novamente.")
            continue
        return texto

def obter_data(mensagem):
    while True:
        data = input(mensagem + " (DD/MM/AAAA): ")
        partes = data.split('/')
        if len(partes) == 3 and all(p.isdigit() for p in partes):
            return data
        print("Formato de data inválido. Use DD/MM/AAAA.")

def cadastrar_produto():
    print("\n--- Cadastrar Produto ---")
    codigo = obter_texto("Código de barras: ", permitir_numeros=True)
    nome = obter_texto("Nome do produto: ")
    descricao = obter_texto("Descrição completa: ")
    categoria = obter_texto("Categoria (elétrica/hidráulica/ferragens/básico): ")
    unidade = obter_texto("Unidade de medida (kg/m2/peça/saco): ")
    custo = obter_numero("Preço de custo: R$ ")
    venda = obter_numero("Preço de venda: R$ ")
    estoque_min = obter_inteiro("Estoque mínimo: ")
    estoque_max = obter_inteiro("Estoque máximo: ")
    quantidade = obter_inteiro("Quantidade em estoque: ")
    
    estoque[codigo] = {
        'nome': nome,
        'descricao': descricao,
        'categoria': categoria,
        'unidade': unidade,
        'custo': custo,
        'venda': venda,
        'estoque_min': estoque_min,
        'estoque_max': estoque_max,
        'quantidade': quantidade
    }
    print(f"Produto {nome} cadastrado com sucesso!")

def verificar_estoque(codigo):
    return estoque.get(codigo, None)

def atualizar_estoque(codigo, quantidade):
    if codigo in estoque:
        estoque[codigo]['quantidade'] += quantidade
        return True
    return False

def cadastrar_vendedor():
    print("\n--- Cadastrar Vendedor ---")
    id_vendedor = obter_texto("ID do vendedor: ", permitir_numeros=True)
    nome = obter_texto("Nome completo: ")
    cpf = obter_texto("CPF (somente números): ", permitir_numeros=True)
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido. Deve conter 11 dígitos.")
        return
    telefone = obter_texto("Telefone (somente números): ", permitir_numeros=True)
    
    vendedores[id_vendedor] = {
        'nome': nome,
        'cpf': cpf,
        'telefone': telefone,
        'vendas': 0,
        'comissao': 0
    }
    print(f"Vendedor {nome} cadastrado com sucesso!")

def cadastrar_cliente():
    print("\n--- Cadastrar Cliente ---")
    cpf_cnpj = obter_texto("CPF/CNPJ (somente números): ", permitir_numeros=True)
    nome = obter_texto("Nome/Razão Social: ")
    telefone = obter_texto("Telefone (somente números): ", permitir_numeros=True)
    endereco = obter_texto("Endereço: ")
    
    clientes[cpf_cnpj] = {
        'nome': nome,
        'telefone': telefone,
        'endereco': endereco
    }
    print(f"Cliente {nome} cadastrado com sucesso!")

def realizar_venda():
    print("\n--- Realizar Venda ---")
    id_venda = len(vendas) + 1
    data = obter_data("Data da venda")
    id_vendedor = obter_texto("ID do vendedor: ", permitir_numeros=True)
    
    if id_vendedor not in vendedores:
        print("Vendedor não encontrado!")
        return
    
    cpf_cliente = input("CPF/CNPJ do cliente (deixe em branco se não cadastrado): ").strip()
    if cpf_cliente and cpf_cliente not in clientes:
        print("Cliente não cadastrado. Prosseguindo sem cadastro.")
    
    itens = []
    total = 0
    
    while True:
        codigo = input("Código do produto (ou 'sair' para finalizar): ").strip()
        if codigo.lower() == 'sair':
            if not itens:
                print("A venda precisa ter pelo menos um item.")
                continue
            break
            
        produto = verificar_estoque(codigo)
        if not produto:
            print("Produto não encontrado!")
            continue
            
        print(f"Produto: {produto['nome']} - Estoque: {produto['quantidade']}")
        quantidade = obter_inteiro("Quantidade: ")
        
        if quantidade > produto['quantidade']:
            print("Quantidade em estoque insuficiente!")
            continue
            
        preco_unitario = produto['venda']
        desconto = obter_numero("Desconto (R$): ")
        subtotal = (preco_unitario * quantidade) - desconto
        
        itens.append({
            'codigo': codigo,
            'quantidade': quantidade,
            'preco_unitario': preco_unitario,
            'desconto': desconto,
            'subtotal': subtotal
        })
        
        total += subtotal
        produto['quantidade'] -= quantidade  # Baixa no estoque
        
    formas_validas = ['dinheiro', 'cartão', 'pix', 'boleto', 'crediário']
    while True:
        forma_pagamento = input("Forma de pagamento (dinheiro/cartão/PIX/boleto/crediário): ").lower()
        if forma_pagamento in formas_validas:
            break
        print("Forma de pagamento inválida. Escolha entre: dinheiro, cartão, PIX, boleto ou crediário")
    
    if forma_pagamento == 'cartão':
        comissao = total * 0.03
    else:
        comissao = total * 0.05
        
    vendedores[id_vendedor]['vendas'] += total
    vendedores[id_vendedor]['comissao'] += comissao
    
    venda = {
        'id': id_venda,
        'data': data,
        'vendedor': id_vendedor,
        'cliente': cpf_cliente,
        'itens': itens,
        'total': total,
        'forma_pagamento': forma_pagamento,
        'comissao': comissao
    }
    
    vendas.append(venda)
    
    # Gerar documento fiscal
    documento = {
        'tipo': 'NF-e' if len(cpf_cliente) > 11 else 'NFC-e',
        'numero': len(controle_fiscal) + 1,
        'data': data,
        'valor': total,
        'cliente': cpf_cliente
    }
    controle_fiscal.append(documento)
    
    print(f"\nVenda realizada com sucesso!")
    print(f"Total: R$ {total:.2f}")
    print(f"Comissão do vendedor: R$ {comissao:.2f}")

def gerar_relatorio_vendas():
    print("\n--- Relatório de Vendas ---")
    if not vendas:
        print("Nenhuma venda registrada.")
        return
        
    for venda in vendas:
        print(f"\nVenda ID: {venda['id']} - Data: {venda['data']}")
        print(f"Vendedor: {venda['vendedor']} - {vendedores[venda['vendedor']]['nome']}")
        if venda['cliente']:
            cliente_nome = clientes.get(venda['cliente'], {}).get('nome', 'Não cadastrado')
            print(f"Cliente: {venda['cliente']} - {cliente_nome}")
        else:
            print("Cliente: Não cadastrado")
        print("Itens:")
        for item in venda['itens']:
            produto = estoque[item['codigo']]
            print(f"- {produto['nome']}: {item['quantidade']} x R$ {item['preco_unitario']:.2f} = R$ {item['subtotal']:.2f}")
        print(f"Total: R$ {venda['total']:.2f} - Forma: {venda['forma_pagamento'].capitalize()}")
        print(f"Comissão: R$ {venda['comissao']:.2f}")

def gerar_relatorio_estoque():
    print("\n--- Relatório de Estoque ---")
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
        
    for codigo, produto in estoque.items():
        print(f"\nCódigo: {codigo} - {produto['nome']}")
        print(f"Categoria: {produto['categoria'].capitalize()} - Unidade: {produto['unidade']}")
        print(f"Estoque: {produto['quantidade']} (Mín: {produto['estoque_min']}, Máx: {produto['estoque_max']})")
        print(f"Preço: Custo R$ {produto['custo']:.2f} - Venda R$ {produto['venda']:.2f}")
        if produto['quantidade'] < produto['estoque_min']:
            print("ALERTA: Estoque abaixo do mínimo!")

def gerar_relatorio_vendedores():
    print("\n--- Relatório de Vendedores ---")
    if not vendedores:
        print("Nenhum vendedor cadastrado.")
        return
        
    for id_vendedor, vendedor in vendedores.items():
        print(f"\nID: {id_vendedor} - {vendedor['nome']}")
        print(f"CPF: {vendedor['cpf']} - Telefone: {vendedor['telefone']}")
        print(f"Total vendas: R$ {vendedor['vendas']:.2f}")
        print(f"Comissão acumulada: R$ {vendedor['comissao']:.2f}")

def menu_principal():
    while True:
        print("\n=== SISTEMA CONSTRUÇÃO FÁCIL ===")
        print("1. Cadastrar Produto")
        print("2. Cadastrar Vendedor")
        print("3. Cadastrar Cliente")
        print("4. Realizar Venda")
        print("5. Relatório de Vendas")
        print("6. Relatório de Estoque")
        print("7. Relatório de Vendedores")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            cadastrar_vendedor()
        elif opcao == "3":
            cadastrar_cliente()
        elif opcao == "4":
            realizar_venda()
        elif opcao == "5":
            gerar_relatorio_vendas()
        elif opcao == "6":
            gerar_relatorio_estoque()
        elif opcao == "7":
            gerar_relatorio_vendedores()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Digite um número entre 0 e 7.")

# Iniciar o sistema
if __name__ == "__main__":
    menu_principal()