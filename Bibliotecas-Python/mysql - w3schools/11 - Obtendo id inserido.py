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

# comando para adicionar
sql = 'INSERT INTO costumizada (nome, telefone) VALUES(%s, %s)'
valores = ('erickson', '515465464')

# Adicionar varios valores
cursor.execute(sql, valores)

meu_banco.commit()
print(cursor.rowcount, '+ Itens adicionados')
print(cursor.lastrowid, '+ Iten no id ')
