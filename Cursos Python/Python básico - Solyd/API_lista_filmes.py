import requests

try:
    req = requests.get('http://www.omdbapi.com/?t=Interstellar')
except Exception as err:
    print('erro', err)

else:
    print(req)