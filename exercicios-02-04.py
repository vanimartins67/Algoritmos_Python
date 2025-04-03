listas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(listas[1:10]) #inervalo 1 a 9
print(listas[8:11]) #intervalo 8 a 10
print(listas[2:10:2]) #salto para par (o ultimo numero é qtos elementos salta)
print(listas[1:10:2]) #salto para impar (o ultimo numero é qtos elementos salta)
listas.reverse() #lista reversa
print(listas)
listas.sort(reverse = True) #lista reversa 2
print(listas)


P1 = [7.0, 8.3, 10.0, 6.5, 9.3]
P2 = [8.5, 6.9, 5.0, 7.5, 9.8]
print(sum(P1)/5) #calculo media com 5 elementos como na lista dada
print(sum(P2)/5)
media1 = (sum(P1)/len(P1)) #calculo media com quantos elementos tiver na lista
media2 = (sum(P2)/len(P2))
print(media1)
print(media2)
print(f"{media2:.2f}") #limitando casas decimais













