class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
    
    def nome_completo(self):
        nome_completo = f"{self.nome} {self.sobrenome}"
        print(f"Nome completo: {nome_completo}")
        return nome_completo
    
    def calcular_salario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        print(f"Salário: R$ {salario:.2f}")
        return salario
    
    def incrementar_horas(self, horas):
        self.horas_trabalhadas += horas
        print(f"Horas incrementadas em {horas}. Total: {self.horas_trabalhadas} horas")

func1 = Funcionario("Ana", "Pereira", 160, 25.50)
func1.nome_completo()
func1.calcular_salario()
func1.incrementar_horas(10)
func1.calcular_salario()
print()