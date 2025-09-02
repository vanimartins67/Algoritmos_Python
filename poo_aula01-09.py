brinquedo = {
    'marca': 'Estrela',
    'modelo': 'Boneca',
    'preco':150
}


valor = brinquedo['preco']

print("Valor: ",valor)

####quando eu criar uma função que não sei
####a quantidade de parametros que irá receber usar
#### *args

def my_func(param1, *args):
    print(param1)
    for item in args:
        print(item)

    print((args))

my_func(12,14,16,18)



####multiplos argumentos

def world_cup_titles(country, *args):
    print('Country:', country)
    for title in args:
        print('year:', title)

world_cup_titles('Brazil', 1959, 1962, 1970, 1994, 2002)


def local_estudo(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
local_estudo(first = 'Senac', second = 'Hub', third = 'Academy')
             




pessoa = {}

pessoa['nome'] = "Thiago"
pessoa['cidade'] = "CGR"
print(pessoa)

def cria_dicionario(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

###chamando de função com parametros nomeados

cria_dicionario(nome="Thiago", idade=32, cidade="CGR")




def calculate_tax(value, **kwargs):
    total = 0
    print(kwargs)
    if 'iss' in kwargs:
        total += value * kwargs['iss']
    if "pis" in kwargs:
        total += value * kwargs['pis']
    

    calculate_tax(1000, iss=0.05, pis=0.033)
   
    return total




def concatena(**kwargs):
    print(f'Valores recebidos: {kwargs}')
    resultado = ''
    for valor in kwargs.values():
        resultado += f'{valor}'
    return resultado

print(concatena(a='Python', b='Academy', c='Rules'))
    