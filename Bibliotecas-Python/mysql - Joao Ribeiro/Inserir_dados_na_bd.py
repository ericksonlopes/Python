import mysql.connector

try:
    ligacao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='python'
    )
except Exception as err:
    print('Não foi possível se conectar', err)

else:
    # adicionar um valor por vez
    def add_valor():
        cursor = ligacao.cursor()
        # inserir dados na tabela criada
        parametros = ('ana', '943604897')  # -> parametros que deseja adicionar
        sql = 'INSERT INTO clientes VALUES(0, %s, %s)'  # -> código para adicionar os valores de parametros
        cursor.execute(sql, parametros)  # -> junta o aprametro com o código de uma forma protegida
        ligacao.commit()  # _->faz a inserção do código dentro da bd

    # adicionar varios valores
    def add_valores():
        cursor = ligacao.cursor()

        parametros = [
            ('calos', '51654665'),
            ('antonio', '5135484'),
            ('variss', '51654684'),
            ('lucas', '577885644')
        ]
        sql = 'INSERT INTO clientes VALUES(0, %s, %s)'  # expressão para adicionar valores

        cursor.executemany(sql, parametros)  # -> executemany tem o sql e uma sequencia de parametros
        ligacao.commit()  # -> fazer alterações

        print(cursor.rowcount, '+ registros foram inseridos') # -> conta a quantidade de linhas introduzidas

    add_valores()
