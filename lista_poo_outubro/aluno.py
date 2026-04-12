class Aluno:
    def __init__(self, nome, ra, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
    
    def mostrar_situacao(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
                
        if media >= 7:
            return "APROVADO"
        elif media >= 5:
            return "EXAME"
        else:
            return "REPROVADO"

aluno1 = Aluno("Maria Santos", "2023001", 8.0, 7.5, 6.0, 9.0)
aluno2 = Aluno("Pedro Costa", "2023002", 4.0, 5.0, 3.5, 4.5)
print(f"Aluno: {aluno1.nome} - RA: {aluno1.ra}")
print(f"Situação: {aluno1.mostrar_situacao()}")
print(f"Aluno: {aluno2.nome} - RA: {aluno2.ra}")
print(f"Situação: {aluno2.mostrar_situacao()}")
print()