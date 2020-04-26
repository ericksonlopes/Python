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

    #  ordem decrescente
    sql = 'SELECT * FROM costumizada ORDER BY nome DESC'

    cursor.execute(sql)

    rescultado = cursor.fetchall()

    print(rescultado)