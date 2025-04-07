#exercícios trabalhando com strings e listas

#61
palavras = ["gato", "cachorro", "ramster"]
frase = " ".join(palavras)
print(frase) 
#62
palavras = ["eu", "amo", "voce"]
maiusculas = [palavras[0].upper(), palavras[1].upper(), palavras[2].upper()]
print(maiusculas) 
#63
palavras = ["EU", "ODEIO", "VOCE"]
minusculas = [palavras[0].lower(), palavras[1].lower(), palavras[2].lower()]
print(minusculas)
#64
palavras = ["cavalo", "boi", "vaca"]
capitalizadas = [palavras[0].capitalize(), palavras[1].capitalize(), palavras[2].capitalize()]
print(capitalizadas)
#65
palavras = ["bem-vindo", "ao Brasil"]
titulos = [palavras[0].title(), palavras[1].title()]
print(titulos)
#66
palavras = ["banana", "maçã", "pera"]
substituidas = [palavras[0].replace("a", "o"), palavras[1].replace("a", "o"), palavras[2].replace("a", "o")]
print(substituidas) 
#67
frases = ["Eu amo cinema", "Ler é legal"]
lista1 = frases[0].split()
lista2 = frases[1].split()
listas_palavras = [lista1, lista2]
print(listas_palavras)
#68
palavras = ["banana", "abacaxi", "laranja"]
palavras.sort()
print(palavras)
#69
palavras = ["a", "b", "c"]
palavras.sort(reverse=True)
print(palavras)
#70
palavras = ["gato", "cachorro", "ramster", "oi"]
mais_curta = min(palavras, key=len)
print(mais_curta)
#71
palavras = ["gato", "cachorro", "ramster", "oi"]
mais_longa = max(palavras, key=len)
print(mais_longa)
#72
frases = ["Eu sou legal", "O dia está bonito"]
primeira1 = frases[0].split()[0]
primeira2 = frases[1].split()[0]
primeiras = [primeira1, primeira2]
print(primeiras)
#73
palavras = ["casa", "sol", "mato", "mar"]
filtradas = []
if len(palavras[0]) >= 4: filtradas.append(palavras[0])
if len(palavras[1]) >= 4: filtradas.append(palavras[1])
if len(palavras[2]) >= 4: filtradas.append(palavras[2])
if len(palavras[3]) >= 4: filtradas.append(palavras[3])
print(filtradas) 
#74
palavras = ["computador", "livro", "caneta", "caderno"]
filtradas = []
if len(palavras[0]) <= 6: filtradas.append(palavras[0])
if len(palavras[1]) <= 6: filtradas.append(palavras[1])
if len(palavras[2]) <= 6: filtradas.append(palavras[2])
if len(palavras[3]) <= 6: filtradas.append(palavras[3])
print(filtradas)
#75
lista = [1, 2, 3, 4, 5, 6]
metade = len(lista) // 2
lista1 = lista[:metade]
lista2 = lista[metade:]
print(lista1, lista2)
#76
lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 7, 8]
combinada = lista1 + lista2
print(combinada) 
#77
lista = [1, 2, 3, 4, 5]
rotacionada = [lista[1], lista[2], lista[3], lista[4], lista[0]]
print(rotacionada)
#78
lista = [1, 2, 3, 4, 5]
rotacionada = [lista[4], lista[0], lista[1], lista[2], lista[3]]
print(rotacionada)
#79
lista = ["  filme  ", "serie ", "  curta"]
sem_espacos = [lista[0].strip(), lista[1].strip(), lista[2].strip()]
print(sem_espacos)
#80
numeros = [1, 2, 3, 4]
strings = [str(numeros[0]), str(numeros[1]), str(numeros[2]), str(numeros[3])]
print(strings)