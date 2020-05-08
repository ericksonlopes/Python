import requests

req_del = requests.delete('http://127.0.0.1:5000/hoteis/374145')

print(req_del.text)
