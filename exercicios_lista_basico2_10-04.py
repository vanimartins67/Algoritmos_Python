#exercícios de operações matemáticas com listas

#1
minimo = [1, 2, 3, 4, 5]
print(min(minimo))
#2
cinco = [1, 2, 3, 4, 5]
cinco[2] = 0
print(cinco)
#3
quatro = [1, 2, 3, 4, 5]
quatro[0] = 0
print(quatro)
#4
seis =[1, 2, 3, 4, 5, 6]
seis[5] = 0
print(seis)
#5
tres = [1, 2, 3]
tres.remove(1)
print(tres)
#6
cinco = [1, 2, 3, 4, 5]
print(cinco.pop(4))
#7
quatro = [1, 2, 3, 4]
print(quatro.pop(0))
#8
lista = ["papel", "caneta", "borracha"]
lista.append("lapis")
print(lista)
#9
lista = ["camisa", "calça", "tenis"]
lista.insert(1, "camiseta")
print(lista)
#10
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
lista1.extend(lista2)
print(lista1)
#11
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)
#12
lista = [1, 2, 3, 4, 5]
lista.sort()
print(lista)
#13
lista = [1, 2, 3, 4, 5]
lista.sort(reverse=True)
print(lista)
#14
lista = [1, 2, 3, 4, 5]
lista.index(3)
print(lista.index(3))
#15
lista = [ 1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 8, 9, 10]
lista.count(4)
print(lista.count(4))
#16
lista = [1, 2, 3, 4, 5]
del lista[2]
print(lista)
#17
lista1 = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c", "d", "e"]
lista1 = lista2.copy()
print(lista1)
#18
lista = ["BRAZIL"]
print(",".join(lista[0]))
#19
lista = [1, 2, 3, 4, 5]
lista.clear()
print(lista)
#20
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(lista))


