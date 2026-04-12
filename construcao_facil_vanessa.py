import os
from datetime import datetime
import re

ARQUIVO_PRODUTOS = "produtos.txt"
ARQUIVO_VENDEDORES = "vendedores.txt"
ARQUIVO_CLIENTES = "clientes.txt"
ARQUIVO_VENDAS = "vendas.txt"
ARQUIVO_ORCAMENTOS = "orcamentos.txt"
ARQUIVO_CONTAS_RECEBER = "contas_a_receber.txt"

produtos = {}
vendedores = {}
clientes = {}
vendas = []
orcamentos = {}
contas_a_receber = {}

# VALIDAÇÃO
def validar_cpf(cpf):
    """Verifica se o CPF tem 11 dígitos numéricos e se é válido."""
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    if len(set(cpf)) == 1:
        return False
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0
    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2

def validar_email(email):
    """Verifica se o e-mail tem um formato válido."""
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

def obter_data_valida():
    while True:
        data = input("Data (DD/MM/AAAA): ").strip()
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data.replace("/", "")
        except ValueError:
            print("Data inválida. Use o formato DD/MM/AAAA.")

# PERSISTÊNCIA
def salvar_dados():
    try:
        with open(ARQUIVO_PRODUTOS, 'w') as f:
            for cod, prod in produtos.items():
                f.write(f"{cod};{prod['nome']};{prod['categoria']};{prod['unidade']};{prod['preco_custo']};{prod['preco_venda']};{prod['estoque_min']};{prod['estoque_max']};{prod['quantidade']}\n")
        
        with open(ARQUIVO_VENDEDORES, 'w') as f:
            for id_vend, vend in vendedores.items():
                f.write(f"{id_vend};{vend['nome']};{vend['cpf']};{vend['vendas']};{vend['comissao']}\n")
        
        with open(ARQUIVO_CLIENTES, 'w') as f:
            for cpf, cli in clientes.items():
                f.write(f"{cpf};{cli['nome']};{cli['telefone']};{cli['email']};{cli['endereco']}\n")
        
        with open(ARQUIVO_VENDAS, 'w') as f:
            for venda in vendas:
                f.write(f"{venda['data']};{venda['vendedor']};{venda['cliente']};{venda['total']};{venda['forma_pagamento']};{venda['comissao']}\n")
                for item in venda['itens']:
                    f.write(f"ITEM;{item['codigo']};{item['quantidade']};{item['desconto']};{item['subtotal']}\n")

        with open(ARQUIVO_ORCAMENTOS, 'w') as f:
            for id_orc, orc in orcamentos.items():
                f.write(f"{id_orc};{orc['data']};{orc['vendedor']};{orc['cliente']};{orc['total']}\n")
                for item in orc['itens']:
                    f.write(f"ITEM;{item['codigo']};{item['quantidade']};{item['subtotal']}\n")

        with open(ARQUIVO_CONTAS_RECEBER, 'w') as f:
            for id_venda, conta in contas_a_receber.items():
                f.write(f"{id_venda};{conta['cliente_cpf']};{conta['total']};{conta['pago']};{conta['pendente']}\n")
        return True
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
        return False

def salvar_automaticamente():
    """Salva dados silenciosamente (sem mensagens)"""
    salvar_dados()

