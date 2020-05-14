from flask import Flask
from flask_restful import Api
from Resources.hotel import Hotel, Hoteis

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def cria_banco():
    banco.create_all()


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hotel/<string:id_hotel>')

if __name__ == '__main__':
    from sql_alchemy import banco

    # inicia o banco
    banco.init_app(app)
    app.run()
