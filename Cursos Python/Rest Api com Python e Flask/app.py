from flask import Flask
from flask_restful import Api
from resources.ninjas_resources import Ninjas, Ninja


# aplicação que irá executar o código especificando o nome
app = Flask(__name__)
# especificando onde a api irá ser executada e realiza o regenciamento  dos recursos
api = Api(app)

# Adicionar recursos para fazer requisições
api.add_resource(Ninjas, "/ninjas")
# irá receber o id_nome e passar para a classe Ninja(Resources)
api.add_resource(Ninja, '/ninjas/<string:id_nome>')

if __name__ == '__main__':
    # executa a api
    app.run()

