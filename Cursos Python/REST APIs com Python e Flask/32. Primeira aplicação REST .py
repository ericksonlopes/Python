from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# primeiro recurso da api
class Hoteis(Resource):
    # função para pegar dado
    def get(self):
        return {'hoteis': 'meus hoteis'}


api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/hoteis
