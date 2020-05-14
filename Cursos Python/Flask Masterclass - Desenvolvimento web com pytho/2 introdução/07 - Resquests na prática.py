from flask import Flask, request

app = Flask(__name__)


# Criando rota / quando ele acessar o site ser redimensionado para essa rota usando decorador
@app.route("/")
def index():
    # retorna um link para a rota '/posts'
    return "<a href='/posts'>Posts</a>"


# rota de acesso
@app.route('/response')
def response():
    headers = {
        'nome': 'Ericskon'
    }
    return headers


# a rota pode ser acessada de dois modos
@app.route('/posts')
@app.route('/posts/<int:id>')
def posts(id):
    titulo = request.args.get('titulo')
    data = dict(
        path=request.path,
        referrer=request.referrer,
        content_type=request.content_type,
        method=request.method,
        titulo=titulo,
        id=id if id else 0
    )
    return data


if __name__ == '__main__':
    # debug para qualquer alteração feita não rpecisar reiniciar
    app.run(debug=True)
