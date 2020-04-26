import requests

dados = requests.get('https://economia.awesomeapi.com.br/json/all')
lista = dados.json()
dolar = float(f"{float(lista['USD']['high']):.2f}")

real = float(input('Quanto você tem para converter? :'))
em_dolar = real / dolar

print(f'Com R${real:.2f} você pode comprar US${em_dolar:.2f}')
