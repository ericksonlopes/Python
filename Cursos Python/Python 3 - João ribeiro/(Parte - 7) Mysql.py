# instalar o mysql-connector
# pip install mysql-connector

# importando mysql
import mysql.connector

ligacao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database='python'
)

# se um objeto for retornado significa que a ligação existe
print(ligacao)

# # cria um objeto no qual podemos escrever argumentos sql
# cursor = ligacao.cursor()

# cria a base de dados, só pode ser criada uma vez se ja existir retorna erro
# cursor.execute("CREATE DATABASE python")

# # Verifica quais base de dados existem no servidor local
# cursor.execute('SHOW DATABASES')
# for db in cursor:
#     print(db)

# # criar nossa primeira tabela
# cursor.execute('CREATE TABLE clientes(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50), telefone VARCHAR(20))')

# # inserir valores na base de dados
# params = ("ana", "43604897")
# sql = "INSERT INTO clientes VALUES(0, %s, %s)"
# cursor.execute(sql, params)
# ligacao.commit()

# # inserir multiplos valores na base de dado
# params = [
#     ("ana", "43604897"),
#     ("anasda", "436504897"),
#     ("agdsna", "436604897")
# ]
#
# sql = "INSERT INTO clientes VALUES(0, %s, %s)"
# cursor.executemany(sql, params)
# ligacao.commit()

# # ler informações de dados
# cursor.execute('SELECT * FROM clientes')
# # transformar em lista
# resultados = cursor.fetchall()
# # exibir cada linha
# [print(linha) for linha in resultados]

# # ler informações em um dicionario
# cursor = ligacao.cursor(dictionary=True)
# cursor.execute('SELECT * FROM clientes')
# [print(linha) for linha in cursor]  

# 
