class People:  ##superclass herança
    def __init__(self, nome, email, senha):
        self.name = nome
        self.mail = email
        self.password = senha

    def hello(self):
        print(f" Hellooooo {self.name} ")


class Student(People):
    def __init__(self, nome, email, senha, ra):
        super().__init__(nome, email, senha)
        self.ra = ra 


p1 = People("LUIS", "lulu@gmail.com", "123456")
p1.hello()
s1 = Student("TESMAN", "tesmas@gmail.com", "123", "55555")
s1.hello()