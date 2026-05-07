import mysql.connector

# 1. Conexão
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Usar buffered=True evita erros de sincronização em scripts sequenciais
cursor = conexao.cursor(buffered=True)

# 2 e 3. Criação e Seleção do Banco
cursor.execute("CREATE DATABASE IF NOT EXISTS `Aula23-04`")
cursor.execute("USE `Aula23-04`")

# 4. Criar tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        idade INT
    )
""")

# 5. Inserir (O uso de placeholders %s está perfeito!)
sql_insert = "INSERT INTO alunos (nome, idade) VALUES (%s, %s)"
valores = ("TesmanCarlos", 24)
cursor.execute(sql_insert, valores)
conexao.commit()
id_inserido = cursor.lastrowid # Pega o ID que acabou de ser gerado
print(f"Inserção realizada. ID: {id_inserido}")

# 6. Atualizar (Melhor usar o ID para ser específico)
# Aqui alteramos apenas o aluno que acabamos de inserir
sql_update = "UPDATE alunos SET idade = %s WHERE id = %s"
cursor.execute(sql_update, (28, id_inserido))
conexao.commit()
print("Atualização realizada com foco no ID.")

# 7. Mostrar todos
cursor.execute("SELECT * FROM alunos")
resultados = cursor.fetchall()
print("\nDados na tabela alunos:")
for linha in resultados:
    print(linha)

# 8. Fechar tudo
cursor.close()
conexao.close()