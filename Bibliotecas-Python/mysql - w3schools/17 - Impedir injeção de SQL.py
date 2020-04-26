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

    # Escape dos valores da consulta usando o método %s placholder:
    sql = 'SELECT * FROM costumizada WHERE nome = %s'
    nome = ('joao', )

    cursor.execute(sql, nome)

    resultado = cursor.fetchall()

    print(resultado)