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

    # Você também pode selecionar os registros que iniciam, incluem ou terminam com uma determinada letra ou frase.
    # Use o % para representar caracteres curinga:
    # procurar todos que tenha a
    cursor.execute("SELECT * FROM costumizada WHERE nome LIKE '%a%'")
    # exibir em uma lista
    resultado = cursor.fetchall()

    print(resultado)
