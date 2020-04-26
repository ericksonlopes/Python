import mysql.connector

try:
    ligacao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='python'
    )
except Exception as err:
    print('Não foi possível se conectar a base de dados\n', err)

else:
    def ler_tudo_lista():
        cursor = ligacao.cursor()

        # ler todas as informaçoes de clientes
        cursor.execute('SELECT * FROM clientes')

        # transforma todos os valores recebidos em uma lista
        resultados = cursor.fetchall()

        # fazendo iteração de cada linha
        for linha in resultados:
            print(linha)

    def ler_tudo_dict():
        # avisa que o cursor irá pegar os itens e inserir em
        # um dicionario com as chaves equivalentes aos nomes das colunas
        cursor = ligacao.cursor(dictionary=True)

        # seleciona todos os itens
        cursor.execute('SELECT * FROM clientes')

        # avisa que deseja armazenar os itens recebidos
        resultados = cursor.fetchall()

        # iteravel para viasualização
        for linha in resultados:
            print(linha['nome'])

    ler_tudo_dict()