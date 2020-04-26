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

    cursor.execute('SELECT nome FROM costumizada')

    # Se você estiver interessado apenas em uma linha, poderá usar o método fetchone() .
    resultado = cursor.fetchone()

    for item in resultado:
        print(item)