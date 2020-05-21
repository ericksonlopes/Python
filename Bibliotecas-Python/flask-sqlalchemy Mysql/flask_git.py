from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'rf_db_v'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        details = request.form
        cur = mysql.connection.cursor()
        cur.execute("select * from pessoas")
        return {"asdas", f"{cur.fetchall()}"}

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
