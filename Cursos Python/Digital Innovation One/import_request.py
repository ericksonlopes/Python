import requests


def cep():
    responde = requests.get('https://viacep.com.br/ws/01001000/json/')
    # Verifica se esta disponivel
    print(responde.status_code)
    # imprime todo texto
    print(responde.text, '\n')

    # converte para um dicionario
    print(responde.json())
    # mostra o dipo
    print(type(responde.json()), '\n')

    # armazena o dicionario em uma variavel
    dados_cep = responde.json()
    # exibe a chave dentro do dicionario
    print('Rua: '+dados_cep['logradouro'])


def retorna_response(url):
    response = requests.get(url)
    return response.text


response = retorna_response('https://www.arduino.cc/')
print(response)
