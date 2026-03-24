import mysql.connector

# conexão
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_usuario"
    )

# CREATE
def create_user(nome, email, endereco):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = "INSERT INTO usuario (nome, email, endereco) VALUES (%s, %s, %s)"
        valores = (nome, email, endereco)

        cursor.execute(sql, valores)
        conn.commit()

        print("Usuário criado com sucesso!")

    except Exception as e:
        print("Erro ao criar:", e)

    finally:
        cursor.close()
        conn.close()


# READ
def read_users():
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = "SELECT * FROM usuario"
        cursor.execute(sql)

        resultados = cursor.fetchall()

        for user in resultados:
            print(user)

    except Exception as e:
        print("Erro ao ler:", e)

    finally:
        cursor.close()
        conn.close()


# UPDATE
def update_user(id, nome, email):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = "UPDATE usuario SET nome=%s, email=%s WHERE id=%s"
        valores = (nome, email, id)

        cursor.execute(sql, valores)
        conn.commit()

        print("Usuário atualizado!")

    except Exception as e:
        print("Erro ao atualizar:", e)

    finally:
        cursor.close()
        conn.close()


# DELETE
def delete_user(id):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = "DELETE FROM usuario WHERE id=%s"
        cursor.execute(sql, (id,))
        conn.commit()

        print("Usuário deletado!")

    except Exception as e:
        print("Erro ao deletar:", e)

    finally:
        cursor.close()
        conn.close()


#teste

create_user("Vanessa Martins", "vanessa@email.com", "Campo Grande")

read_users()

update_user(1, "Vanessa M.", "vanessa2@email.com")

delete_user(1)