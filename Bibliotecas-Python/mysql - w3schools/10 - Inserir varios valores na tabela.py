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
valores = [
    ('joao', '5165464'),
    ('asdasdjoao', '58498165464'),
    ('joaasdsao', '855165464')
]

# Adicionar varios valores 
cursor.executemany(sql, valores)

meu_banco.commit()
print(cursor.rowcount, '+Itens adicionados')