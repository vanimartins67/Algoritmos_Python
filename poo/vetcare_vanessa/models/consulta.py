from models.conexao import criar_conexao

class Consulta:
    def __init__(self, animal_id=0, vet_id=0, data='', hora=''):
        self.animal_id = animal_id
        self.vet_id = vet_id
        self.data = data
        self.hora = hora

    def salvar(self):
        con = criar_conexao()
        cursor = con.cursor()
        sql = "INSERT INTO consulta (animal_id, vet_id, data_consulta, hora_consulta) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (self.animal_id, self.vet_id, self.data, self.hora))
        con.commit()
        con.close()

    def listar(self):
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT c.id, c.data_consulta, c.hora_consulta FROM consulta c"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado