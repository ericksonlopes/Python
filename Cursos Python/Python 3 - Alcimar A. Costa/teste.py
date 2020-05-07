import urllib.request
import json
from pprint import pprint

# https://www.facebook.com/RenanRodrigues278

url = 'https://graph.facebook.com/fmasanori'
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('UTF-8'))
pprint(data)
