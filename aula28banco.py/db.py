import mysql.connector #pip install mysql-connector-python

#criar uma conexao
def conectar():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "aula_connect" 
    )
    return conexao


