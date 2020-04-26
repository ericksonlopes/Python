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

# função para adicionar itens no sql
sql = 'INSERT INTO costumizada (nome, telefone) VALUES (%s, %s)'
# valores a cer adicionado
valores = ('JOhs', '119452364')
# executar dentro do banco os comandos
cursor.execute(sql, valores)
# realizar as alterações
meu_banco.commit()
print(cursor.rowcount, '+ itens adicionados')