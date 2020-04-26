import mysql.connector

try:
    ligacao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='python'
    )

except Exception as err:
    print('Ocorreu um erro \n', err)

else:
    def atualizar_telefone():
        cursor = ligacao.cursor()
        parametros = ('00000000', 'antonio')
        sql = 'UPDATE clientes SET telefone = %s WHERE nome = %s'
        cursor.execute(sql, parametros)
        ligacao.commit()

    atualizar_telefone()