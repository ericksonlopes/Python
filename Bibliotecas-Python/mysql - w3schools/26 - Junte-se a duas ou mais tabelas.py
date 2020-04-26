import mysql.connector

try:
    ligacao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='minhadatabase'
    )
except Exception as err:
    print('Ocorreu um erro', err)


else:
    # Comercial
    # { id: 1, name: 'John', fav: 154},
    # { id: 2, name: 'Peter', fav: 154},
    # { id: 3, name: 'Amy', fav: 155},
    # { id: 4, name: 'Hannah', fav:},
    # { id: 5, name: 'Michael', fav:}
    # produtos
    # { id: 154, name: 'Chocolate Heaven' },
    # { id: 155, name: 'Tasty Lemons' },
    # { id: 156, name: 'Vanilla Dreams' }

    # Junte-se a usuários e produtos para ver o nome do produto favorito dos usuários:
    sql = "SELECT \
      users.name AS user, \
      products.name AS favorite \
      FROM users \
      INNER JOIN products ON users.fav = products.id"
    cursor = ligacao.cursor(sql)

    res = cursor.fetchall()

    print(res)