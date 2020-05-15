import requests
from requests.auth import HTTPDigestAuth
import json

red = requests.post('http://127.0.0.1:5000/login', {"login": "ersad", "senha": "123"})
token = red.text

# print(token)
# x = {'nome': 'lllllll',
#      'estrelas': 0.0,
#      'diaria': 0.0,
#      'cidade': 'louaries'
#      }
#
auth_token = f"Bearer {json.loads(token)['acess']}"
hed = {"Authorization": auth_token}
# req = requests.post('http://127.0.0.1:5000/hotel/sggizif', data=x, headers={"Authorization": f"{auth_token}"})
#
# print(req.status_code)
# print(req.text)

red = requests.post('http://127.0.0.1:5000/logout', headers={"Authorization": f"{auth_token}"})
print(red.text)
print(red.status_code)

# red = requests.post('http://127.0.0.1:5000/cadastro', {"login": "ersad", "senha": "123"})
# print(red.text)
# print(red.status_code)


