# -*- coding: iso-8859-1 -*-
"""
Funções de maior grandeza

 - funções com argumentos para outras funções

"""


def soma(a, b):
    return a + b


def calculo(a, b, funcao):
    return funcao(a, b)


print(calculo(5, 3, soma))

"""
funções aninhadas

em python podemos ter funções dentro de funções (funções internas)

"""

from random import choice


def cumprimentar(pessoa):
    def humor():
        return choice(['Estou feliz,', 'Estou triste,', 'Estou bem,'])
    return humor() + pessoa


print(cumprimentar(' Gean'))
