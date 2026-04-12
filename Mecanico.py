class Mecanico:
    def __init__(self, nome, matricula, nivel):
        self.nome = nome
        self.matricula = matricula
        self.nivel = nivel
        self.salario = 0
 
    def passar_orcamento(self):
        print("Seu carro ficou tanto...")
   
    def realizar_diagnostico(self):
        print(f"{self.nome} diagnosticando o veículo...")
 
    def get_salario(self):
        return self.salario
   
    def set_salario(self, valor):
        self.salario = valor
 
    def calcular_comissao(self,servicos):
        comissao = servicos * 0.15
        self.salario += comissao
        return True
 
mec1 = Mecanico("Carlos", "1234", "N1")
mec1.passar_orcamento()
mec1.realizar_diagnostico()
sal = mec1.get_salario()
print(sal)
 
mec2 = Mecanico("João", "4321", "N2")
mec2.set_salario(9000)
x = mec2.get_salario()
print(f"Salário do {mec2.nome} é {mec2.salario}")
 
mec1.set_salario(5000)
print(sal)
 
sal = mec1.get_salario()
print(sal)
 
mec1.calcular_comissao(9000)
print(f"Salario Atual do {mec1.nome} é R$ {mec1.get_salario()}")
 