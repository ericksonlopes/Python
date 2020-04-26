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

# colocar uma coluna nova em uma base existente
cursor.execute('ALTER TABLE costumizada ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')
