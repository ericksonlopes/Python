from flask_restful import Resource
from flask_restful import reqparse
from models.models import HotelModel
from flask_jwt_extended import jwt_required



class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}


class Hotel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome')
    atributos.add_argument('estrelas')
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')

    def get(self, id_hotel):
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel:
            return hotel.json()
        return {'message': 'hotel not found'}, 404

    @jwt_required
    def post(self, id_hotel):
        if HotelModel.find_hotel(id_hotel):
            return {'message': 'Hotel ja existe'}, 400

        dados = self.atributos.parse_args()
        hotel = HotelModel(id_hotel, **dados)
        hotel.save_hotel()
        return hotel.json()

    @jwt_required
    def put(self, id_hotel):
        dados = Hotel.atributos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        hotel = HotelModel(id_hotel, **dados)
        hotel.save_hotel()
        return hotel.json(), 201

    @jwt_required
    def delete(self, id_hotel):
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel:
            hotel.delete_hotel()
            return {"message": "Hotel deleted."}, 200
        return {"Message": "Hotel Not found"}, 404
