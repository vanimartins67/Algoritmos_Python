#exercícios de operações matemáticas com listas

#11
minimo = [1, 2, 3, 4, 5]
print(min(minimo))
#12
cinco = [1, 2, 3, 4, 5]
cinco[2] = 0
print(cinco)
#13
quatro = [1, 2, 3, 4, 5]
quatro[0] = 0
print(quatro)
#14
seis =[1, 2, 3, 4, 5, 6]
seis[5] = 0
print(seis)
#15
tres = [1, 2, 3]
tres.remove(1)
print(tres)
#16
cinco = [1, 2, 3, 4, 5]
print(cinco.pop(4))
#17
quatro = [1, 2, 3, 4]
print(quatro.pop(0))
#18
lista = ["papel", "caneta", "borracha"]
lista.append("lapis")
print(lista)
#19
lista = ["camisa", "calça", "tenis"]
lista.insert(1, "camiseta")
print(lista)
#20
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
lista1.extend(lista2)
print(lista1)
#21
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)
#22
lista = [1, 2, 3, 4, 5]
lista.sort()
print(lista)
#23
lista = [1, 2, 3, 4, 5]
lista.sort(reverse=True)
print(lista)
#24
lista = [1, 2, 3, 4, 5]
lista.index(3)
print(lista.index(3))
#25
lista = [ 1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 8, 9, 10]
lista.count(4)
print(lista.count(4))
#26
lista = [1, 2, 3, 4, 5]
del lista[2]
print(lista)
#27
lista1 = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c", "d", "e"]
lista1 = lista2.copy()
print(lista1)
#28
lista = ["BRAZIL"]
print(",".join(lista[0]))
#29
lista = [1, 2, 3, 4, 5]
lista.clear()
print(lista)
#30
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(lista))


