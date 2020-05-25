from django.http import HttpResponse


def hello(request):
    return HttpResponse('Olá mundo')


def articles(request, anos):
    return HttpResponse(f'ele tem {anos}')
