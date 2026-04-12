class Consumidor:
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    def cadastrar(self):
        print(f"Consumidor {self.nome} cadastrado")

class ServiceOferecido:
    def __init__(self, codigo, nome, descricao, tempo, preco):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.tempo = tempo
        self.preco = preco
    
    def mostrar(self):
        print(f"Serviço: {self.nome}")

class Tecnico:
    def __init__(self, nome, especialidade, contato):
        self.nome = nome
        self.especialidade = especialidade
        self.contato = contato
        self.disponivel = True
    
    def ver_disponibilidade(self):
        return self.disponivel

class ReservaService:
    def __init__(self, codigo, consumidor, data, hora):
        self.codigo = codigo
        self.consumidor = consumidor
        self.data = data
        self.hora = hora
        self.status = "Pendente"
        self.servicos = []
        self.tecnico = None
    
    def add_servico(self, servico):
        self.servicos.append(servico)
        print(f"Serviço {servico.nome} adicionado")
    
    def add_tecnico(self, tecnico):
        self.tecnico = tecnico
        print(f"Técnico {tecnico.nome} designado")
    
    def confirmar(self):
        self.status = "Confirmada"
        print("Reserva confirmada")

class PagamentoService:
    def __init__(self, id_pagamento, reserva, forma_pagamento, data):
        self.id_pagamento = id_pagamento
        self.reserva = reserva
        self.forma_pagamento = forma_pagamento
        self.data = data
        self.status = "Pendente"
    
    def pagar(self):
        self.status = "Pago"
        print("Pagamento realizado")
    
    def emitir_recibo(self):
        print(f"Recibo #{self.id_pagamento}")
        print(f"Cliente: {self.reserva.consumidor.nome}")

# Teste
consumidor1 = Consumidor("João", "999888777", "11988887777", "joao@email.com", "Rua B, 456")
servico1 = ServiceOferecido("S001", "Instalação", "Instalação de software", 60, 100)
tecnico1 = Tecnico("Carlos", "TI", "11977776666")

reserva1 = ReservaService("RS001", consumidor1, "01/11/2025", "14:00")
reserva1.add_servico(servico1)
reserva1.add_tecnico(tecnico1)
reserva1.confirmar()

pagamento1 = PagamentoService("PS001", reserva1, "Dinheiro", "01/11/2025")
pagamento1.pagar()
pagamento1.emitir_recibo()