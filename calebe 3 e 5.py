#03
class AlunoCurso:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def situacao(self):
        media = self.media()
        if media >= 6.0:  
            return "Aprovado"
        else:
            return "Reprovado"

alunos = [
    AlunoCurso("001", "Ana", 7.5, 8.0, 6.5),
    AlunoCurso("002", "João", 5.0, 4.5, 6.0),
    AlunoCurso("003", "Maria", 8.0, 8.5, 7.5),
    AlunoCurso("004", "Pedro", 6.0, 5.5, 6.5),
    AlunoCurso("005", "Carla", 7.0, 7.5, 7.0)
]

maior_media = alunos[0]
for aluno in alunos:
    if aluno.media() > maior_media.media():
        maior_media = aluno

menor_media = alunos[0]
for aluno in alunos:
    if aluno.media() < menor_media.media():
        menor_media = aluno

print(f"Aluno com maior média: {maior_media.nome} - Média: {maior_media.media()}") 
print(f"Aluno com menor média: {menor_media.nome} - Média: {menor_media.media()}")  

print("\nSituação dos alunos:")
for aluno in alunos:
    print(f"{aluno.nome}: Média = {aluno.media()} - {aluno.situacao()}")  


#05
class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto  
        self.segundo = segundo

    def incrementar_segundos(self, segundos):
        total_segundos = self.hora * 3600 + self.minuto * 60 + self.segundo + segundos
        self.hora = total_segundos // 3600
        self.minuto = (total_segundos % 3600) // 60
        self.segundo = total_segundos % 60
        # ERRO: não trata caso onde hora > 23

    def diferenca(self, outro):
        segundos_self = self.hora * 3600 + self.minuto * 60 + self.segundo
        segundos_outro = outro.hora * 3600 + outro.minuto * 60 + outro.segundo
        return abs(segundos_self - segundos_outro)

    def __str__(self):
        return f"{self.hora}:{self.minuto}:{self.segundo}"

h1 = Horario(8, 5, 30)
h2 = Horario(14, 20, 15)
print(f"Horário 1: {h1}")
print(f"Horário 2: {h2}")
h1.incrementar_segundos(7200)
print(f"Horário 1 após incremento: {h1}")
print(f"Diferença em segundos: {h1.diferenca(h2)}")
h3 = Horario(23, 59, 59)
h3.incrementar_segundos(3600) 
print(f"Horário 3 após incremento: {h3}")
print()