from models.conexao import criar_conexao
from models.pessoa import Pessoa

class Veterinario(Pessoa):
    def __init__(self, nome='', telefone='', crmv=''):
        super().__init__(nome, telefone)
        self.crmv = crmv

    def salvar(self):
        con = criar_conexao()
        cursor = con.cursor()
        
        # 1. Salvar em Person
        sql_pessoa = "INSERT INTO person (nome, telefone) VALUES (%s, %s)"
        cursor.execute(sql_pessoa, (self.nome, self.telefone))
        self.id = cursor.lastrowid
        
        # 2. Salvar em Veterinario
        sql_vet = "INSERT INTO veterinario (id, crmv) VALUES (%s, %s)"
        cursor.execute(sql_vet, (self.id, self.crmv))
        
        con.commit()
        con.close()

    def listar(self):
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT p.id, p.nome, v.crmv FROM person p JOIN veterinario v ON p.id = v.id"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado