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


engine = create_engine('sqlite:///:memory:', echo=True)

# Create all tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

session.add(User(name='John', password='123'))
session.commit()

users = session.query(User).all()

for user in users: 
    print(user)

