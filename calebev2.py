# Sistema Básico para Construção Fácil com validações robustas

# Dados iniciais
estoque = {}
vendedores = {}
clientes = {}
vendas = []
comissoes = {}

def validar_cpf(cpf):
    """Valida um CPF (somente números, 11 dígitos e dígitos verificadores)"""
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = 11 - (soma % 11)
    digito1 = resto if resto < 10 else 0
    
    if digito1 != int(cpf[9]):
        return False
    
    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = 11 - (soma % 11)
    digito2 = resto if resto < 10 else 0
    
    return digito2 == int(cpf[10])

def validar_email(email):
    """Valida o formato básico de um e-mail"""
    if '@' not in email or '.' not in email:
        return False
    return True

def obter_numero(mensagem, inteiro=False):
    """Obtém um número válido do usuário"""
    while True:
        try:
            valor = input(mensagem).strip()
            if not valor:
                print("Este campo não pode estar vazio.")
                continue
                
            if inteiro:
                valor = int(valor)
            else:
                valor = float(valor)
                
            if valor < 0:
                print("O valor não pode ser negativo.")
                continue
                
            return valor
        except ValueError:
            print("Por favor, digite um número válido.")

def obter_texto(mensagem, permitir_numeros=False, tamanho_min=1):
    """Obtém um texto válido do usuário"""
    while True:
        texto = input(mensagem).strip()
        if len(texto) < tamanho_min:
            print(f"Este campo deve ter pelo menos {tamanho_min} caracteres.")
            continue
        if not permitir_numeros and any(c.isdigit() for c in texto):
            print("Este campo não deve conter números.")
            continue
        return texto

def obter_data(mensagem):
    """Obtém uma data válida no formato DDMMAAAA"""
    while True:
        data = input(f"{mensagem} (DDMMAAAA): ").strip()
        if len(data) != 8 or not data.isdigit():
            print("Formato inválido. Use 8 dígitos (DDMMAAAA).")
            continue
            
        dia = int(data[:2])
        mes = int(data[2:4])
        ano = int(data[4:])
        
        if mes < 1 or mes > 12:
            print("Mês inválido. Deve ser entre 01 e 12.")
            continue
            
        if dia < 1 or dia > 31:
            print("Dia inválido. Deve ser entre 01 e 31.")
            continue
            
        # Validação básica de dias por mês (não considera anos bissextos)
        if mes in [4, 6, 9, 11] and dia > 30:
            print("Este mês só tem 30 dias.")
            continue
        elif mes == 2 and dia > 28:
            print("Fevereiro só tem 28 dias (não bissexto).")
            continue
            
        return data

def obter_cpf(mensagem):
    """Obtém um CPF válido do usuário"""
    while True:
        cpf = input(mensagem).strip()
        if not cpf.isdigit():
            print("CPF deve conter apenas números.")
            continue
        if len(cpf) != 11:
            print("CPF deve ter 11 dígitos.")
            continue
        if not validar_cpf(cpf):
            print("CPF inválido. Verifique os dígitos.")
            continue
        return cpf

def obter_email(mensagem):
    """Obtém um e-mail válido do usuário"""
    while True:
        email = input(mensagem).strip()
        if not validar_email(email):
            print("E-mail inválido. Deve conter @ e domínio.")
            continue
        return email

def cadastrar_produto():
    print("\n--- Cadastrar Produto ---")
    codigo = obter_texto("Código do produto: ", permitir_numeros=True, tamanho_min=3)
    nome = obter_texto("Nome do produto: ", tamanho_min=3)
    descricao = obter_texto("Descrição completa: ", tamanho_min=5)
    categoria = obter_texto("Categoria (elétrica/hidráulica/ferragens/básico): ", tamanho_min=3)
    unidade = obter_texto("Unidade de medida (kg/m2/peça/saco): ", tamanho_min=2)
    custo = obter_numero("Preço de custo: R$ ")
    venda = obter_numero("Preço de venda: R$ ")
    estoque_min = obter_numero("Estoque mínimo: ", inteiro=True)
    estoque_max = obter_numero("Estoque máximo: ", inteiro=True)
    quantidade = obter_numero("Quantidade em estoque: ", inteiro=True)
    
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
    print(f"\nProduto {nome} cadastrado com sucesso!")

