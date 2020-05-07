from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [
    {
        'hotel_id': 'Alpha',
        'nome': 'Truncafuriador',
        'estrelas': 4.5,
        'diaria': 453.10,
        'cidade': 'Rio de janeiro'
    },
    {
        'hotel_id': 'Alp',
        'nome': 'Trunc',
        'estrelas': 3.5,
        'diaria': 254.44,
        'cidade': 'São Paulo'
    },
    {
        'hotel_id': 'hak',
        'nome': 'furiador',
        'estrelas': 2.5,
        'diaria': 100.87,
        'cidade': 'Rio de janeiro'
    }
]


# primeiro recurso da api
class Hoteis(Resource):
    # função para pegar dado
    def get(self):
        return {'hoteis': hoteis}


api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/hoteis
