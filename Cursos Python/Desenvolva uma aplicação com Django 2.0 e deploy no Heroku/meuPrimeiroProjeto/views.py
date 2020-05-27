from django.http import HttpResponse


def hello(request):
    return HttpResponse('Olá mundo')


def articles(request, anos):
    return HttpResponse(f'ele tem {anos}')


def lerBanco(nome):
    lista_nomes = [
        {'nome': 'Marcelo', 'idade': 18},
        {'nome': 'adriana', 'idade': 28},
        {'nome': 'lucia', 'idade': 48}
    ]
    for item in lista_nomes:
        if item['nome'] == nome:
            return f'O {item["nome"]} tem {item["idade"]} anos'
    return 'Nenhum item encontrado'


def procura_nome(request, name):
    return HttpResponse(lerBanco(name))
