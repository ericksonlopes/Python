from flask import Flask, redirect, url_for

app = Flask(__name__)


# rota de acesso
@app.route('/redirect')
def rendimenciona():
    return redirect(url_for("response"))


# rota de acesso
@app.route('/response')
def response():
    user = {'user': 'Erickson'}
    return user


if __name__ == '__main__':
    # debug para qualquer alteração feita não rpecisar reiniciar
    app.run(debug=True)