def carregar_dados():
    try:
        if os.path.exists(ARQUIVO_PRODUTOS):
            with open(ARQUIVO_PRODUTOS, 'r') as f:
                for linha in f:
                    dados = linha.strip().split(';')
                    if len(dados) == 9:
                        produtos[dados[0]] = {
                            'nome': dados[1], 'categoria': dados[2], 'unidade': dados[3],
                            'preco_custo': float(dados[4]), 'preco_venda': float(dados[5]),
                            'estoque_min': int(dados[6]), 'estoque_max': int(dados[7]), 
                            'quantidade': int(dados[8])
                        }
        
        if os.path.exists(ARQUIVO_VENDEDORES):
            with open(ARQUIVO_VENDEDORES, 'r') as f:
                for linha in f:
                    dados = linha.strip().split(';')
                    if len(dados) == 5:
                        vendedores[dados[0]] = {
                            'nome': dados[1], 'cpf': dados[2],
                            'vendas': float(dados[3]), 'comissao': float(dados[4])
                        }
        
        if os.path.exists(ARQUIVO_CLIENTES):
            with open(ARQUIVO_CLIENTES, 'r') as f:
                for linha in f:
                    dados = linha.strip().split(';')
                    if len(dados) == 5:
                        clientes[dados[0]] = {
                            'nome': dados[1], 'telefone': dados[2],
                            'email': dados[3], 'endereco': dados[4]
                        }
        
        if os.path.exists(ARQUIVO_VENDAS):
            with open(ARQUIVO_VENDAS, 'r') as f:
                venda_atual = None
                for linha in f:
                    dados = linha.strip().split(';')
                    if dados[0] == 'ITEM' and venda_atual:
                        venda_atual['itens'].append({
                            'codigo': dados[1], 'quantidade': int(dados[2]),
                            'desconto': float(dados[3]), 'subtotal': float(dados[4])
                        })
                    else:
                        if venda_atual:
                            vendas.append(venda_atual)
                        if len(dados) == 6:
                            venda_atual = {
                                'data': dados[0], 'vendedor': dados[1], 'cliente': dados[2],
                                'total': float(dados[3]), 'forma_pagamento': dados[4],
                                'comissao': float(dados[5]), 'itens': []
                            }
                if venda_atual:
                    vendas.append(venda_atual)
        
        if os.path.exists(ARQUIVO_ORCAMENTOS):
            with open(ARQUIVO_ORCAMENTOS, 'r') as f:
                orcamento_atual = None
                for linha in f:
                    dados = linha.strip().split(';')
                    if dados[0] == 'ITEM' and orcamento_atual:
                        orcamento_atual['itens'].append({
                            'codigo': dados[1], 'quantidade': int(dados[2]),
                            'subtotal': float(dados[3])
                        })
                    else:
                        if orcamento_atual:
                            orcamentos[orcamento_atual['id']] = orcamento_atual
                        if len(dados) == 5:
                            orcamento_atual = {
                                'id': dados[0], 'data': dados[1], 'vendedor': dados[2],
                                'cliente': dados[3], 'total': float(dados[4]), 'itens': []
                            }
                if orcamento_atual:
                    orcamentos[orcamento_atual['id']] = orcamento_atual

        if os.path.exists(ARQUIVO_CONTAS_RECEBER):
            with open(ARQUIVO_CONTAS_RECEBER, 'r') as f:
                for linha in f:
                    dados = linha.strip().split(';')
                    if len(dados) == 5:
                        contas_a_receber[dados[0]] = {
                            'cliente_cpf': dados[1], 'total': float(dados[2]),
                            'pago': float(dados[3]), 'pendente': float(dados[4])
                        }
        return True
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return False

# CADASTROS
def cadastrar_cliente():
    print("\n--- CADASTRAR CLIENTE ---")
    cpf = input("CPF (11 dígitos): ").strip()
    while not validar_cpf(cpf):
        print("CPF inválido! Por favor, digite um CPF válido.")
        cpf = input("CPF (11 dígitos): ").strip()

    if cpf in clientes:
        print("Cliente com este CPF já cadastrado.")
        return

    nome = input("Nome completo: ").strip()
    while not nome.replace(" ", "").isalpha():
        print("Nome inválido! Por favor, digite apenas letras.")
        nome = input("Nome completo: ").strip()

    telefone = input("Telefone (apenas números): ").strip()
    while not telefone.isdigit():
        print("Telefone inválido! Por favor, digite apenas números.")
        telefone = input("Telefone (apenas números): ").strip()

    email = input("E-mail: ").strip()
    while not validar_email(email):
        print("E-mail inválido! Use o formato nome@dominio.com")
        email = input("E-mail: ").strip()
    
    endereco = input("Endereço: ").strip()
    
    clientes[cpf] = {'nome': nome, 'telefone': telefone, 'email': email, 'endereco': endereco}
    salvar_automaticamente()
    print(f"Cliente {nome} cadastrado!")

