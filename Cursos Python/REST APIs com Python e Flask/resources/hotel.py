from modelos.modelos import HotelModel
from flask_restful import Resource, reqparse


# primeiro recurso da api
class Hoteis(Resource):
    # função para pegar dado
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}


class Hotel(Resource):
    arqgumentos = reqparse.RequestParser()
    arqgumentos.add_argument('nome', type=str, required=True, help='o nome não pode ser deixado em branco')
    arqgumentos.add_argument('estrelas', type=float, required=True, help='Colocar estrelas')
    arqgumentos.add_argument('diaria')
    arqgumentos.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        # se existe hotel
        if hotel is not None:
            return hotel.json()
        return {'message': 'O Hotel não foi encontrado.'}, 404  # informa que não foi encontrado

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": f"hotel id='{hotel_id}' already exists"}, 400  # requisição errada
        # criar construtor
        dados = Hotel.arqgumentos.parse_args()

        hotel_objeto = HotelModel(hotel_id, **dados)
        try:
            hotel_objeto.save_hotel()
        except:
            return {'message': 'Erro interno ao salvar no banco de dados'}, 500 # internal erro
        return hotel_objeto.json()

    def put(self, hotel_id):
        dados = Hotel.arqgumentos.parse_args()

        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        # se hotel for encontrado
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            try:
                hotel_encontrado.save_hotel()
            except:
                return {'message': 'Erro interno ao salvar no banco de dados'}, 500  # internal erro
            return hotel_encontrado.json(), 200  # atualizado

        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()

        return hotel.json(), 201  # criado

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.deleted_hotel()
            except:
                return {'message': 'Erro interno ao Deletar no banco de dados'}, 500  # internal erro
            return {'message': 'Hotel deleted.'}, 200
        return {'message': 'Hotel not fuound.'}, 404
