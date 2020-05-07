# -*- coding: utf-8 -*-
"""
Docoratorns com diferentes assinaturas

 - Passar varios parametros de um funcão decorada

 - A assinatura de uma função é representada por seu retorno e nome e parametro de entrada.

"""


# # Relembrando
# def gritar(funcao):
#     def aumentar(nome):
#         return funcao(nome).upper()
#     return aumentar
#
#
# @gritar
# def saudacao(nome):
#     return f'Olá, eu sou o {nome}'
#
#
# @gritar
# def ordenar(principal, acompanhamento):
#     return f'eu gostaria de {principal}, aompanhado de {acompanhamento}'
#
#
# print(ordenar('picanha', 'batata frita'))

# refatorando com decorator patter

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def ordenar(prato, acompanhamento):
    return f'quero {prato}, com {acompanhamento}'


print(ordenar('Picanha', 'batata'))


@gritar
def lol():
    return 'lol'


print(lol())


# vale lembrar que podemos usar padroes nomeados
print(ordenar(acompanhamento='ssalada', prato='Cheio'))


# decorator com argumentos
