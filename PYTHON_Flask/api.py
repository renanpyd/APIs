# Uma API é um lugar para disponibilizar recursos e/ou funcionalidades.
# 1. Objetivo - Criar uma api que disponibiliza consulta, criação, edição e exclusão de livros. 
# 2. URL base - localhost
# 3. Endpoints - localhost/livros (get)
#                localhost/livros (post)
#                localhost/livros/id (get)
#                localhost/livros/id (put)
#                localhost/livros/id (delete)
# 4. Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'livro teste um',
        'autor': 'autor teste um'
    },
    {
        'id': 2,
        'titulo': 'livro teste dois',
        'autor': 'autor teste dois'
    },
    {
        'id': 3,
        'titulo': 'livro teste três',
        'autor': 'autor teste três'
    }
]

# Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def consultar_livros_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
# Editar
@app.route('/livros/<int:id>', methods=['PUT'])        
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get(id) == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>', methods=[DELETE])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)        

app.run(port=5000,host='localhost',debug=True)
