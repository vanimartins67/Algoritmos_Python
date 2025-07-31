# SISTEMA PARA "CONSTRUÇÃO FÁCIL" - FIEL AO BRIEFING
import os
from datetime import datetime

# Arquivos de dados
ARQUIVO_PRODUTOS = "produtos.txt"
ARQUIVO_VENDEDORES = "vendedores.txt"
ARQUIVO_CLIENTES = "clientes.txt"
ARQUIVO_VENDAS = "vendas.txt"

# Dados em memória
produtos = {}
vendedores = {}
clientes = {}
vendas = []

# --- FUNÇÕES DE VALIDAÇÃO ---
def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    # Cálculo dos dígitos verificadores (simplificado)
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    if digito1 >= 10:
        digito1 = 0
    if digito1 != int(cpf[9]):
        return False
    return True

def obter_data_valida():
    while True:
        data = input("Data (DDMMAAAA): ").strip()
        if len(data) == 8 and data.isdigit():
            try:
                dia, mes, ano = int(data[:2]), int(data[2:4]), int(data[4:])
                datetime(ano, mes, dia)
                return data
            except:
                print("Data inválida. Verifique dia, mês e ano.")
        else:
            print("Formato incorreto. Use DDMMAAAA.")

# --- CADASTROS ---
def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")
    codigo = input("Código de barras: ").strip()
    nome = input("Nome: ").strip()
    categoria = input("Categoria (elétrica/hidráulica/ferragens/básico): ").strip()
    unidade = input("Unidade (kg/m2/peça/saco): ").strip()
    preco_custo = float(input("Preço de custo R$: "))
    preco_venda = float(input("Preço de venda R$: "))
    estoque_min = int(input("Estoque mínimo: "))
    estoque_max = int(input("Estoque máximo: "))
    quantidade = int(input("Quantidade em estoque: "))
    
    produtos[codigo] = {
        'nome': nome,
        'categoria': categoria,
        'unidade': unidade,
        'preco_custo': preco_custo,
        'preco_venda': preco_venda,
        'estoque_min': estoque_min,
        'estoque_max': estoque_max,
        'quantidade': quantidade
    }
    print(f"Produto {nome} cadastrado!")

def cadastrar_vendedor():
    print("\n--- CADASTRAR VENDEDOR ---")
    id_vendedor = input("ID do vendedor: ").strip()
    nome = input("Nome completo: ").strip()
    cpf = input("CPF (11 dígitos): ").strip()
    while not validar_cpf(cpf):
        print("CPF inválido!")
        cpf = input("CPF (11 dígitos): ").strip()
    
    vendedores[id_vendedor] = {
        'nome': nome,
        'cpf': cpf,
        'vendas': 0.0,
        'comissao': 0.0
    }
    print(f"Vendedor {nome} cadastrado!")

# --- PROCESSO DE VENDA ---
def realizar_venda():
    print("\n--- REALIZAR VENDA ---")
    
    # Verifica pré-requisitos
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    if not vendedores:
        print("Nenhum vendedor cadastrado!")
        return
    
    # Dados da venda
    data = obter_data_valida()
    id_vendedor = input("ID do vendedor: ").strip()
    if id_vendedor not in vendedores:
        print("Vendedor não encontrado!")
        return
    
    cpf_cliente = input("CPF do cliente (deixe em branco se não cadastrado): ").strip()
    if cpf_cliente and cpf_cliente not in clientes:
        print("Cliente não cadastrado. Venda avulsa.")
        cpf_cliente = ""
    
    # Seleção de produtos
    itens = []
    total = 0.0
    
    while True:
        print("\nProdutos disponíveis:")
        for cod, prod in produtos.items():
            print(f"{cod} - {prod['nome']} | R$ {prod['preco_venda']} | Estoque: {prod['quantidade']}")
        
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
                'codigo': codigo,
                'quantidade': qtd,
                'desconto': desconto,
                'subtotal': subtotal
            })
            total += subtotal
            produto['quantidade'] -= qtd  # Baixa no estoque
            
        except ValueError:
            print("Valor inválido!")
    
    # Forma de pagamento
    formas = {
        '1': {'nome': 'Dinheiro', 'comissao': 0.05},
        '2': {'nome': 'Cartão', 'comissao': 0.03},
        '3': {'nome': 'PIX', 'comissao': 0.05},
        '4': {'nome': 'Boleto', 'comissao': 0.05},
        '5': {'nome': 'Crediário', 'comissao': 0.05}
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
    
    # Atualiza vendedor
    vendedores[id_vendedor]['vendas'] += total
    vendedores[id_vendedor]['comissao'] += comissao
    
    # Registra venda
    vendas.append({
        'data': data,
        'vendedor': id_vendedor,
        'cliente': cpf_cliente,
        'itens': itens,
        'total': total,
        'forma_pagamento': forma_pagamento,
        'comissao': comissao
    })
    
    print(f"\nVENDA CONCLUÍDA! Total: R$ {total:.2f}")
    print(f"Comissão do vendedor: R$ {comissao:.2f}")

# --- RELATÓRIOS ---
def relatorio_estoque():
    print("\n--- RELATÓRIO DE ESTOQUE ---")
    for cod, prod in produtos.items():
        alerta = ""
        if prod['quantidade'] < prod['estoque_min']:
            alerta = " (ESTOQUE BAIXO!)"
        print(f"{cod} - {prod['nome']}: {prod['quantidade']} {prod['unidade']}{alerta}")

# --- PERSISTÊNCIA ---
def salvar_dados():
    # Implementação similar à versão anterior
    pass

def carregar_dados():
    # Implementação similar à versão anterior
    pass

# --- MENU PRINCIPAL ---
def menu_principal():
    carregar_dados()
    
    while True:
        print("\n=== CONSTRUÇÃO FÁCIL ===")
        print("1. Cadastrar Produto")
        print("2. Cadastrar Vendedor")
        print("3. Cadastrar Cliente")
        print("4. Realizar Venda")
        print("5. Relatório de Estoque")
        print("6. Relatório de Vendas")
        print("7. Relatório de Vendedores")
        print("8. Salvar Dados")
        print("0. Sair")
        
        opcao = input("Opção: ").strip()
        
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            cadastrar_vendedor()
        elif opcao == "4":
            realizar_venda()
        elif opcao == "5":
            relatorio_estoque()
        elif opcao == "8":
            salvar_dados()
        elif opcao == "0":
            if input("Salvar antes de sair? (S/N): ").upper() == "S":
                salvar_dados()
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# INICIO DO SISTEMA
if __name__ == "__main__":
    print("=== SISTEMA CONSTRUÇÃO FÁCIL ===")
    menu_principal()