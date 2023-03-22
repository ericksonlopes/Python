# pip install pymongo
import pymongo


class MongoDB:
    def __init__(self, url):
        self.client = pymongo.MongoClient(url)
        self.db = self.client['tests']
        self.collection = self.db['users']

    def create(self, data: dict):
        result = self.collection.insert_one(data)
        print('Documento criado:', result.inserted_id)
        return result.inserted_id

    def read(self, query: dict):
        results = self.collection.find(query)
        print('Documentos encontrados:')
        for result in results:
            print(result)
        return results

    def update(self, query: dict, new_data: dict):
        result = self.collection.update_one(query, new_data)
        print('Documento atualizado:', result.modified_count)
        return result.modified_count

    def delete(self, query: dict):
        result = self.collection.delete_one(query)
        print('Documento excluído:', result.deleted_count)
        return result.deleted_count

    def drop(self):
        self.collection.drop()
        print('Coleção excluída.')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
        print('Conexão fechada.')


if __name__ == '__main__':
    URL_MONGODB = 'mongodb://localhost:27017/'
    mongo = MongoDB(URL_MONGODB)

    # create
    mongo.create({'name': 'John', 'login': True})
    mongo.read({'name': 'John'})

    # update
    mongo.update({'name': 'John'}, {'$set': {'login': False}})
    mongo.read({'name': 'John'})

    # delete
    mongo.delete({'name': 'John'})
    mongo.read({'name': 'John'})

    # drop collection and database
    mongo.drop()
    mongo.db.client.drop_database('tests')
