# try:
#  a = int(input("digite uma palavra"))
# except:
#  print("Digite apenas números")
 
try:
    a = int(input("digite uma palavra= "))
except ValueError:
    print("Digite apenas números")
except:
    print("Erro Desconhecido")
finally:
    print("Final do algoritmo")
