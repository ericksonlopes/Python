import requests

x = {'nome': 'lllllll',
     'estrelas': 0.0,
     'diaria': 0.0,
     'cidade': 'louaries'}
req = requests.post('http://127.0.0.1:5000/hotel/sggizi', x)

print(req.status_code)
print(req.text)

red = requests.delete('http://127.0.0.1:5000/hotel/sggizi')
print(red.text)
print(red.status_code)
