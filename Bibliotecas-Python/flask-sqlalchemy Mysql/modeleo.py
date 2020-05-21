from sqlalchemy import *

engine = create_engine('sqlite:///banco.db')

meta = MetaData()


employees = Table('employees', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(60), nullable=False, key='name'))
# employees.create(engine)

employees.insert(Table(id='sadas', name='zfsaf'))

use =


