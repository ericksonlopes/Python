from django.http import HttpResponse
from django.shortcuts import render


def manda_numero(request, num):
    return HttpResponse(f'Número enviado: {num}')


def hello(request):
    return render(request, 'index.html')


def lerdobanco(nome):
    lista = [
        {'name': 'ana', 'idade': 18},
        {'name': 'camile', 'idade': 45},
        {'name': 'ponte', 'idade': 16}
    ]
    for item in lista:
        if item['name'] == nome:
            return item
    return {'name': 'item não encontrdo', 'idade': 0}


def fname(request, name):
    return HttpResponse(f'{lerdobanco(name)}')


def fname2(request, name):
    idade = lerdobanco(name)
    return render(request, 'pessoa.html', {'age': idade['idade'], 'name': idade['name']})
