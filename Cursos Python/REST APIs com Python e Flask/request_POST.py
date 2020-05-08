import requests

itens = {
    'nome': 'maveric',
    'estrelas': 5.3,
    'diaria': 124.0,
    'cidade': 'São Paulo'
}

red_post = requests.post('http://127.0.0.1:5000/hoteis/Deltas', itens)
