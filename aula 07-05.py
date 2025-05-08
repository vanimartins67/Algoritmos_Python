frutas = ["banana", "maçã", "laranja", "uva"]
for i in frutas:
    print(i)

nomes = ["Pedro", "João", "Letícia"]
for n in nomes:
    print(n)
    if n == "João":
        break

nomes = ["Pedro", "João", "Letícia"]
for n in nomes:
    print(n)
    if n == "João":
        continue
    print(n)

for x in range(6):
    print(x)

for x in range(2,6):
    print(x)

for x in range(2,10,2):
    print(x)

for i in range(100, 0, -1):
    print(i)

for i in range(5):
    for j in range(6):
        print(i, j)

print("TABUADA")
for x in range(1, 11):
    print("------------")
    for y in range(1,11):
        print(x, "x", y, "=", x*y)

