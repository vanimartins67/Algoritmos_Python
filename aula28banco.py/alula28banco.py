import mysql.connector
from db import conectar
from flask import Flask, request, jsonify

app = Flask (__name__)


@app.route("/alunos", methods = ["GET"])
def get_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("select * from alunos")
    dados = cursor.fetchall()

    aluno = []
    for alunos in dados:
        aluno.append({
            "id": alunos[0],
            "nome": alunos[1],
            "idade": alunos[2]
        })
        #print(f"ID: {alunos[0]} | Nome: {alunos[1]} | Idade: {alunos[2]}")

    cursor.close()
    conexao.close()

    return jsonify(aluno)

def post_aluno():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("insert into alunos (nome, idade) values (%s, %s)", (input("Digite o nome do aluno: "), input ("Digite a idade do aluno: ")))
    conexao.commit()

    print("Aluno adicionado com sucesso!")

    cursor.close()
    conexao.close()

def put_aluno():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("update alunos set nome = %s, idade = %s where id = %s", (input("Digite o nome do aluno: "), input ("Digite a idade do aluno: "), int(input("Digite o ID: "))))
    conexao.commit()

    print("Aluno atualizado!")

    cursor.close()
    conexao.close()

def delete_aluno():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("delete from alunos where id = %s", (int(input("Digite o ID do aluno: "))))
    conexao.commit()

    print("Aluno deletado!")

    cursor.close()
    conexao.close()


if __name__ == "__main__":
    app.run(debug = True)