from models.conexao import criar_conexao

class Prescricao:
    def __init__(self, consulta_id=0, texto=''):
        self.consulta_id = consulta_id
        self.texto = texto

    def salvar(self):
        con = criar_conexao()
        cursor = con.cursor()
        sql = "INSERT INTO prescricao (consulta_id, texto) VALUES (%s, %s)"
        cursor.execute(sql, (self.consulta_id, self.texto))
        con.commit()
        con.close()

    def listar(self):
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT id, consulta_id, texto FROM prescricao"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado