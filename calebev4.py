# Sistema Completo para Construção Fácil com Persistência em Arquivos
import os
from datetime import datetime

# Arquivos de dados
ARQUIVO_ESTOQUE = "estoque.txt"
ARQUIVO_VENDEDORES = "vendedores.txt"
ARQUIVO_CLIENTES = "clientes.txt"
ARQUIVO_VENDAS = "vendas.txt"

# Dados em memória
estoque = {}
vendedores = {}
clientes = {}
vendas = []

# ========== FUNÇÕES DE VALIDAÇÃO ==========
def validar_cpf(cpf):
    """Valida CPF com dígitos verificadores"""
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    # Cálculo do 1º dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    if digito1 >= 10:
        digito1 = 0
    
    # Cálculo do 2º dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    if digito2 >= 10:
        digito2 = 0
    
    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2

def obter_data(mensagem):
    """Valida data no formato DDMMAAAA usando datetime"""
    while True:
        data_str = input(f"{mensagem} (DDMMAAAA): ").strip()
        if len(data_str) != 8 or not data_str.isdigit():
            print("⚠️ Use 8 dígitos (DDMMAAAA). Ex: 15072023")
            continue
        
        try:
            dia, mes, ano = int(data_str[:2]), int(data_str[2:4]), int(data_str[4:])
            datetime(ano, mes, dia)  # Testa se a data é válida
            return data_str
        except ValueError as e:
            print(f"⛔ Data inválida: {e}. Tente novamente.")

def obter_numero(mensagem, inteiro=False):
    """Valida números (positivos)"""
    while True:
        try:
            valor = float(input(mensagem)) if not inteiro else int(input(mensagem))
            return valor if valor >= 0 else print("⚠️ O valor não pode ser negativo.")
        except ValueError:
            print("⚠️ Digite um número válido.")

def obter_texto(mensagem, permitir_numeros=False, tamanho_min=1):
    """Valida textos"""
    while True:
        texto = input(mensagem).strip()
        if len(texto) < tamanho_min:
            print(f"⚠️ Mínimo de {tamanho_min} caracteres.")
            continue
        if not permitir_numeros and texto.isdigit():
            print("⚠️ Este campo não aceita apenas números.")
            continue
        return texto

# ========== PERSISTÊNCIA DE DADOS ==========
def carregar_dados():
    """Carrega dados dos arquivos"""
    def carregar(arquivo, campos):
        dados = {}
        if os.path.exists(arquivo):
            with open(arquivo, 'r', encoding='utf-8') as f:
                for linha in f:
                    valores = linha.strip().split(';')
                    if len(valores) == len(campos):
                        dados[valores[0]] = dict(zip(campos[1:], valores[1:]))
        return dados

    global estoque, vendedores, clientes, vendas
    estoque = carregar(ARQUIVO_ESTOQUE, ['codigo', 'nome', 'descricao', 'categoria', 'unidade', 'custo', 'venda', 'estoque_min', 'estoque_max', 'quantidade'])
    vendedores = carregar(ARQUIVO_VENDEDORES, ['id', 'nome', 'cpf', 'telefone', 'email', 'vendas', 'comissao'])
    clientes = carregar(ARQUIVO_CLIENTES, ['cpf', 'nome', 'telefone', 'email', 'endereco'])
    
    # Carregar vendas
    if os.path.exists(ARQUIVO_VENDAS):
        with open(ARQUIVO_VENDAS, 'r', encoding='utf-8') as f:
            vendas = [eval(linha.strip()) for linha in f]

def salvar_dados():
    """Salva todos os dados em arquivos"""
    def salvar(arquivo, dados):
        with open(arquivo, 'w', encoding='utf-8') as f:
            for chave, valores in dados.items():
                f.write(f"{chive};{';'.join(str(v) for v in valores.values())}\n")

    salvar(ARQUIVO_ESTOQUE, estoque)
    salvar(ARQUIVO_VENDEDORES, vendedores)
    salvar(ARQUIVO_CLIENTES, clientes)
    
    with open(ARQUIVO_VENDAS, 'w', encoding='utf-8') as f:
        for venda in vendas:
            f.write(f"{repr(venda)}\n")

# ========== FUNÇÕES PRINCIPAIS ==========
def cadastrar_produto():
    print("\n📦 CADASTRAR PRODUTO")
    produto = {
        'codigo': obter_texto("Código: ", True, 3),
        'nome': obter_texto("Nome: ", tamanho_min=3),
        'descricao': obter_texto("Descrição: "),
        'categoria': obter_texto("Categoria (elétrica/hidráulica/ferragens/básico): "),
        'unidade': obter_texto("Unidade (kg/m2/peça/saco): "),
        'custo': obter_numero("Custo R$: "),
        'venda': obter_numero("Venda R$: "),
        'estoque_min': obter_numero("Estoque mínimo: ", True),
        'estoque_max': obter_numero("Estoque máximo: ", True),
        'quantidade': obter_numero("Quantidade: ", True)
    }
    estoque[produto['codigo']] = produto
    print(f"✅ Produto {produto['nome']} cadastrado!")

def realizar_venda():
    print("\n💰 REALIZAR VENDA")
    if not estoque:
        print("⛔ Nenhum produto cadastrado.")
        return
    
    venda = {
        'id': len(vendas) + 1,
        'data': obter_data("Data"),
        'vendedor': obter_texto("ID do vendedor: ", True),
        'cliente': obter_cpf("CPF do cliente (opcional): ") or "",
        'itens': [],
        'total': 0
    }
    
    # Seleção de produtos
    while True:
        print("\n🛒 Produtos disponíveis:")
        for cod, p in estoque.items():
            print(f"[{cod}] {p['nome']} - R${p['venda']} | Estoque: {p['quantidade']}")
        
        codigo = input("\n▶ Código do produto (ou 'finalizar'): ").lower()
        if codigo == 'finalizar':
            if not venda['itens']:
                print("⛔ Adicione ao menos 1 item.")
                continue
            break
            
        if codigo not in estoque:
            print("⛔ Código inválido.")
            continue
            
        produto = estoque[codigo]
        qtd = obter_numero(f"Quantidade de {produto['nome']}: ", True)
        
        if qtd > produto['quantidade']:
            print(f"⛔ Estoque insuficiente (disponível: {produto['quantidade']}).")
            continue
            
        desconto = obter_numero("Desconto R$ (0 se nenhum): ")
        subtotal = (produto['venda'] * qtd) - desconto
        
        venda['itens'].append({
            'codigo': codigo,
            'quantidade': qtd,
            'preco': produto['venda'],
            'desconto': desconto,
            'subtotal': subtotal
        })
        
        venda['total'] += subtotal
        produto['quantidade'] -= qtd  # Baixa no estoque
    
    # Forma de pagamento
    formas = {'1': 'dinheiro', '2': 'cartão', '3': 'pix', '4': 'boleto', '5': 'crediário'}
    print("\n💳 Formas de pagamento:")
    for op, forma in formas.items():
        print(f"{op}. {forma.capitalize()}")
    
    while True:
        opcao = input("▶ Escolha: ")
        if opcao in formas:
            venda['forma_pagamento'] = formas[opcao]
            break
        print("⛔ Opção inválida.")
    
    # Cálculo de comissão
    comissao = venda['total'] * (0.03 if venda['forma_pagamento'] == 'cartão' else 0.05)
    if venda['vendedor'] in vendedores:
        vendedores[venda['vendedor']]['comissao'] += comissao
    
    vendas.append(venda)
    print(f"\n✅ Venda registrada! Total: R${venda['total']:.2f}")

# (Continua com as outras funções: relatórios, menu principal, etc...)

# ========== MENU PRINCIPAL ==========
def menu_principal():
    carregar_dados()
    while True:
        print("\n🏠 CONSTRUÇÃO FÁCIL - MENU PRINCIPAL")
        print("1. 📦 Cadastrar Produto")
        print("2. 👔 Cadastrar Vendedor")
        print("3. 👤 Cadastrar Cliente")
        print("4. 💰 Realizar Venda")
        print("5. 📊 Relatórios")
        print("6. 💾 Salvar Dados")
        print("0. 🚪 Sair")
        
        opcao = input("▶ Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "4":
            realizar_venda()
        # (Adicione outras opções aqui)
        elif opcao == "0":
            if input("Salvar antes de sair? (s/n): ").lower() == 's':
                salvar_dados()
            print("👋 Até logo!")
            break
        else:
            print("⛔ Opção inválida!")

if __name__ == "__main__":
    print("🏗️ BEM-VINDO AO SISTEMA CONSTRUÇÃO FÁCIL")
    menu_principal()