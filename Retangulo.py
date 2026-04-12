class Retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
 
    def calcula_area(self) -> float:
        return self.base*self.altura
   
r1 = Retangulo(12,24)
print(r1.base)
print(r1.altura)
r2 = Retangulo(8,12)
print(r2.base)
print(r2.altura)
 
x= r1.calcula_area()
print(x)
 
y = r2.calcula_area()
print(y)
 