def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")
    codigo = input("Código de barras: ").strip()
    if codigo in produtos:
        print("Produto com este código já cadastrado.")
        return
    nome = input("Nome: ").strip()
    categoria = input("Categoria (elétrica/hidráulica/ferragens/básico): ").strip()
    unidade = input("Unidade (kg/m2/peça/saco): ").strip()
    
    try:
        preco_custo = float(input("Preço de custo R$: "))
        preco_venda = float(input("Preço de venda R$: "))
        estoque_min = int(input("Estoque mínimo: "))
        estoque_max = int(input("Estoque máximo: "))
        quantidade = int(input("Quantidade em estoque: "))
    except ValueError:
        print("Entrada inválida! Os valores devem ser numéricos. Cadastro cancelado.")
        return
        
    produtos[codigo] = {
        'nome': nome, 'categoria': categoria, 'unidade': unidade,
        'preco_custo': preco_custo, 'preco_venda': preco_venda,
        'estoque_min': estoque_min, 'estoque_max': estoque_max,
        'quantidade': quantidade
    }
    salvar_automaticamente()
    print(f"Produto {nome} cadastrado!")

def cadastrar_vendedor():
    print("\n--- CADASTRAR VENDEDOR ---")
    id_vendedor = input("ID do vendedor: ").strip()
    if id_vendedor in vendedores:
        print("Vendedor com este ID já cadastrado.")
        return
    nome = input("Nome completo: ").strip()
    cpf = input("CPF (11 dígitos): ").strip()
    while not validar_cpf(cpf):
        print("CPF inválido! Por favor, digite um CPF válido.")
        cpf = input("CPF (11 dígitos): ").strip()
    
    vendedores[id_vendedor] = {'nome': nome, 'cpf': cpf, 'vendas': 0.0, 'comissao': 0.0}
    salvar_automaticamente()
    print(f"Vendedor {nome} cadastrado!")

# OPERAÇÕES DA LOJA
def registrar_itens(tipo_operacao):
    itens = []
    total = 0.0
    while True:
        print("\nProdutos disponíveis:")
        for cod, prod in produtos.items():
            print(f"{cod} - {prod['nome']} | R$ {prod['preco_venda']:.2f} | Estoque: {prod['quantidade']}")
        
        codigo = input(f"\nCódigo do produto (ou 'finalizar'): ").strip().lower()
        if codigo == 'finalizar':
            if not itens:
                print("Adicione ao menos 1 item!")
                continue
            break
        
        if codigo not in produtos:
            print("Código inválido!")
            continue
        
        produto = produtos[codigo]
        try:
            qtd = int(input(f"Quantidade de {produto['nome']}: "))
            if qtd <= 0:
                print("Quantidade deve ser positiva!")
                continue
            
            if tipo_operacao in ['venda', 'troca'] and qtd > produto['quantidade']:
                print(f"Estoque insuficiente! Disponível: {produto['quantidade']}")
                continue
            
            desconto = 0.0
            if tipo_operacao == 'venda':
                desconto = float(input("Desconto R$ (0 se nenhum): "))
                if desconto < 0:
                    print("Desconto não pode ser negativo!")
                    continue
            
            subtotal = (produto['preco_venda'] * qtd) - desconto
            itens.append({
                'codigo': codigo, 'quantidade': qtd,
                'desconto': desconto, 'subtotal': subtotal
            })
            total += subtotal
        except ValueError:
            print("Valor inválido! Digite um número.")
    return itens, total

