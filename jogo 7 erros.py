print("-- Resevartório de Água --") #estava sem parênteses

altura=float(input("Digite a altura (cm): "))
largura=float(input("Digite a largura (cm): ")) #int para float / tirei espaço inutil
comprimento=float(input("Digite o comprimento (cm): ")) #tirei espaço inutil
c_diário=float(input("Digite o valor do consumo médio diário(litros/dia)= "))

cap_total=((altura*largura*comprimento)/1000); #o resultado seria em cm3 por isso, dividimos por mil para passar de cm3 / multiplicação entre larg e comppara litros / mudei as aspas triplas para#
auton_reser=cap_total/c_diário #acento

print("Capacidade do Reservatório= ",cap_total, "litros ")
print("Autonomia do reservatório= ",auton_reser," dias") #Agora, vamos classificar o consumo
if(auton_reser<2):
    print("Consumo Elevado") #print indentado
elif(auton_reser>=2 and auton_reser<7): #simbolo de menor
    print("Consumo Moderado")
elif(auton_reser>7):
    print("\n Consumo Baixo") #print indentado
