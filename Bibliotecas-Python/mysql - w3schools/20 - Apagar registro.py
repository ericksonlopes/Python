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
    sql = 'DELETE FROM costumizada WHERE id = 13'

    cursor.execute(sql)

    ligacao.commit()

    print(cursor.rowcount, '+ item deletado')

    # Importante !: Observe a declaração: ligacao.commit() .
    # É necessário fazer as alterações, caso contrário,
    # nenhuma alteração será feita na tabela.

    # Observe a cláusula WHERE na sintaxe DELETE:
    # A cláusula WHERE especifica quais registros devem ser excluídos.
    # Se você omitir a cláusula WHERE, todos os registros serão excluídos!
