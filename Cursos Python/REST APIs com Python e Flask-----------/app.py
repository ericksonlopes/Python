from flask import Flask, jsonify
from flask_restful import Api
from Resources.hotel import Hotel, Hoteis
from Resources.usuario import User, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def verificar_blacklsit(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({"message": 'você ja se deslogou'}), 404


@app.before_first_request
def cria_banco():
    banco.create_all()


api.add_resource(Hoteis, '/')
api.add_resource(Hotel, '/hotel/<string:id_hotel>')
api.add_resource(User, '/usuarios/<int:id_user>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__ == '__main__':
    from sql_alchemy import banco

    # inicia o banco
    banco.init_app(app)
    app.run()
