#listas mutáveis

#alterar elementos
frutas = ["banana", "maça","cereja"]

frutas[0] = "pera"
frutas[-1] = "laranja"
print(frutas)

uma_lista = ["a", "b", "c", "d", "e", "f"]
uma_lista[1:3] = ["x", "y"]
print(uma_lista)

#remover elementos
uma_lista = ["a", "b", "c", "d", "e", "f"]
print(uma_lista)
print(len(uma_lista))
uma_lista[1:3] = []
print(uma_lista)
print(len(uma_lista))

#inserir elementos
uma_lista = ["a", "d", "f"]
uma_lista[1:1] = ["b", "c"]
print(uma_lista)
uma_lista[4:4] = ["e"]
print(uma_lista)

#remover eficiente (del)
a = ["um", "dois", "três"]
del a[1]
print(a)

lista = ["a", "b","c", "d","e","f"]
del lista[1:5]
print(lista)

#colocar dado
a = [81, 82, 83]
a.append(5)
print(a)

#ordenar dado
a = [88, 81, 82, 83]
a.sort()
print(a)

a = [88, 81, 82, 83]
lista.sort(reverse=True)
print(a)

#retorna posicao do dado
a = [1, 2, 3, 4 ,5, 6, 7, 8, 9]
print(a.index(4))

#insere valor a posição
a = [88,81, 82, 83]
a.insert(1, 100)
print(a)

#conta quantas vezes aparece
a = [88, 81, 82, 83, 88, 85, 88, 86]
print(a)
print(a.count(88))

#exclui com maior parametro
a = [88, 81, 82, 83, 88, 85, 88, 86]
a.pop()
print(a)

a.pop(0)
print(a)

#acrescenta mais de um elemento ao final
listas = [1, 2]
listas.extend([3, 4])
print(listas)



