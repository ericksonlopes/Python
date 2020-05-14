from flask import Flask, redirect, url_for, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# onde a extenção sera usada
Bootstrap(app)


# rota de acesso
@app.route('/redirect')
def rendimenciona():
    return redirect(url_for("response"))


# rota de acesso
@app.route('/response')
def response():
    user = {'user': 'Erickson'}
    return render_template('response.html')


if __name__ == '__main__':
    # debug para qualquer alteração feita não rpecisar reiniciar
    app.run(debug=True)