def realizar_venda():
    print("\n--- REALIZAR VENDA ---")
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    if not vendedores:
        print("Nenhum vendedor cadastrado!")
        return
    
    data = obter_data_valida()
    
    id_vendedor = input("ID do vendedor: ").strip()
    if id_vendedor not in vendedores:
        print("Vendedor não encontrado!")
        return
    
    cpf_cliente = input("CPF do cliente (deixe em branco se não cadastrado): ").strip()
    if cpf_cliente and not validar_cpf(cpf_cliente):
        print("CPF do cliente inválido. Venda avulsa.")
        cpf_cliente = ""
    elif cpf_cliente and cpf_cliente not in clientes:
        print("Cliente não cadastrado. Venda avulsa.")
        cpf_cliente = ""

    itens, total = registrar_itens('venda')
    if not itens:
        print("Venda cancelada.")
        return

    formas = {
        '1': {'nome': 'Dinheiro', 'comissao': 0.05},
        '2': {'nome': 'Cartão', 'comissao': 0.03},
        '3': {'nome': 'PIX', 'comissao': 0.05},
        '4': {'nome': 'Boleto', 'comissao': 0.05},
        '5': {'nome': 'Crediário', 'comissao': 0.03}
    }
    
    print("\nFORMAS DE PAGAMENTO:")
    for op, forma in formas.items():
        print(f"{op} - {forma['nome']}")
    
    while True:
        opcao = input("Escolha a forma: ").strip()
        if opcao in formas:
            forma_pagamento = formas[opcao]['nome']
            comissao = total * formas[opcao]['comissao']
            break
        print("Opção inválida!")
    
    vendedores[id_vendedor]['vendas'] += total
    vendedores[id_vendedor]['comissao'] += comissao
    
    id_venda = str(len(vendas) + 1)
    
    venda = {
        'id': id_venda, 'data': data, 'vendedor': id_vendedor, 'cliente': cpf_cliente,
        'itens': itens, 'total': total,
        'forma_pagamento': forma_pagamento, 'comissao': comissao
    }
    vendas.append(venda)

    for item in itens:
        produtos[item['codigo']]['quantidade'] -= item['quantidade']

    if forma_pagamento == 'Crediário':
        contas_a_receber[id_venda] = {
            'cliente_cpf': cpf_cliente,
            'total': total,
            'pago': 0.0,
            'pendente': total
        }

    salvar_automaticamente()
    print(f"\nVENDA CONCLUÍDA! Total: R$ {total:.2f}")
    print(f"Comissão do vendedor: R$ {comissao:.2f}")

def realizar_orcamento():
    print("\n--- REALIZAR ORÇAMENTO ---")
    id_orcamento = input("ID do orçamento: ").strip()
    if id_orcamento in orcamentos:
        print("Orçamento com este ID já existe.")
        return

    data = obter_data_valida()
    id_vendedor = input("ID do vendedor: ").strip()
    if id_vendedor not in vendedores:
        print("Vendedor não encontrado!")
        return
    
    cpf_cliente = input("CPF do cliente (deixe em branco se não cadastrado): ").strip()
    if cpf_cliente and not validar_cpf(cpf_cliente):
        print("CPF do cliente inválido. Orçamento avulso.")
        cpf_cliente = ""
    elif cpf_cliente and cpf_cliente not in clientes:
        print("Cliente não cadastrado. Orçamento avulso.")
        cpf_cliente = ""

    itens, total = registrar_itens('orcamento')
    if not itens:
        print("Orçamento cancelado.")
        return

    orcamentos[id_orcamento] = {
        'id': id_orcamento,
        'data': data,
        'vendedor': id_vendedor,
        'cliente': cpf_cliente,
        'itens': itens,
        'total': total
    }
    salvar_automaticamente()
    print(f"Orçamento {id_orcamento} criado com sucesso! Total: R$ {total:.2f}")

