import mysql.connector

class Database:
    def __init__(self, banco = "perkal") -> None: 
        self.banco = banco
        self.host = 'localhost'
        self.user = 'root'

    def connect(self):
        self.conn = mysql.connector.connect(host=self.host,database=self.banco,user=self.user,password='')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("CONECTADO COM SUCESSO: ",db_info)
        else:
            print("ERROOO")

    def insert(self,tupla):
        self.connect()
        try:
            self.cursor.execute('INSERT INTO cliente (nome,cpf,fone,cidade) VALUES (%s,%s,%s,%s)',tupla)
            self.conn.commit()
            return True
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select(self):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cliente")
            result = self.cursor.fetchall()
            return result
        
        except Exception as err:
            print(err)
        
        finally:
            self.close_connection()

    def select_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f'SELECT * FROM cliente WHERE id_cli = {id} ')
            result = self.cursor.fetchone()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()



    def update(self,tupla):
        self.connect()
        try: ###### TENTE, TENTAR
            self.cursor.execute(f""" 
                UPDATE cliente SET nome = '{tupla[1]}', 
                cpf = '{tupla[2]}',
                fone = '{tupla[3]}',
                cidade = '{tupla[4]}'                
                WHERE id_cli = {tupla[0]}
            """)
            self.conn.commit()
            return True

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def delete(self,id_cli):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cliente WHERE id_cli = {id_cli} ")
            self.conn.commit()
            return True
        
        except Exception as err:
            print(err)
        
        finally:
            self.close_connection()

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexao encerrada com sucesso!!!!")

if __name__ == "__main__":
    db = Database()
    db.connect()
    print("SENDO EXECUTADO PELA MAIN")