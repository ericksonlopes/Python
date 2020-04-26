import mysql.connector

try:
    ligacao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        # Para acrescentar funcionalidades dentro da bd é preciso especificar a que vamos usar
        database='python'
    )
except Exception as err:
    print('Não foi possível se conectar\n', err)

else:
    cursor = ligacao.cursor()

    # criar tabela
    cursor.execute('CREATE TABLE clientes(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50), telefone VARCHAR(20))')
