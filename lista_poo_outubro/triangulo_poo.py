class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    def calcular_perimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        print(f"Perímetro do triângulo: {perimetro}")
        return perimetro
    
    def get_maior_lado(self):
        maior = max(self.ladoA, self.ladoB, self.ladoC)
        print(f"Maior lado: {maior}")
        return maior

print("\n" + "="*50)
print("7 - CLASSE TRIANGULO")
print("="*50)
triangulo1 = Triangulo(3, 4, 5)
triangulo1.calcular_perimetro()
triangulo1.get_maior_lado()