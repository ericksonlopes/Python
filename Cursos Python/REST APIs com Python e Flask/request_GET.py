import json
import requests
import pandas as pd

req = requests.get('http://127.0.0.1:5000/hoteis')

recebido = json.loads(req.text)
for item in recebido['hoteis']:
    print(item)

print()

x = pd.DataFrame(recebido['hoteis'])
print(x)