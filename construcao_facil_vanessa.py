import os
from datetime import datetime
import re

ARQUIVO_PRODUTOS = "produtos.txt"
ARQUIVO_VENDEDORES = "vendedores.txt"
ARQUIVO_CLIENTES = "clientes.txt"
ARQUIVO_VENDAS = "vendas.txt"

produtos = {}
vendedores = {}
clientes = {}
vendas = []

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
    nome = input("Nome completo: ").strip()
    cpf = input("CPF (11 dígitos): ").strip()
    while not validar_cpf(cpf):
        print("CPF inválido! Por favor, digite um CPF válido.")
        cpf = input("CPF (11 dígitos): ").strip()
    
    vendedores[id_vendedor] = {'nome': nome, 'cpf': cpf, 'vendas': 0.0, 'comissao': 0.0}
    salvar_automaticamente()
    print(f"Vendedor {nome} cadastrado!")

# OPERAÇÕES DA LOJA
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
    
    itens = []
    total = 0.0
    
    while True:
        print("\nProdutos disponíveis:")
        for cod, prod in produtos.items():
            print(f"{cod} - {prod['nome']} | R$ {prod['preco_venda']:.2f} | Estoque: {prod['quantidade']}")
        
        codigo = input("\nCódigo do produto (ou 'finalizar'): ").strip().lower()
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
            if qtd > produto['quantidade']:
                print(f"Estoque insuficiente! Disponível: {produto['quantidade']}")
                continue
                
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
            produto['quantidade'] -= qtd
            
        except ValueError:
            print("Valor inválido! Digite um número.")
    
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
    
    vendas.append({
        'data': data, 'vendedor': id_vendedor, 'cliente': cpf_cliente,
        'itens': itens, 'total': total,
        'forma_pagamento': forma_pagamento, 'comissao': comissao
    })
    salvar_automaticamente()
    print(f"\nVENDA CONCLUÍDA! Total: R$ {total:.2f}")
    print(f"Comissão do vendedor: R$ {comissao:.2f}")

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
        
        print(f"\nData: {data_formatada}")
        
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
        print("5. Relatório de Estoque")
        print("6. Relatório de Vendas")
        print("7. Relatório de Vendedores")
        print("8. Relatório de Clientes")
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
            relatorio_estoque()
        elif opcao == "6":
            relatorio_vendas()
        elif opcao == "7":
            relatorio_vendedores()
        elif opcao == "8":
            relatorio_clientes()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# MAIN
if __name__ == "__main__":
    menu_principal()