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

    # Se você deseja retornar cinco registros, começando no terceiro registro, você pode usar a palavra-chave "OFFSET":
    cursor.execute('SELECT * FROM costumizada LIMIT 5 OFFSET 2')

    resultado = cursor.fetchall()

    print(resultado)