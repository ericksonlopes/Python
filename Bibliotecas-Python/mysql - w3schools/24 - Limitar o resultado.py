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

    # Você pode limitar o número de registros retornados da consulta, usando a instrução "LIMIT":
    cursor.execute('SELECT * FROM costumizada LIMIT 5')

    resultado = cursor.fetchall()

    print(resultado)