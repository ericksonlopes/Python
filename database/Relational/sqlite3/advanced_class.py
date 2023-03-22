import sqlite3


class ConnSQLite:
    def __init__(self, conn_str) -> None:
        self.conn = sqlite3.connect(conn_str)

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, *args, **kwargs):
        self.conn.close()


if __name__ == '__main__':

    conn_str = 'database.db'
    with ConnSQLite(conn_str) as cursor:
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS users (name text, login integer)')
        cursor.execute('INSERT INTO users VALUES (?, ?)', ('John', 1))
        cursor.execute('SELECT * FROM users WHERE name')
        print(cursor.fetchone())
