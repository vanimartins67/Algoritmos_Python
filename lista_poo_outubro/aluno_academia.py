class AlunoAcademia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120.00):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade
    
    def calcular_IMC(self):
        imc = self.peso / (self.altura ** 2)
        print(f"IMC de {self.nome}: {imc:.2f}")
        return imc
    
    def obter_valor_mensalidade(self):
        if self.idade < 18:
            mensalidade_com_desconto = self.mensalidade * 0.8  # 20% de desconto
            print(f"Aluno menor de idade - Mensalidade com desconto: R$ {mensalidade_com_desconto:.2f}")
            return mensalidade_com_desconto
        else:
            print(f"Mensalidade: R$ {self.mensalidade:.2f}")
            return self.mensalidade

print("\n" + "="*50)
print("8 - CLASSE ALUNO_ACADEMIA")
print("="*50)
aluno_acad1 = AlunoAcademia("João", 16, 65, 1.75)
aluno_acad1.calcular_IMC()
aluno_acad1.obter_valor_mensalidade()