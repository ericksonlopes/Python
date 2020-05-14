import requests


def get(rota):
    req = requests.get(f'http://127.0.0.1:5000{rota}')
    print(req.status_code)
    print(req.text)


if __name__ == '__main__':
    get('/')