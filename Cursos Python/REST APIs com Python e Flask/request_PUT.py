import requests

itens = {
    'nome': 'trsit',
    'estrelas': 2,
    'diaria': 20.45,
    'cidade': 'goas'
}

red_put = requests.put('http://127.0.0.1:5000/hoteis/suzin', itens)
print(red_put.text)