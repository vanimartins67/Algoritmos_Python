from flask import Flask, request, jsonify
from db import conectar # Importa a função do seu outro arquivo

app = Flask(__name__)

# --- ROTA GET: Listar todos os alunos ---
@app.route('/alunos', methods=['GET'])
def get_alunos():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True) # Retorna os dados como dicionário (JSON)
    
    try:
        cursor.execute("SELECT * FROM alunos")
        lista_alunos = cursor.fetchall()
        return jsonify(lista_alunos), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        cursor.close()
        conexao.close()

# --- ROTA POST: Adicionar um novo aluno ---
@app.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.get_json()
    nome = dados.get('nome')
    curso = dados.get('curso')

    if not nome or not curso:
        return jsonify({"erro": "Campos 'nome' e 'curso' são obrigatórios"}), 400

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "INSERT INTO alunos (nome, curso) VALUES (%s, %s)"
        cursor.execute(sql, (nome, curso))
        conexao.commit() # Salva no banco
        return jsonify({"mensagem": "Aluno cadastrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        cursor.close()
        conexao.close()

# --- ROTA DELETE: Remover um aluno pelo ID ---
@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deletar_aluno(id_aluno):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "DELETE FROM alunos WHERE id = %s"
        cursor.execute(sql, (id_aluno,))
        conexao.commit()

        if cursor.rowcount == 0:
            return jsonify({"erro": "Aluno não encontrado"}), 404

        return jsonify({"mensagem": f"Aluno {id_aluno} removido!"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        cursor.close()
        conexao.close()

if __name__ == '__main__':
    app.run(debug=True)