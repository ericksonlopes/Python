from modelos.modelos import HotelModelo
from flask_restful import Resource, reqparse

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
    arqgumentos = reqparse.RequestParser()
    arqgumentos.add_argument('nome')
    arqgumentos.add_argument('estrelas')
    arqgumentos.add_argument('diaria')
    arqgumentos.add_argument('cidade')

    def encontrar_hotel(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = self.encontrar_hotel(hotel_id)
        # se existe hotel
        if hotel is not None:
            return hotel
        return {'message': 'O Hotel não foi encontrado.'}, 404  # informa que não foi encontrado

    def post(self, hotel_id):

        # criar construtor
        dados = Hotel.arqgumentos.parse_args()

        hotel_objeto = HotelModelo(hotel_id, **dados)

        novo_hotel = hotel_objeto.json()

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.arqgumentos.parse_args()

        hotel_objeto = HotelModelo(hotel_id, **dados)

        novo_hotel = hotel_objeto.json()

        hotel = self.encontrar_hotel(hotel_id)
        # se hotel for encontrado
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200  # atualizado
        hoteis.append(novo_hotel)
        return novo_hotel, 201  # criado

    def delete(self, hotel_id):
        # referenciando lista de hoteis globais
        global hoteis
        # criando lista com hoteis que deseja deletar
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deletado'}
