import requests


def get_ful():
    req = requests.get('http://127.0.0.1:5000/ninjas')
    print(req.status_code)
    return req.text


def get_id(id_nome):
    req = requests.get(f'http://127.0.0.1:5000/ninjas/{id_nome}')
    print(req.text, req.status_code)


def post_id(id_nome):
    personagem = {
        'altura': 1.75,
        'cla': 'Shinobi'
    }
    req = requests.post(f'http://127.0.0.1:5000/ninjas/{id_nome}', personagem)
    print(req.text, req.status_code)


def put_id(id_nome):
    atualizar = {
        'altura': 1.90,
        'cla': 'CAnino'
    }
    req = requests.put(f'http://127.0.0.1:5000/ninjas/{id_nome}', atualizar)
    print(req.text, req.status_code)


def delete_id(id_nome):
    req = requests.delete(f'http://127.0.0.1:5000/ninjas/{id_nome}')
    print(req.text, req.status_code)


if __name__ == '__main__':
    delete_id('Madara Uchiha')
    print(get_ful())
    # post_id('hidra')
    # get_id('Madara Uchiha')
    # put_id('Madara Uchiha')
