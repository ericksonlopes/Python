import sqlite3

ligacao = sqlite3.connect('banco.db')
cursor = ligacao.cursor()

sql = 'CREATE TABLE cliente (id INTEGER PRIMERY KEY, ' \
      'nome VARCHAR(20), telefone VARCHAR(20))'

cursor.execute(sql)