def verificar_estoque(codigo):
    return estoque.get(codigo, None)

def cadastrar_vendedor():
    print("\n--- Cadastrar Vendedor ---")
    id_vendedor = obter_texto("ID do vendedor: ", permitir_numeros=True, tamanho_min=2)
    nome = obter_texto("Nome completo: ", tamanho_min=5)
    cpf = obter_cpf("CPF (somente números): ")
    telefone = obter_texto("Telefone (somente números): ", permitir_numeros=True, tamanho_min=8)
    email = obter_email("E-mail: ")
    
    vendedores[id_vendedor] = {
        'nome': nome,
        'cpf': cpf,
        'telefone': telefone,
        'email': email,
        'vendas': 0,
        'comissao': 0
    }
    print(f"\nVendedor {nome} cadastrado com sucesso!")

def cadastrar_cliente():
    print("\n--- Cadastrar Cliente ---")
    cpf_cnpj = obter_cpf("CPF (somente números): ")
    nome = obter_texto("Nome completo: ", tamanho_min=5)
    telefone = obter_texto("Telefone (somente números): ", permitir_numeros=True, tamanho_min=8)
    email = obter_email("E-mail: ")
    endereco = obter_texto("Endereço: ", tamanho_min=5)
    
    clientes[cpf_cnpj] = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    print(f"\nCliente {nome} cadastrado com sucesso!")

def realizar_venda():
    print("\n--- Realizar Venda ---")
    if not estoque:
        print("Não há produtos cadastrados para vender.")
        return
    if not vendedores:
        print("Não há vendedores cadastrados.")
        return
    
    id_venda = len(vendas) + 1
    data = obter_data("Data da venda")
    id_vendedor = obter_texto("ID do vendedor: ", permitir_numeros=True)
    
    if id_vendedor not in vendedores:
        print("Vendedor não encontrado!")
        return
    
    cpf_cliente = input("CPF do cliente (deixe em branco se não cadastrado): ").strip()
    if cpf_cliente:
        if not validar_cpf(cpf_cliente):
            print("CPF inválido. Prosseguindo sem cadastro.")
            cpf_cliente = ""
        elif cpf_cliente not in clientes:
            print("Cliente não cadastrado. Prosseguindo sem cadastro.")
    
    itens = []
    total = 0
    
    while True:
        print("\nProdutos disponíveis:")
        for codigo, produto in estoque.items():
            print(f"{codigo} - {produto['nome']} (R$ {produto['venda']:.2f}) - Estoque: {produto['quantidade']}")
        
        codigo = input("\nCódigo do produto (ou 'sair' para finalizar): ").strip().lower()
        if codigo == 'sair':
            if not itens:
                print("A venda precisa ter pelo menos um item.")
                continue
            break
            
        produto = verificar_estoque(codigo)
        if not produto:
            print("Produto não encontrado!")
            continue
            
        print(f"\nProduto selecionado: {produto['nome']}")
        print(f"Preço unitário: R$ {produto['venda']:.2f}")
        print(f"Estoque disponível: {produto['quantidade']}")
        
        quantidade = obter_numero("Quantidade: ", inteiro=True)
        
        if quantidade <= 0:
            print("Quantidade deve ser maior que zero.")
            continue
        if quantidade > produto['quantidade']:
            print("Quantidade em estoque insuficiente!")
            continue
            
        preco_unitario = produto['venda']
        desconto = obter_numero("Desconto (R$): ")
        if desconto < 0:
            print("Desconto não pode ser negativo.")
            continue
        if desconto > (preco_unitario * quantidade):
            print("Desconto não pode ser maior que o valor total do item.")
            continue
            
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
        forma_pagamento = input("\nForma de pagamento (dinheiro/cartão/PIX/boleto/crediário): ").lower()
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
    
    print(f"\n=== RESUMO DA VENDA ===")
    print(f"Data: {data[:2]}/{data[2:4]}/{data[4:]}")
    print(f"Vendedor: {vendedores[id_vendedor]['nome']}")
    if cpf_cliente:
        print(f"Cliente: {clientes[cpf_cliente]['nome']} (CPF: {cpf_cliente})")
    else:
        print("Cliente: Não cadastrado")
    
    print("\nItens:")
    for item in itens:
        produto = estoque[item['codigo']]
        print(f"- {produto['nome']}: {item['quantidade']} x R$ {item['preco_unitario']:.2f} = R$ {item['subtotal']:.2f}")
    
    print(f"\nTotal: R$ {total:.2f}")
    print(f"Forma de pagamento: {forma_pagamento.capitalize()}")
    print(f"Comissão do vendedor: R$ {comissao:.2f}")
    print("\nVenda registrada com sucesso!")

