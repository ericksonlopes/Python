from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


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


def procura_nome_pessoa(request, name):
    pessoa = lerBanco(name)
    return render(request, 'pessoa.html', {'pessoa': pessoa})
