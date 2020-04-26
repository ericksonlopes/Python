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

    # retorna apenas os valores correspondente ao valor especificado..
    cursor.execute("SELECT * FROM costumizada WHERE nome = 'joaasdsao'")

    resultado = cursor.fetchall()

    print(resultado)
