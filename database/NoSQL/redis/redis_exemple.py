# pip install redis
import redis


class Redis:
    def __init__(self, host, port, db):
        redis_pool = redis.ConnectionPool(
            host=host,
            port=port,
            db=db,
        )
        self.client = redis.Redis(connection_pool=redis_pool)

    def create(self, data: dict):
        self.client.set(data['name'], data['login'])

    def read(self, name: str):
        return self.client.get(name)

    def update(self, new_data: dict):
        self.client.set(new_data['name'], new_data['login'])

    def delete(self, query: dict):
        self.client.delete(query['name'])

    def create_hash(self, data: dict):
        self.client.hset(data['name'], "login", str(data))

    def read_hash(self, name: str):
        return self.client.hgetall(name)

    def update_hash(self, new_data: dict):
        self.client.hset(new_data['name'], "login", str(new_data))

    def delete_hash(self, query: dict):
        self.client.hdel(query['name'], "login")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
        self.client.flushdb()


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 6379
    DB = 0
    redis = Redis(HOST, PORT, DB)

    # create
    redis.create({'name': 'John', 'login': 1})
    print(redis.read('John'))

    # update
    redis.update({'name': 'John', 'login': 0})
    print(redis.read('John'))

    # delete
    redis.delete({'name': 'John'})
    print(redis.read('John'))

    # create hash
    redis.create_hash({'name': 'John', 'login': 1})
    print(redis.read_hash('John'))

    # update hash
    redis.update_hash({'name': 'John', 'login': 0})
    print(redis.read_hash('John'))

    # delete hash
    redis.delete_hash({'name': 'John'})
    print(redis.read_hash('John'))
