import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = 'create table if not exists hoteis(' \
              'hotel_id text PRIMARY KEY, ' \
              'nome text,' \
              'estrelas real,' \
              'diaria real,' \
              'cidade text)'

cria_hotel = "INSERT INTO hoteis VALUES ('GH', 'alphaprime', 4.3, 450.00, 'Rio de Janeiro')"

cursor.execute(cria_hotel)
cursor.execute(cria_tabela)
connection.commit()
connection.close()
