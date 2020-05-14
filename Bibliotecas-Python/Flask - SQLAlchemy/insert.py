from main import User
from sql_alchemy import banco

me = User('adim', 'admin@gmail')
banco.session.add(me)
banco.session.commit()
