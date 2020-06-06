"""
Módulos Builtin ( módulos integrados que ja vem instalado no python)


"""

for i in dir(__builtins__):
    print(i)

# # apelidando importações
# import random as aleatorio
# import matplotlib as graficos
#
# print(graficos)
# print(aleatorio.random())

# # improtando todas as funções
# from random import *
#
# print(random())
# # importando mais de uma função
# from random import randint, random

# # apelidando função preferenciada
# from random import randint as randomint
#
# print(randomint(1, 9))

# para melhor visualização solocamos as funções importadas em uma tupla
from random import (
    random,
    randint,
    choice)


