# -*- coding: iso-8859-1 -*-

"""
O que são Decoradores?

    - Decorators são funções
    -  que envolvem outras funções e tem uma sintax própria, usando "@" (syntact Sugar)

"""


# def seja_educado(funcao):
#     def sendo():
#         print('Foi um prazer conhecer você!')
#         funcao()
#         print('Tenha um ótimo dia!')
#
#     return sendo()
#
#
# def saudacao():
#     print('Seja bem vindo ao meu curso')
#
#
# def raiva():
#     print('Ja pode se retirar')
#

# seja_educado(saudacao)
# print()
# seja_educado(raiva)

def seja_educado(funcao):
    def sendo():
        print('seja bem vindo')
        funcao()
        print('otimo dia ')

    return sendo()


@seja_educado
def legal():
    print('estou inserido aqui')



