#exercícios de manipulação de listas

#21
minimo = [1, 2, 3, 4, 5]
print(min(minimo))
#22
cinco = [1, 2, 3, 4, 5]
cinco[2] = 0
print(cinco)
#23
quatro = [1, 2, 3, 4, 5]
quatro[0] = 0
print(quatro)
#24
seis =[1, 2, 3, 4, 5, 6]
seis[5] = 0
print(seis)
#25
tres = [1, 2, 3]
tres.remove(1)
print(tres)
#26
cinco = [1, 2, 3, 4, 5]
print(cinco.pop(4))
#27
quatro = [1, 2, 3, 4]
print(quatro.pop(0))
#28
lista = ["papel", "caneta", "borracha"]
lista.append("lapis")
print(lista)
#29
lista = ["camisa", "calça", "tenis"]
lista.insert(1, "camiseta")
print(lista)
#30
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
lista1.extend(lista2)
print(lista1)
#31
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)
#32
lista = [1, 2, 3, 4, 5]
lista.sort()
print(lista)
#33
lista = [1, 2, 3, 4, 5]
lista.sort(reverse=True)
print(lista)
#34
lista = [1, 2, 3, 4, 5]
lista.index(3)
print(lista.index(3))
#35
lista = [ 1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 8, 9, 10]
lista.count(4)
print(lista.count(4))
#36
lista = [1, 2, 3, 4, 5]
del lista[2]
print(lista)
#37
lista1 = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c", "d", "e"]
lista1 = lista2.copy()
print(lista1)
#38
lista = ["BRAZIL"]
print(",".join(lista[0]))
#39
lista = [1, 2, 3, 4, 5]
lista.clear()
print(lista)
#40
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(lista))


