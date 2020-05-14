from flask import Flask

app = Flask(__name__)


# rota de acesso
@app.route('/response')
def response():
    user = {'user': 'Erickson'}
    return user


if __name__ == '__main__':
    # debug para qualquer alteração feita não rpecisar reiniciar
    app.run(debug=True)
