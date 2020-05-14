from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# referencia da classe Flask
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Página em branco'


if __name__ == '__main__':
    app.run(debug=True)
