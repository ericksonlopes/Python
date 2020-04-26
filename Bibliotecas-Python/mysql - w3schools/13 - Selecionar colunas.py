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

    # seleciona os itens da coluna especificada
    cursor.execute('SELECT nome FROM costumizada')

    resultado = cursor.fetchall()

    for item in resultado:
        print(item[0])
