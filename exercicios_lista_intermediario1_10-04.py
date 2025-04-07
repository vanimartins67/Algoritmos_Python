#exercícios de operações matemáticas com listas

#41
lista = [1, 2, 3]
nova_lista = [lista[0]*2, lista[1]*2, lista[2]*2]
print(nova_lista)
#42
lista = [1, 2, 3]
nova_lista = [lista[0]+10, lista[1]+10, lista[2]+10]
print(nova_lista)
#43
lista = [1, 2, 3, 4, 5]
quadrados = [lista[0]**2, lista[1]**2, lista[2]**2, lista[3]**2, lista[4]**2]
print(quadrados)
#44
lista = [2, 3, 4]
resultado = lista[0] * lista[1] * lista[2]
print(resultado)
#45
lista = [10, 20, 30]
media = sum(lista) / len(lista)
print(media)
#46
lista = [5, 2, 8, 1]
copia = lista.copy()
copia.remove(max(copia))
segundo_maior = max(copia)
print(segundo_maior)
#47
lista = [5, 2, 8, 1]
copia = lista.copy()
copia.remove(min(copia))
segundo_menor = min(copia)
print(segundo_menor) 
#48
lista = [3, 1, 4, 2]
ordenada = sorted(lista)
print(ordenada)  
print(lista)     
#49
lista = [3, 1, 4, 2]
ordenada = sorted(lista, reverse=True)
print(ordenada)  
#50
lista = [1, 2, 3, 4]
invertida = lista[::-1]
print(invertida)  
#51
lista = [10, 20, 30, 40, 50]
tres_primeiros = lista[:3]
print(tres_primeiros) 
lista = [10, 20, 30, 40, 50]
tres_ultimos = lista[-3:]
print(tres_ultimos)  
#53
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pedaco = lista[2:6]
print(pedaco) 
#54
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista[:5] = [0] * 5
print(lista) 
#55
lista = [-1, 2, -3, 4]
absolutos = []
absolutos.append(abs(lista[0]))  
absolutos.append(abs(lista[1]))  
absolutos.append(abs(lista[2]))  
absolutos.append(abs(lista[3]))  
print(absolutos)  
#56
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista[:3]
print(lista)  
#57
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista[-3:]
print(lista)
#58
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2
print(concatenada)  
#59
lista = [1, 2, 2, 3, 4, 4, 5]
sem_duplicatas = list(set(lista))
print(sem_duplicatas) 
#60
lista = [1, 2, 2, 3, 2, 4]
contagem = lista.count(2)
print(contagem)