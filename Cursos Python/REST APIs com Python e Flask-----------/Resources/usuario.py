from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, help='Não pode ser deixado em branco: login')
atributos.add_argument('senha', type=str, help='Não pode ser deixado em branco: senha')


class User(Resource):
    def get(self, id_user):
        user = UserModel.find_user(id_user)
        if user:
            return user.json()
        return {'message': 'user not found'}, 404

    @jwt_required
    def delete(self, id_user):
        user = UserModel.find_user(id_user)
        if user:
            user.delete_user()
            return {"message": "user deleted."}, 200
        return {"Message": "user Not found"}, 404


class UserRegister(Resource):
    def post(self):
        dados = atributos.parse_args()

        if UserModel.find_by_user(dados['login']):
            return {"message": f"login ja existe {dados['login']}"}
        user = UserModel(**dados)
        user.save_user()
        return {'message': 'sucesso '}, 201


class UserLogin(Resource):
    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_user(dados['login'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            token_acesso = create_access_token(identity=user.id_user)
            return {'acess': token_acesso}, 200
        return {'message': 'incorreto senha usuario'}, 401


class UserLogout(Resource):
    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti']  # identificador do token
        BLACKLIST.add(jwt_id)
        return {"message": "deslogou com sucesso"}

