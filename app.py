from flask import Flask, jsonify, request

app = Flask (__name__)

livros = [

]

#Consultar livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_id(id):
    for livro in livros:
       if livro.get('id') == id:
           return jsonify(livro)
#Editar por ID
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
#Criar Livro
@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

#Excluir Livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


#Servidor
app.run(port=5000, host='localhost', debug=True)