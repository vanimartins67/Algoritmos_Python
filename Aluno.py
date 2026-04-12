class Aluno:
    def __init__(self, nome, ra):
        self.nome = nome
        self.ra = ra

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno:object):
        self.alunos.append(aluno)

    def lista_alunos(self):
        for item in self.alunos:
            print(f"Nome: {item.nome} | RA: {item.ra}")

a1 = Aluno("CARLOS","4321")
a2 = Aluno("TESMAN","1234")
a3 = Aluno("FABIO","1324")
a4 = Aluno("ALLAN", "1432")

faculdade = Universidade("SENAC MS")
print(len(faculdade.alunos))
faculdade.adicionar_aluno(a1)
faculdade.adicionar_aluno(a2)
faculdade.adicionar_aluno(a3)
faculdade.adicionar_aluno(a4)
print(len(faculdade.alunos))

print("ALUNOS DA: ", faculdade.nome)
for aluno in faculdade.alunos:
    print(aluno.nome)