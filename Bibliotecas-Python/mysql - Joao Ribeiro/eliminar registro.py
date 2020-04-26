import mysql.connector

try:
    ligacao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='python'
    )
except Exception as err:
    print('Ocorreu um erro', err)

else:
    cursor = ligacao.cursor()
    # parametro que deseja remover
    parametros = 'calos'
    # comando sql para remover
    sql = f"DELETE FROM clientes WHERE nome = '{parametros}'"
    # executar o comando sql
    cursor.execute(sql)
    # fazer alterações
    ligacao.commit()
