""" 
1. Defnir o objetivo da API:

    Iremos montar uma api de músicas, onde deverá ser possível, consultar todas canções disponíveis, consultar uma canção individual, adicionar uma canção nova, editar canções existentes e também excluir músicas existentes.

2. Qual será o URL base da API? 

    Iremos utilizar o url base 'localhost'

3. Quais são os endpoints?

    Disponibilize endpoints para consultar, editar, criar e excluir

4. Quais recursos serão disponibilizados pela API?
    Informações sobre canções

5. Quais verbos http serão disponibilizados?

    * GET

    * POST

    * PUT

    * DELETE 

6. Quais são os URLs completos para cada um?

    * GET http://localhost:5000/cancoes

    * GET http://localhost:5000/cancoes/1

    * POST http://localhost:5000/cancoes

    * PUT http://localhost:5000/cancoes/1

    * DELETE http://localhost:5000/cancoes/1

7. Qual deve ser a estrutura de cada canção.

    - lista de dicionários, que contem cancao e estilo 
 """

from flask import Flask, jsonify, request

app = Flask(__name__);

# URL BASE - Rota padrão

cancoes = [
    {
        'musica': 'Nova era',
        'autor': 'Chefin'
    },
    {
        'musica': 'Voando alto',
        'autor': 'Poze do rodo'
    },
    {
        'musica': 'Chefe do crime perfeito',
        'autor': 'Felipe Ret'
    },
]

# Consultando - GET http://localhost:8888

@app.route('/cancoes')
def obter_cancoes():
    return jsonify(cancoes)

# Consultando por ID - GET http://localhost:8888/cancoes/1
@app.route('/cancoes/<int:indice>', methods=['GET'])
def obter_cancoes_por_id(indice):
    return jsonify(cancoes[indice], 200);

# Adicionando uma canção nova - POST http://localhost:8888/cancoes
@app.route('/cancoes', methods=['POST'])
def adicionar_cancoes():
    nova_cancoes = request.get_json();
    cancoes.append(nova_cancoes);
    return jsonify(nova_cancoes, 200);

# Editando uma canção - PUT http://localhost:8888/cancoes/1
@app.route('/cancoes/<int:indice>', methods=['PUT'])
def alterar_cancoes(indice):
    cancoes_alterada = request.get_json();
    cancoes[indice].update(cancoes_alterada);

    return jsonify(cancoes[indice], 200)

# Deletando uma canção - DELETE http://localhost:8888/cancoes/1
@app.route('/cancoes/<int:indice>', methods=['DELETE'])
def deletar_cancoes(indice):
    try:
        del cancoes[indice]
        return jsonify(f'Foi excluído a canção {cancoes[indice]}');
    except:
        return jsonify('Canção não encontrada para exclusão.', 404);


app.run(port=8888, host='localhost', debug=True);