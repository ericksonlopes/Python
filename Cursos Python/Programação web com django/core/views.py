from django.shortcuts import render


# Create your views here.

def index(request):
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuario não esta logado'
    else:
        teste = 'Usuario logado'

    context = {"curso": "Reprogramação",
               "outro": 'programação',
               'user': teste}
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
