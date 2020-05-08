from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
# configura o caminho e o nome do banco/ e cria na raiz um banco sqlite
app.config['SQLALCHEMY_DA TABASE_URI'] = 'sqlite:///banco.db'
# Para não sobrecarregar o sistema com avisos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


# antes da primeira requisição
@app.before_first_request
# executa a função que cria o banco
def cria_banco():
    banco.create_all()


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
if __name__ == '__main__':
    from sql_alchemy import banco

    # instanciar objeto e passar a a aplicação que seja usada
    banco.init_app(app)
    app.run(debug=True)
