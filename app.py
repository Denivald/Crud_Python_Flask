from flask import Flask , request, jsonify  # Importa a classe Flask do módulo 
import mysql.connector  #connectando biblioteca mysql conector, para conectar o código ao meu banco de dados.

app=Flask(__name__)  # Cria uma instância da aplicação Flask

# conexação com o meu banco de dados.
def conectar_bd():
 return mysql.connector.connect(
    host="localhost", # Local da execução do meu banco dados.
    port=3306,
    user="root", # meu usuário do MySQL.
    password="aprendiz", # minha senha de usuário
    database="escola",
 )

# Rota para cadastrar aluno.
@app.route("/alunos",methods=["POST"]) # Estabelecendo o methodo post.
def cadastrar_aluno(): 
    dados = request.get_json() 
    nome = dados.get("nome")
    email = dados.get("email")
    matricula = dados.get("matricula")
    senha = dados.get("senha")
    
    if not nome or not email or not matricula or not senha:
        return jsonify({"erro": "Todos os campos são obrigatórios."}), 400

    conexao = conectar_bd() # Conectando ao banco de dados.
    cursor = conexao.cursor() # executando comandos sql e interagindo com  os resultados.
    sql = "INSERT INTO aluno (nome, email, matricula, senha) VALUES (%s, %s, %s, %s)"  #Definição de Strings de consulta sql, com os  valores a ser inseridos em cada coluna.
    valores = (nome, email, matricula,senha) 
    
    cursor.execute(sql,valores) # Enviando valores para o banco de dados.
    conexao.commit() # Salvando alterações no banco de dados.
    cursor.close() # Fecha{"Aluno cadartrado com sucesso"}, 
    conexao.close()  # fechando conexão com o banco de dados.

    return jsonify({"mensagem":"Aluno cadastrado com sucesso!"}), 201

# Rota para listar  todos os alunos.
@app.route("/alunos",methods=["GET"]) 
def listar_alunos(): # Listando alunos.
    conexao =conectar_bd()  # conectando ao banco de dados.
    cursor = conexao.cursor(dictionary=True) # Retornando o resultado como dicionários python em vez de tuplas.
    cursor.execute("select * From aluno") # executando consulta no banco de dados.
    alunos = cursor.fetchall()
    cursor.close() # Fechando o cursor,que é ponte entre o código e obanco de dados.
    conexao.close() # fechando conexão com o banco de dados.
    return jsonify(alunos)  # Retorna  lista de alunos em formato json.

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente 

 app.run(debug=True)  # Inicia o servidor Flask com modo debug ativado Por fim, execute a aplic
