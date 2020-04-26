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

    # Você pode excluir registros de uma tabela existente usando a instrução "DELETE FROM"
    sql = 'DROP TABLE costumiza_pk'

    cursor.execute(sql)