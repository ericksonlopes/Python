import sqlite3

ligacao = sqlite3.connect('banco.db')
cursor = ligacao.cursor()

valores = [(100, 'sergio', '15464564')]

for registro in valores:
    cursor.execute('INSERT INTO cliente VALUES (?,?,?)', registro)

ligacao.commit()