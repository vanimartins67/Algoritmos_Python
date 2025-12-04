from models.conexao import criar_conexao

class Animal:
    def __init__(self, nome='', especie='', raca='', idade=0, tutor_id=0):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.tutor_id = tutor_id

    def salvar(self):
        con = criar_conexao()
        cursor = con.cursor()
        sql = "INSERT INTO animal (nome, especie, raca, idade, tutor_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (self.nome, self.especie, self.raca, self.idade, self.tutor_id))
        con.commit()
        con.close()

    def listar(self):
        con = criar_conexao()
        cursor = con.cursor()
        # Traz o nome do dono junto (JOIN)
        sql = "SELECT a.id, a.nome, a.especie, p.nome FROM animal a JOIN person p ON a.tutor_id = p.id"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado