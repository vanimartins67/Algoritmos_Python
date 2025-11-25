class ClienteVip:
    def __init__(self, id_cliente, nome, cpf, email, celular):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.celular = celular
    
    def cadastrar(self):
        print(f"Cliente {self.nome} cadastrado")
    
    def atualizar(self, novo_email, novo_celular):
        self.email = novo_email
        self.celular = novo_celular

class ProdutoEstoque:
    def __init__(self, codigo, nome, descricao, preco, estoque):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
    
    def atualizar_estoque(self, novo_estoque):
        self.estoque = novo_estoque
    
    def mostrar(self):
        print(f"{self.nome} - R$ {self.preco}")

class OrdemCompra:
    def __init__(self, numero, cliente, data):
        self.numero = numero
        self.cliente = cliente
        self.data = data
        self.itens = []
        self.total = 0
        self.status = "Aberta"
    
    def add_item(self, produto, qtd):
        if produto.estoque >= qtd:
            item = ItemOrdem(produto, qtd)
            self.itens.append(item)
            produto.estoque -= qtd
            self.calcular_total()
            print(f"Item {produto.nome} adicionado")
        else:
            print("Estoque insuficiente")
    
    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item.subtotal
        self.total = total

class ItemOrdem:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = produto.preco
        self.subtotal = self.preco_unitario * quantidade

class TransacaoFinanceira:
    def __init__(self, id_transacao, ordem, forma_pagamento, data):
        self.id_transacao = id_transacao
        self.ordem = ordem
        self.forma_pagamento = forma_pagamento
        self.data = data
        self.valor = ordem.total
        self.status = "Pendente"
    
    def processar(self):
        self.status = "Paga"
        print("Pagamento processado")
    
    def recibo(self):
        print(f"Recibo #{self.id_transacao}")
        print(f"Cliente: {self.ordem.cliente.nome}")
        print(f"Valor: R$ {self.valor}")

# Teste
cliente1 = ClienteVip("C001", "Maria", "111222333", "maria@email.com", "11999998888")
produto1 = ProdutoEstoque("P001", "Tablet", "Tablet 10 polegadas", 800, 5)

ordem1 = OrdemCompra("OC001", cliente1, "30/10/2025")
ordem1.add_item(produto1, 1)
ordem1.calcular_total()

pagamento1 = TransacaoFinanceira("T001", ordem1, "Cartão", "30/10/2025")
pagamento1.processar()
pagamento1.recibo()