def converter_orcamento_em_venda():
    print("\n--- CONVERTER ORÇAMENTO EM VENDA ---")
    if not orcamentos:
        print("Nenhum orçamento pendente para converter.")
        return
    
    id_orcamento = input("Digite o ID do orçamento a ser convertido: ").strip()
    if id_orcamento not in orcamentos:
        print("Orçamento não encontrado.")
        return

    orcamento = orcamentos[id_orcamento]
    
    data = obter_data_valida()
    id_vendedor = orcamento['vendedor']
    cpf_cliente = orcamento['cliente']
    itens = orcamento['itens']
    total = orcamento['total']

    for item in itens:
        if produtos[item['codigo']]['quantidade'] < item['quantidade']:
            print(f"Estoque insuficiente para o item {produtos[item['codigo']]['nome']}.")
            return
            
    formas = {
        '1': {'nome': 'Dinheiro', 'comissao': 0.05},
        '2': {'nome': 'Cartão', 'comissao': 0.03},
        '3': {'nome': 'PIX', 'comissao': 0.05},
        '4': {'nome': 'Boleto', 'comissao': 0.05},
        '5': {'nome': 'Crediário', 'comissao': 0.03}
    }
    
    print("\nFORMAS DE PAGAMENTO:")
    for op, forma in formas.items():
        print(f"{op} - {forma['nome']}")
    
    while True:
        opcao = input("Escolha a forma de pagamento para a venda: ").strip()
        if opcao in formas:
            forma_pagamento = formas[opcao]['nome']
            comissao = total * formas[opcao]['comissao']
            break
        print("Opção inválida!")
    
    vendedores[id_vendedor]['vendas'] += total
    vendedores[id_vendedor]['comissao'] += comissao
    
    id_venda = str(len(vendas) + 1)
    
    venda = {
        'id': id_venda, 'data': data, 'vendedor': id_vendedor, 'cliente': cpf_cliente,
        'itens': itens, 'total': total,
        'forma_pagamento': forma_pagamento, 'comissao': comissao
    }
    vendas.append(venda)

    for item in itens:
        produtos[item['codigo']]['quantidade'] -= item['quantidade']

    if forma_pagamento == 'Crediário':
        contas_a_receber[id_venda] = {
            'cliente_cpf': cpf_cliente,
            'total': total,
            'pago': 0.0,
            'pendente': total
        }

    del orcamentos[id_orcamento]
    salvar_automaticamente()
    print(f"\nOrçamento {id_orcamento} convertido em venda {id_venda} com sucesso!")

def registrar_devolucao_troca():
    print("\n--- REGISTRAR DEVOLUÇÃO/TROCA ---")
    if not vendas:
        print("Nenhuma venda realizada para registrar devolução/troca.")
        return

    id_venda = input("Digite o ID da venda para devolução/troca: ").strip()
    venda_encontrada = next((v for v in vendas if v['id'] == id_venda), None)
    
    if not venda_encontrada:
        print("Venda não encontrada.")
        return

    print("Itens da venda:")
    for i, item in enumerate(venda_encontrada['itens']):
        print(f"{i+1} - {produtos[item['codigo']]['nome']} | Quantidade: {item['quantidade']}")
    
    try:
        idx_item = int(input("Número do item a ser devolvido/trocado: ")) - 1
        if not 0 <= idx_item < len(venda_encontrada['itens']):
            print("Número de item inválido.")
            return

        item_devolvido = venda_encontrada['itens'][idx_item]
        qtd_devolvida = int(input(f"Quantidade a ser devolvida (máx: {item_devolvido['quantidade']}): "))
        
        if qtd_devolvida <= 0 or qtd_devolvida > item_devolvido['quantidade']:
            print("Quantidade inválida.")
            return
            
    except ValueError:
        print("Entrada inválida.")
        return

    produtos[item_devolvido['codigo']]['quantidade'] += qtd_devolvida

    valor_devolvido = (produtos[item_devolvido['codigo']]['preco_venda'] * qtd_devolvida) - item_devolvido['desconto']
    venda_encontrada['total'] -= valor_devolvido
    comissao_original = vendedores[venda_encontrada['vendedor']]['comissao']
    
    if venda_encontrada['forma_pagamento'] == 'Crediário':
        if id_venda in contas_a_receber:
            contas_a_receber[id_venda]['total'] -= valor_devolvido
            contas_a_receber[id_venda]['pendente'] -= valor_devolvido
    
    if 'Cartão' in venda_encontrada['forma_pagamento']:
        fator_comissao = 0.03
    else:
        fator_comissao = 0.05
    
    venda_encontrada['comissao'] -= (valor_devolvido * fator_comissao)
    vendedores[venda_encontrada['vendedor']]['comissao'] = venda_encontrada['comissao']

    item_devolvido['quantidade'] -= qtd_devolvida

    salvar_automaticamente()
    print(f"\nDevolução de {qtd_devolvida} unidades de {produtos[item_devolvido['codigo']]['nome']} registrada com sucesso.")
    print("Estoque e comissão do vendedor ajustados.")

