import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def imprimir_raio(self):
        print(f"Raio do círculo: {self.raio}")
        return self.raio
    
    def calcular_area(self):
        area = math.pi * (self.raio ** 2)
        print(f"Área do círculo: {area:.2f}")
        return area
    
    def calcular_circunferencia(self):
        circunferencia = 2 * math.pi * self.raio
        print(f"Circunferência do círculo: {circunferencia:.2f}")
        return circunferencia

circulo1 = Circulo(5)
circulo1.imprimir_raio()
circulo1.calcular_area()
circulo1.calcular_circunferencia()
print()