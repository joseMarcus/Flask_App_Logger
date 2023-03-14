import logging
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Configurando os loggers
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s'
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

pessoas = [{'nome': 'Marcus', 'sexo': 'Masculino', 'idade': 27}, {'nome': 'Marcus', 'sexo': 'Masculino', 'idade': 27}]

class PessoaResource(Resource):
    def get(self):
        logging.info('Pegue todas as pessoas')
        return pessoas

    def post(self):
        logging.warning('post method not implemented')
        pass

class PessoasResource(Resource):
    def get(self, pessoa_id):
        try:
            pessoa = pessoas[pessoa_id]
            logging.info('pessoa com o id %s', pessoa_id)
            return pessoa
        except IndexError:
            logging.error('pessoa não encontrada com o id %s', pessoa_id)
            return {'error': 'pessoa não encontrada'}

    def post(self, pessoa_id):
        logging.error('error on post method called with id %s', pessoa_id)
        pass


api.add_resource(PessoaResource, '/pessoas')
api.add_resource(PessoasResource, '/pessoas/<int:pessoa_id>')


if __name__ == '__main__':
    app.run(debug=False, port=5001)
