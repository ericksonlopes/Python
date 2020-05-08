import requests

req_del = requests.delete('http://127.0.0.1:5000/hoteis/suzin')

print(req_del.text)