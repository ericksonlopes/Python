import sqlite3

ligacao = sqlite3.connect('banco.db')
cursor = ligacao.cursor()

cursor.execute('SELECT * FROM cliente')
dados = cursor.fetchall()

print(dados)
for linha in dados:
    print(f'id: {linha[0]} nome: {linha[1]} numero: {linha[2]}')

