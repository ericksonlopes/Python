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

    # Você pode atualizar registros existentes em uma tabela usando a instrução "UPDATE":
    sql = "UPDATE costumizada SET nome = %s WHERE nome = %s"
    val = ('Jonas fulano', "joao")

    cursor.execute(sql, val)

    # fazer alterações
    ligacao.commit()

    print(cursor.rowcount, '+ linhas(s) afetadas')