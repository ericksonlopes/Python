# importa biblioteca, depois da instalação
import mysql.connector

# criando conexao
meu_banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='minhadatabase'
)

# criando cursor
cursor = meu_banco.cursor()

# seleciona todos os itens da database
cursor.execute('SELECT * FROM costumizada')

# busca todas as linhas da última instrução executada.
resultado = cursor.fetchall()

for linha in resultado:
    print(linha)
