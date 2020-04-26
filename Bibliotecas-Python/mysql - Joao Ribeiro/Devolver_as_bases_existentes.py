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
        cursor.execute('SHOW DATABASES')  # -> devolve as bases de dados existentes
    except Exception as err:
        print('Não foi possível criar o banco de dados\n', err)
    else:
        # fazendo iteração por todas as bases
        for bd in cursor:
            print(bd)
