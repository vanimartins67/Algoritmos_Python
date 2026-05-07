import mysql.connector


def conectar():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "aula_connect"
    )
 
    return conexao


