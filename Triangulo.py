class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def calcular_area(self) -> float:
        area = (self.base  * self.altura) / 2


t1 = Triangulo(9,15)
t2 = Triangulo(4.5,6)

print("BASE DO T2: ", t2.base)
print( t2.calcular_area())
print("BASE DO T1: ", t1.base)
print( type(t1.calcular_area()) )