# importa biblioteca, depois da instalação
import mysql.connector

# criando conexao
meu_banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=''
)

meu_cursor = meu_banco.cursor()

# comando sql para exibir os bds existentes
meu_cursor.execute('SHOW DATABASES')

for data in meu_cursor:
    print(data)