def gerar_relatorio_vendas():
    print("\n--- Relatório de Vendas ---")
    if not vendas:
        print("Nenhuma venda registrada.")
        return
        
    for venda in vendas:
        print(f"\nVenda ID: {venda['id']}")
        print(f"Data: {venda['data'][:2]}/{venda['data'][2:4]}/{venda['data'][4:]}")
        print(f"Vendedor: {vendedores[venda['vendedor']]['nome']} (ID: {venda['vendedor']})")
        
        if venda['cliente']:
            print(f"Cliente: {clientes[venda['cliente']]['nome']} (CPF: {venda['cliente']})")
        else:
            print("Cliente: Não cadastrado")
            
        print("\nItens:")
        for item in venda['itens']:
            produto = estoque[item['codigo']]
            print(f"- {produto['nome']}: {item['quantidade']} x R$ {item['preco_unitario']:.2f}")
            if item['desconto'] > 0:
                print(f"  Desconto: R$ {item['desconto']:.2f}")
            print(f"  Subtotal: R$ {item['subtotal']:.2f}")
        
        print(f"\nTotal da venda: R$ {venda['total']:.2f}")
        print(f"Forma de pagamento: {venda['forma_pagamento'].capitalize()}")
        print(f"Comissão: R$ {venda['comissao']:.2f}")
        print("-" * 40)

def gerar_relatorio_estoque():
    print("\n--- Relatório de Estoque ---")
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
        
    for codigo, produto in estoque.items():
        print(f"\nCódigo: {codigo}")
        print(f"Produto: {produto['nome']}")
        print(f"Descrição: {produto['descricao']}")
        print(f"Categoria: {produto['categoria'].capitalize()}")
        print(f"Unidade: {produto['unidade']}")
        print(f"Preço: Custo R$ {produto['custo']:.2f} | Venda R$ {produto['venda']:.2f}")
        print(f"Estoque: {produto['quantidade']} (Mín: {produto['estoque_min']}, Máx: {produto['estoque_max']})")
        
        if produto['quantidade'] < produto['estoque_min']:
            print("ALERTA: Estoque abaixo do mínimo!")
        elif produto['quantidade'] > produto['estoque_max']:
            print("AVISO: Estoque acima do máximo!")
        
        print("-" * 30)

def gerar_relatorio_vendedores():
    print("\n--- Relatório de Vendedores ---")
    if not vendedores:
        print("Nenhum vendedor cadastrado.")
        return
        
    for id_vendedor, vendedor in vendedores.items():
        print(f"\nID: {id_vendedor}")
        print(f"Nome: {vendedor['nome']}")
        print(f"CPF: {vendedor['cpf']}")
        print(f"Contato: {vendedor['telefone']} | {vendedor['email']}")
        print(f"Total de vendas: R$ {vendedor['vendas']:.2f}")
        print(f"Comissão acumulada: R$ {vendedor['comissao']:.2f}")
        print("-" * 30)

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
        
        opcao = input("\nEscolha uma opção: ").strip()
        
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
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida! Digite um número entre 0 e 7.")

# Iniciar o sistema
if __name__ == "__main__":
    print("=== BEM-VINDO AO SISTEMA CONSTRUÇÃO FÁCIL ===")
    menu_principal()