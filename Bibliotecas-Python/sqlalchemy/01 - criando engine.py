from sqlalchemy import create_engine

engine = create_engine('sqlite:///:banco.db')

# conn = engine.connect()
# conn.execute('select * from tagbela')

# trans = conn.begin()
# conn.execute('INSERT INTO "EX1" (name) '
#              'VALUES ("Hello")')
# trans.commit()
