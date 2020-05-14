from flask import Flask
from sql_alchemy import banco

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def cria_banco():
    banco.create_all()


@app.route('/')
def index():
    return 'olá'


class User(banco.Model):
    __tablename__ = 'user'
    id = banco.Column(banco.Integer, primary_key=True)
    username = banco.Column(banco.String(80), unique=True, nullable=False)
    email = banco.Column(banco.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
