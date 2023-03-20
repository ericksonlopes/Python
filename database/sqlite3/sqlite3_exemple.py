import sqlite3


class SQLite:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS users (name text, login integer)')
        
    def create(self, data: dict):
        self.c.execute('INSERT INTO users VALUES (?, ?)', (data['name'], data['login']))
        self.conn.commit()
    
    def read_all(self):
        self.c.execute('SELECT * FROM users WHERE name')
        return self.c.fetchone()
    
    def read(self, name: str):
        self.c.execute('SELECT * FROM users WHERE name=?', (name,))
        return self.c.fetchone()
    
    def update(self, new_data: dict):
        self.c.execute('UPDATE users SET login=? WHERE name=?', (new_data['login'], new_data['name']))
        self.conn.commit()
        
    def delete(self, query: dict):
        self.c.execute('DELETE FROM users WHERE name=?', (query['name'],))
        self.conn.commit()

if __name__ == '__main__':
    sqlite = SQLite()
    
    # create
    sqlite.create({'name': 'John', 'login': 1})
    print(sqlite.read('John'))
    
    # update
    sqlite.update({'name': 'John', 'login': 0})
    print(sqlite.read('John'))
    
    # delete
    sqlite.delete({'name': 'John'})
    print(sqlite.read('John'))
    
    # read all
    sqlite.create({'name': 'John', 'login': 1})
    sqlite.create({'name': 'Jane', 'login': 0})
    print(sqlite.read_all())
    
    