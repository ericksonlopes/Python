import requests


cabecalho = {'User-agent': 'windows 12', 'Referer': 'https://google.com'}


try:
    # site 'putsreq'

    requisicao = requests.post('https://putsreq.com/MnzxbkRydd2heaJB1eLL', headers=cabecalho)

    if requisicao.status_code == 200:
        print('O site esta em funcionamento')
        # ver código fonte

    texto = requisicao.text

except Exception as err:
    print('requisição deu erro', err)

else:
    print(texto)


