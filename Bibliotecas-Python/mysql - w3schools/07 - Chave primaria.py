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

# inserirá um número exclusivo para cada registro
cursor.execute('CREATE TABLE costomizada_PK (id INT AUTO_INCREMENT PRIMARY KEY, '
               'nome VARCHAR(25), telefone VARCHAR(18))')
