import requests

req = requests.get('http://127.0.0.1:5000/hoteis')
req.encoding = 'utf-8'
recebido = req.text
print(recebido)

