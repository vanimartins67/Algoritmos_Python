turma = int(input("Digite o número de pessoas: "))
soma_idades = 0
for i in range(turma):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    soma_idades = soma_idades + idade
media = soma_idades / turma
if media <= 25:
    classificacao = "Turma Jovem"
elif 26 <= media <= 60:
    classificacao = "Turma Adulta"
else:
    classificacao = "Turma Idosa"
print(f"A média de idade da turma é {media:.1f} anos, portanto é classificada como {classificacao}.")


eleitores = int(input("Digite o número de eleitores: "))
candidato1 = 0
candidato2 = 0
candidato3 = 0
print("Para votar no candidato 1, vote 1")
print("Para votar no candidato 2, vote 2")
print("Para votar no candidato 3, vote 3")
for i in range(eleitores):
    voto = int(input(f"Digite seu voto {i + 1}: "))
    if voto == 1:
        candidato1 = candidato1 + 1
    elif voto == 2:
        candidato2 = candidato2 + 1
    elif voto == 3:
        candidato3 = candidato3 + 1
    else:
        print("Voto inválido! (Digite 1, 2 ou 3)")
print("\nResultado da eleição")
print(f"Candidato 1: {candidato1}")
print(f"Candidato 2: {candidato2}")
print(f"Candidato 3: {candidato3}")
if candidato1 > candidato2 and candidato1 > candidato3:
    print("Candidato 1 é o vencedor.")
elif candidato2 > candidato1 and candidato2 > candidato3:
    print("Candidato 2 é o vencedor.")
elif candidato3 > candidato1 and candidato3 > candidato2:
    print("Candidato 3 é o vencedor.")
else:
    print("Houve um empate!")
   