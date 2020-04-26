# instalar mysql -> pip install mysql-connector

# importando biblioteca
import mysql.connector

# conectando ao servidor
try:
    ligacao = mysql.connector.connect(
        host='localhost',  # -> Endereço local
        user='root',  # -> Usuário
        passwd=''  # -> Senha
    )

except Exception as err:
    print('Não foi possível se conectar ao servidor\n', err)

else:
    # cria um objeto para podermos incrementar elementos sql
    cursor = ligacao.cursor()

    try:
        # permite acesso a função que realiza os comandos sql
        cursor.execute('CREATE DATABASE python')  # -> cria uma base de dados chamada python
    except Exception as err:
        print('Não foi possível criar o banco de dados\n', err)
    else:
        print('Banco de dados criado com sucesso')


