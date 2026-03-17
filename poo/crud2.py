import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='db_usuario',
            user='root',
            password='' 
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# 1. CREATE: Função para criar usuário
def create_user(nome, email, endereco=""):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            # O comando SQL usa %s para evitar ataques de SQL Injection
            sql = "INSERT INTO usuarios (nome, email, endereco) VALUES (%s, %s, %s)"
            valores = (nome, email, endereco)
            cursor.execute(sql, valores)
            conexao.commit() # Confirma a alteração no banco
            print(f"Sucesso: Usuário '{nome}' inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conexao.close()

# 2. READ: Função para ler usuários
def read_users():
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "SELECT * FROM usuarios"
            cursor.execute(sql)
            resultados = cursor.fetchall() # Busca todos os registros
            
            print("\n--- Lista de Usuários ---")
            for linha in resultados:
                print(f"ID: {linha[0]} | Nome: {linha[1]} | E-mail: {linha[2]} | Endereço: {linha[3]}")
            print("-------------------------\n")
        except Error as e:
            print(f"Erro ao buscar usuários: {e}")
        finally:
            cursor.close()
            conexao.close()

# 3. UPDATE: Função para atualizar usuário
def update_user(user_id, new_name, new_email):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "UPDATE usuarios SET nome = %s, email = %s WHERE id = %s"
            valores = (new_name, new_email, user_id)
            cursor.execute(sql, valores)
            conexao.commit()
            
            # Verifica se algum registro foi realmente alterado
            if cursor.rowcount > 0:
                print(f"Sucesso: Usuário ID {user_id} atualizado!")
            else:
                print(f"Aviso: Nenhum usuário encontrado com o ID {user_id}.")
        except Error as e:
            print(f"Erro ao atualizar usuário: {e}")
        finally:
            cursor.close()
            conexao.close()

# 4. DELETE: Função para deletar usuário
def delete_user(user_id):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "DELETE FROM usuarios WHERE id = %s"
            valores = (user_id,)
            cursor.execute(sql, valores)
            conexao.commit()
            
            if cursor.rowcount > 0:
                print(f"Sucesso: Usuário ID {user_id} deletado!")
            else:
                print(f"Aviso: Nenhum usuário encontrado com o ID {user_id}.")
        except Error as e:
            print(f"Erro ao deletar usuário: {e}")
        finally:
            cursor.close()
            conexao.close()

# ==========================================
# ÁREA DE TESTES (Passo 3)
# ==========================================
if __name__ == "__main__":
    # Testando o CREATE
    create_user("Ana Silva", "ana@email.com", "Rua A, 123")
    create_user("Carlos Dias", "carlos@email.com", "Av B, 456")
    
    # Testando o READ
    read_users()
    
    # Testando o UPDATE (Supondo que a Ana seja o ID 1)
    update_user(1, "Ana Silva Santos", "anasantos@email.com")
    
    # Lendo novamente para ver a atualização
    read_users()
    
    # Testando o DELETE (Supondo que o Carlos seja o ID 2)
    delete_user(2)
    
    # Lendo no final para confirmar a exclusão
    read_users()