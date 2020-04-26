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

    # Você pode excluir uma tabela existente usando a instrução "DROP TABLE":
    sql = 'DROP TABLE IF EXISTS costomizada_pk'

    cursor.execute(sql)
