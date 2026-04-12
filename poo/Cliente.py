from Database import Database

class Cliente:
    def __init__(self,nome=None,cpf=None,fone=None,cidade=None):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.cidade = cidade

    def cadastrar(self): #### NA CLASSE OS MÉTODOS ESCRITO EM PORTUGUES
        self.db = Database()
        tupla = (self.nome,self.cpf,self.fone,self.cidade)
        result = self.db.insert(tupla)        
        return result
    
    def buscar(self):
        self.db = Database()
        dados = self.db.select()
        return dados
    
    def buscar_por_id(self,id):
        self.db = Database()
        cliente = self.db.select_by_id(id)
        return cliente
    
    def atualizar(self,tupla):
        self.db = Database()
        cliente = self.db.update(tupla)
        return cliente
    
    
    def excluir(self,id):
        self.db = Database()
        result = self.db.delete(id)
        return result