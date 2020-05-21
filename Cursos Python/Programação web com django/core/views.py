from django.shortcuts import render
from .models import Produto


def index(request):
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuario não esta logado'
    else:
        teste = 'Usuario logado'

    produtos = Produto.objects.all()

    context = {"curso": "Reprogramação",
               "outro": 'programação',
               'user': teste,
               'produtos': produtos}
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)
