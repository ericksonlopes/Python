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
    print('Não foi possível se conectar ao servidor', err)

else:
    print(ligacao)