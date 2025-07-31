# Sistema de Gerenciamento para Loja de Materiais de Construção
import os
from datetime import datetime

# Arquivos para salvar os dados
ARQUIVO_PRODUTOS = "produtos.txt"
ARQUIVO_CLIENTES = "clientes.txt"
ARQUIVO_VENDAS = "vendas.txt"

# Dados em memória
produtos = {}
clientes = {}
vendas = []

# Função para validar data
def obter_data():
    while True:
        data_str = input("Data da venda (DDMMAAAA): ").strip()
        if len(data_str) != 8 or not data_str.isdigit():
            print("Formato inválido. Digite 8 números (DDMMAAAA).")
            continue
        
        try:
            dia = int(data_str[:2])
            mes = int(data_str[2:4])
            ano = int(data_str[4:])
            datetime(ano, mes, dia)  # Testa se a data existe
            return data_str
        except ValueError:
            print("Data inválida. Verifique dia, mês e ano.")

# Função para cadastrar produto
def cadastrar_produto():
    print("\n--- Cadastrar Produto ---")
    codigo = input("Código do produto: ").strip()
    nome = input("Nome: ").strip()
    preco = float(input("Preço de venda: R$ "))
    quantidade = int(input("Quantidade em estoque: "))
    
    produtos[codigo] = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    print(f"Produto '{nome}' cadastrado com sucesso!")

# Função para realizar venda
def realizar_venda():
    print("\n--- Nova Venda ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    data = obter_data()
    cpf_cliente = input("CPF do cliente (opcional): ").strip()
    
    itens = []
    total = 0
    
    while True:
        print("\nProdutos disponíveis:")
        for cod, prod in produtos.items():
            print(f"{cod}: {prod['nome']} - R$ {prod['preco']} | Estoque: {prod['quantidade']}")
        
        codigo = input("\nCódigo do produto (ou 'sair'): ").lower()
        if codigo == 'sair':
            break
        
        if codigo not in produtos:
            print("Código inválido.")
            continue
        
        produto = produtos[codigo]
        qtd = int(input(f"Quantidade de {produto['nome']}: "))
        
        if qtd > produto['quantidade']:
            print(f"Estoque insuficiente. Disponível: {produto['quantidade']}")
            continue
        
        subtotal = produto['preco'] * qtd
        itens.append({
            'codigo': codigo,
            'quantidade': qtd,
            'subtotal': subtotal
        })
        total += subtotal
        produto['quantidade'] -= qtd  # Atualiza estoque
    
    if not itens:
        print("Nenhum item adicionado. Venda cancelada.")
        return
    
    print("\nResumo da Venda:")
    for item in itens:
        prod = produtos[item['codigo']]
        print(f"{prod['nome']}: {item['quantidade']} x R$ {prod['preco']} = R$ {item['subtotal']}")
    
    print(f"\nTOTAL: R$ {total:.2f}")
    vendas.append({
        'data': data,
        'cliente': cpf_cliente,
        'itens': itens,
        'total': total
    })
    print("Venda registrada com sucesso!")

# Função para salvar dados em arquivos
def salvar_dados():
    with open(ARQUIVO_PRODUTOS, 'w') as f:
        for cod, prod in produtos.items():
            f.write(f"{cod};{prod['nome']};{prod['preco']};{prod['quantidade']}\n")
    
    with open(ARQUIVO_VENDAS, 'w') as f:
        for venda in vendas:
            f.write(f"{venda['data']};{venda['cliente']};{venda['total']}\n")
    
    print("Dados salvos com sucesso!")

# Menu principal
def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar Produto")
        print("2. Realizar Venda")
        print("3. Salvar Dados")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            realizar_venda()
        elif opcao == "3":
            salvar_dados()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar sistema
if __name__ == "__main__":
    print("=== SISTEMA CONSTRUÇÃO FÁCIL ===")
    menu()