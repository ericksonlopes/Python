# -*- coding: utf-8 -*-
"""
Preservando metadata das wraps

metadados - são dados intrínsecos em arquivos

wraps - funções que envolvem elementos com diversas finalidades
"""


# # problema
# def ver_log(funcao):
#     def logar(*args, **kwargs):
#         """Eu sou a função (logar) dentro de outra"""
#         print(f'você esta chamando a função {funcao.__name__}')
#         print(f'aqui a documentação {funcao.__doc__}')
#         return funcao(*args, **kwargs)
#     return logar
#
#
# @ver_log
# def soma(a, b):
#     """retorna dois números"""
#     return a + b
#
#
# print(soma(10, 30))

# resolução

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou a função (logar) dentro de outra"""
        print(f'você esta chamando a função {funcao.__name__}')
        print(f'aqui a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """retorna dois números"""
    return a + b


print(soma.__name__)
print(soma.__doc__)

