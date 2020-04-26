import mysql.connector

try:
    ligacao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='minhadatabase'
    )
except Exception as err:
    print('Ocorreu um erro', err)

else:
    cursor = ligacao.cursor()

    # Classifique o resultado em ordem alfabética por nome: resultado:
    cursor.execute('SELECT * FROM costumizada ORDER BY nome')

    resultado = cursor.fetchall()

    print(resultado)
