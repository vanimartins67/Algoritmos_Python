class Estudante: ##nome de classe
    def __init__(self, nome, idade, nota): ##método construtor
        self.nome = nome ##atributo
        self.idade = idade #atributo
        self.nota = nota

    def get_grade(self):
        print(self.nota)


e1 = Estudante("Luis", 20, 10) 
e2 = Estudante("Jow", 48, 10)

print(e1) 
    