class Dog:
    def __init__(self, nome, peso, cor):
        self.nome = nome
        self.peso = peso
        self.cor = cor

    def latir(self):
        print(f'{self.nome} AU AU AU')

    def comer(self):
        print(f'{self.nome} comendo... ')

dog1 = Dog("Toto", 5, "Caramelo")
dog2 = Dog("Charlene", 7, "Branca")
dog1.latir()
dog1.comer()