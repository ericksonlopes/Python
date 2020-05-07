from flask_restful import Resource

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


class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'O Hotel não foi encontrado.'}, 404 # informa que não foi encontrado

    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
