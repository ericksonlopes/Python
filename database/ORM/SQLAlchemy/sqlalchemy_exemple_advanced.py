from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base classes for all tables"""
    pass


class User(Base):
    """User table"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'User {self.name}'


engine = create_engine('sqlite:///:memory:', echo=False)

# Create all tables
Base.metadata.create_all(engine)


class Session:
    """Context manager for session"""

    def __init__(self):
        # Create a session
        self.session = sessionmaker(bind=engine)()

    def __enter__(self):
        return self.session

    def __exit__(self, *args, **kwargs):
        self.session.commit()
        self.session.close()


class SQLAlchemyCRUD:
    """CRUD operations using SQLAlchemy"""

    def __init__(self):
        self.session = sessionmaker(bind=engine)()

    def create(self, obj):
        self.session.add(obj)
        print(f'Object {obj} created')

    def read_all(self, model):
        return self.session.query(model).all()

    def read(self, id_user):
        return self.session.query(User).filter_by(id=id_user).first()

    def update(self, id_user: int, dict_update: dict):
        self.session.query(User).filter(User.id == id_user).update(dict_update)
        print(f'User {id_user} updated')

    def delete(self, id_user: int):
        user = self.session.query(User).filter(User.id == id_user)
        user.delete()
        print(f'id User {id_user} deleted')

    def __exit__(self, *args, **kwargs):
        self.session.commit()
        self.session.close()


if __name__ == '__main__':
    with Session() as session:
        session.add(User(name='Joana', password='123'))

    with Session() as session:
        users = session.query(User).all()

        for user in users:
            print(user)

    orm = SQLAlchemyCRUD()

    orm.create(User(name='John', password='123'))

    # read all
    print(orm.read_all(User))

    # read
    user = orm.read(1)
    print(user)

    # update
    orm.update(1, {'name': 'Marta'})

    # delete
    orm.delete(1)
