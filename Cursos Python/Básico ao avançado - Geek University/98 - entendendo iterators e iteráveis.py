# -*- coding: utf-8 -*-

"""
Entendendo iterators e Iterables

Iterator ->
    um objeto que pode ser iterado
    um objeto que retorna um dado, sendo um elemento por vez quando uma função next é chamada

iterable ->
    um objeto que irá retornar um iterator quando a função iter for chamada.

"""

palavra = 'Palavra'
extenco = ['p', 'a', 'l', 'a', 'v', 'r', 'a,']

x = iter(extenco)
y = iter(palavra)

print(next(x))
print(next(x))

print(next(y))
print(next(y))
