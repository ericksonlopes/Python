import requests

dado_usuario = input('Por favor, digite o CEP que você gostaria de procurar na base (ex: 00000000): ')

print(dado_usuario)
# filtra qualquer adereço a mais que o usuário possa colcocar, converte para apenas numeros na string
cep = ''.join(list(filter(lambda num: num.isnumeric(), dado_usuario)))

print(cep)
# recebe os dados
dados_serve = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

# verifica se esta disponivel, deve receber 200 para estar disponivel
if dados_serve.status_code != 200:
    print('CEP não encontrado, por favor digite um valor válido')
else:
    # retorna na variavel um dicionario com as informações
    dados = dados_serve.json()

    print('')
    try:
        print(dados['cep'])
        print(dados['logradouro'])
        print(dados['bairro'])
        print(dados['localidade'])
        if dados['complemento'] == '':
            print('indisponivel')
        else:
            print(dados['complemento'])
    except KeyError:
        print('cep inválido, certifique que digitou o cep correto')

