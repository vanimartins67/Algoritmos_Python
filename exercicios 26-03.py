a = [1, 2, 3, 4, 5]
print(a) #mostrar
print(min(a)) #menor numero
print(max(a)) #maior numero
print(len(a)) #quantidade de numeros
print(sum(a)) #somar numeros

lista = [1, 2, 1, 5, 6, 4 ,3 ,1]
print(lista.count(1)) #contar quantas vezes o numero 1 aparece na lista

lista = ["manga", "uva", "banana", "pera", "limao"]
print(lista)
lista [1] = "laranja"
lista [1:2] = ["laranja"] #substituir uva por laranja
print(lista)


lista = [[1, 2], [3], [4, 5, 6]]
t1 = lista[0]
t2 = lista[1]
t3 = lista[2]
print(sum(t1) + sum(t2) + sum(t3)) #somar todos os numeros da lista

lista = [1, 2, 3]
x = sum(lista [0:1])
y = sum(lista [0:2])
z = sum(lista [0:3])
print([x, y, z]) #somar os numeros da lista
print([lista[0], lista[0] + lista[1], lista[0] + lista[1] + lista[2]]) #somar os numeros da lista2

lista = [1, 2, 3, 4]
del lista[0]
del lista[2]
print(lista) #deletar os numeros 1 e 3

Country = ["Alemanha", "Itália", "Japão"]
#add países america do sul
#add países america do norte
#add países america central
#add capitais dos países
Country.extend(["Brasil", "Argentina", "Uruguai", "Paraguai", "Bolívia", "Chile", "Peru", 
               "Equador", "Colômbia", "Venezuela", "Guiana", "Guiana Francesa", "Suriname"])
Country.extend(["Estados Unidos", "Canadá", "México"])
Country.extend(["Belize", "Costa Rica", "El Salvador", "Guatemala", "Honduras", 
               "Nicarágua", "Panamá", "Antígua e Barbuda", "Bahamas", "Barbados", 
               "Cuba", "Dominica", "Granada", "Haiti", "Jamaica", "República Dominicana", 
               "Santa Lúcia", "São Cristóvão e Névis", "São Vicente e Granadinas", 
               "Trinidad e Tobago"])
Country.extend(["Brasília", "Buenos Aires", "Montevidéu", "Assunção", "La Paz", 
               "Santiago", "Lima", "Quito", "Bogotá", "Caracas", "Georgetown", 
               "Caiena", "Paramaribo"])
Country.extend(["Washington DC", "Ottawa", "Cidade do México"])
Country.extend(["Belmopan", "San José", "San Salvador", "Cidade da Guatemala", 
               "Tegucigalpa", "Manágua", "Cidade do Panamá", "Saint John's", 
               "Nassau", "Bridgetown", "Havana", "Roseau", "Saint George's", 
               "Porto Príncipe", "Kingston", "Santo Domingo", "Castries", 
               "Basseterre", "Kingstown", "Porto de Espanha"])
print(Country)



















