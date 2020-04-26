import sqlite3

ligacao = sqlite3.connect('banco.bd')

print(type(ligacao))