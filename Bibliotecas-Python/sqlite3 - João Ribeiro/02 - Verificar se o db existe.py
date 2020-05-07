import os

if os.path.exists('banco.db'):
    print('O banco de dados existe')
else:
    print('O banco de dados não existe')
    print('criando banco de dados')
    try:
        open('banco.bd', 'x')
    except Exception as err:
        print('ocorreu um erro ao criar o banco de dados\n', err)
    else:
        print('Banco de dados criado com sucesso')