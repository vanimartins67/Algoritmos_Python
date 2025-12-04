from models.conexao import criar_conexao
from models.pessoa import Pessoa

class Tutor(Pessoa):
    def __init__(self, nome='', telefone='', endereco=''):
        super().__init__(nome, telefone)
        self.endereco = endereco

    def salvar(self):
        con = criar_conexao()
        cursor = con.cursor()
        
        # 1. Salvar em Person (tabela pai)
        sql_pessoa = "INSERT INTO person (nome, telefone) VALUES (%s, %s)"
        cursor.execute(sql_pessoa, (self.nome, self.telefone))
        self.id = cursor.lastrowid
        
        # 2. Salvar em Tutor (tabela filha) usando o mesmo ID
        sql_tutor = "INSERT INTO tutor (id, endereco) VALUES (%s, %s)"
        cursor.execute(sql_tutor, (self.id, self.endereco))
        
        con.commit()
        con.close()

    def listar(self):
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT p.id, p.nome, p.telefone, t.endereco FROM person p JOIN tutor t ON p.id = t.id"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado