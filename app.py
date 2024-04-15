from flask import Flask, jsonify
from random_data import pessoas 
import funcoes
app = Flask(__name__)

@app.route("/" , methods = ["GET"])
def index ():
    return jsonify({"Status": 200, "mensagem":"API kauan"})


# Route A
@app.route('/maiores_de_50', methods = ["GET"])
def todos_maiores_de_50():
    maiores_de_50 = funcoes.maior_de_50(pessoas)
    return jsonify({"Status": 200, "mensagem":maiores_de_50})


# Route B
@app.route('/salario_acima_2000',methods = ["GET"])
def todos_salarios_acima_2000():
    salario_acima_2000 = funcoes.mais_2000(pessoas)
    return jsonify({"Status": 200, "mensagem":salario_acima_2000})

# Route C
@app.route('/maiores_salarios',methods = ["GET"])
def maiores_salarios_todos():
    maiores_salarios = funcoes.maior_salario(pessoas)
    return jsonify({"Status": 200, "mensagem":maiores_salarios})

# Route D
@app.route('/media_salarial_profissao',methods = ["GET"])
def media_de_salario_profissao():
    media_salarial_profissao = funcoes.media_profissoes(pessoas)
    return jsonify({"Status": 200, "mensagem":media_salarial_profissao})
# Route E

@app.route('/maioria_idade_sexo_acima_2000',methods = ["GET"])
def homem_e_mulher_maior_2000():
    maioria_idade_sexo_acima_2000 = funcoes.maior_2000_sexo(pessoas)
    return jsonify({"Status": 200, "mensagem":maioria_idade_sexo_acima_2000})
# Route Sair
@app.route('/sair')
def sair():
    return jsonify('sair.html')