# importa biblioteca, depois da instalação
import mysql.connector

# criando conexao
meu_banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=''
)

# criando cursor
meu_cursor = meu_banco.cursor()

# criando uma tabela atravez de comando sql
meu_cursor.execute('CREATE DATABASE minhadatabase')