def registrar_pagamento_crediario():
    print("\n--- REGISTRAR PAGAMENTO DE CREDÍARIO ---")
    if not contas_a_receber:
        print("Nenhuma conta a receber pendente.")
        return

    print("\nCONTAS A RECEBER PENDENTES:")
    for id_venda, conta in contas_a_receber.items():
        if conta['pendente'] > 0:
            cliente_nome = clientes.get(conta['cliente_cpf'], {}).get('nome', 'Cliente não cadastrado')
            print(f"Venda ID: {id_venda} | Cliente: {cliente_nome} | Pendente: R$ {conta['pendente']:.2f}")

    id_venda = input("\nDigite o ID da venda para registrar pagamento: ").strip()
    if id_venda not in contas_a_receber or contas_a_receber[id_venda]['pendente'] == 0:
        print("Venda não encontrada ou já quitada.")
        return

    conta = contas_a_receber[id_venda]
    try:
        valor_pagamento = float(input(f"Valor do pagamento (pendente: R$ {conta['pendente']:.2f}): "))
        if valor_pagamento <= 0 or valor_pagamento > conta['pendente']:
            print("Valor de pagamento inválido.")
            return
    except ValueError:
        print("Valor inválido.")
        return

    conta['pago'] += valor_pagamento
    conta['pendente'] -= valor_pagamento

    salvar_automaticamente()
    print(f"Pagamento de R$ {valor_pagamento:.2f} registrado para a venda {id_venda}.")
    print(f"Valor pendente atual: R$ {conta['pendente']:.2f}")

# RELATÓRIOS
def relatorio_estoque():
    print("\n--- RELATÓRIO DE ESTOQUE ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
        
    for cod, prod in produtos.items():
        alerta = ""
        if prod['quantidade'] < prod['estoque_min']:
            alerta = " (ESTOQUE BAIXO!)"
        elif prod['quantidade'] > prod['estoque_max']:
            alerta = " (ESTOQUE ALTO!)"
        print(f"{cod} - {prod['nome']}: {prod['quantidade']} {prod['unidade']}{alerta}")

def relatorio_vendas():
    print("\n--- RELATÓRIO DE VENDAS ---")
    if not vendas:
        print("Nenhuma venda realizada.")
        return

    for venda in vendas:
        data_formatada = f"{venda['data'][:2]}/{venda['data'][2:4]}/{venda['data'][4:]}"
        print(f"\nID Venda: {venda['id']} | Data: {data_formatada}")
        vendedor_nome = vendedores.get(venda['vendedor'], {}).get('nome', 'Vendedor não encontrado')
        print(f"Vendedor: {vendedor_nome}")
        if venda['cliente']:
            cliente_nome = clientes.get(venda['cliente'], {}).get('nome', 'Cliente não encontrado')
            print(f"Cliente: {cliente_nome}")
        print("Itens:")
        for item in venda['itens']:
            prod = produtos.get(item['codigo'], None)
            if prod:
                print(f"- {prod['nome']}: {item['quantidade']} x R$ {prod['preco_venda']:.2f} = R$ {item['subtotal']:.2f}")
            else:
                print(f"- Código {item['codigo']} - Produto não encontrado.")
        print(f"Total: R$ {venda['total']:.2f} | Forma: {venda['forma_pagamento']}")
        print(f"Comissão do Vendedor: R$ {venda['comissao']:.2f}")

def relatorio_vendedores():
    print("\n--- RELATÓRIO DE VENDEDORES ---")
    if not vendedores:
        print("Nenhum vendedor cadastrado.")
        return
        
    for id_vend, vend in vendedores.items():
        print(f"\nID: {id_vend} | Nome: {vend['nome']}")
        print(f"Total vendas: R$ {vend['vendas']:.2f}")
        print(f"Comissão acumulada: R$ {vend['comissao']:.2f}")

def relatorio_clientes():
    print("\n--- RELATÓRIO DE CLIENTES ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
        
    for cpf, cli in clientes.items():
        print(f"\nCPF: {cpf}")
        print(f"Nome: {cli['nome']}")
        print(f"Telefone: {cli['telefone']}")
        print(f"E-mail: {cli['email']}")
        print(f"Endereço: {cli['endereco']}")

def relatorio_orcamentos():
    print("\n--- RELATÓRIO DE ORÇAMENTOS PENDENTES ---")
    if not orcamentos:
        print("Nenhum orçamento pendente.")
        return
    
    for id_orc, orc in orcamentos.items():
        data_formatada = f"{orc['data'][:2]}/{orc['data'][2:4]}/{orc['data'][4:]}"
        vendedor_nome = vendedores.get(orc['vendedor'], {}).get('nome', 'Vendedor não encontrado')
        print(f"\nID Orçamento: {id_orc} | Data: {data_formatada} | Vendedor: {vendedor_nome}")
        if orc['cliente']:
            cliente_nome = clientes.get(orc['cliente'], {}).get('nome', 'Cliente não encontrado')
            print(f"Cliente: {cliente_nome}")
        print(f"Total: R$ {orc['total']:.2f}")
        print("Itens:")
        for item in orc['itens']:
            prod = produtos.get(item['codigo'], None)
            if prod:
                print(f"- {prod['nome']}: {item['quantidade']} unidades")
            else:
                print(f"- Código {item['codigo']} - Produto não encontrado.")

def relatorio_contas_receber():
    print("\n--- RELATÓRIO DE CONTAS A RECEBER (CREDIÁRIO) ---")
    if not contas_a_receber:
        print("Nenhuma conta a receber pendente.")
        return

    tem_contas_pendentes = False
    for id_venda, conta in contas_a_receber.items():
        if conta['pendente'] > 0:
            tem_contas_pendentes = True
            cliente_nome = clientes.get(conta['cliente_cpf'], {}).get('nome', 'Cliente não cadastrado')
            print(f"\nID Venda: {id_venda} | Cliente: {cliente_nome}")
            print(f"Total da venda: R$ {conta['total']:.2f}")
            print(f"Total pago: R$ {conta['pago']:.2f}")
            print(f"Valor pendente: R$ {conta['pendente']:.2f}")
    
    if not tem_contas_pendentes:
        print("Todas as contas de crediário foram quitadas.")

# MENU PRINCIPAL
def menu_principal():
    carregar_dados()
    
    while True:
        print("\n=== SISTEMA CONSTRUÇÃO FÁCIL ===")
        print("\n===== CADASTROS =====")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Produto")
        print("3. Cadastrar Vendedor")
        print("\n===== OPERAÇÕES DA LOJA =====")
        print("4. Realizar Venda")
        print("5. Fazer Orçamento")
        print("6. Converter Orçamento em Venda")
        print("7. Registrar Devolução/Troca")
        print("8. Registrar Pagamento de Crediário")
        print("\n===== RELATÓRIOS =====")
        print("9. Relatório de Estoque")
        print("10. Relatório de Vendas")
        print("11. Relatório de Vendedores")
        print("12. Relatório de Clientes")
        print("13. Relatório de Orçamentos")
        print("14. Relatório de Contas a Receber")
        print("\n===== SISTEMA =====")
        print("0. Sair")
        
        opcao = input("Opção: ").strip()
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_produto()
        elif opcao == "3":
            cadastrar_vendedor()
        elif opcao == "4":
            realizar_venda()
        elif opcao == "5":
            realizar_orcamento()
        elif opcao == "6":
            converter_orcamento_em_venda()
        elif opcao == "7":
            registrar_devolucao_troca()
        elif opcao == "8":
            registrar_pagamento_crediario()
        elif opcao == "9":
            relatorio_estoque()
        elif opcao == "10":
            relatorio_vendas()
        elif opcao == "11":
            relatorio_vendedores()
        elif opcao == "12":
            relatorio_clientes()
        elif opcao == "13":
            relatorio_orcamentos()
        elif opcao == "14":
            relatorio_contas_receber()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# MAIN
if __name__ == "__main__":
    menu_principal()