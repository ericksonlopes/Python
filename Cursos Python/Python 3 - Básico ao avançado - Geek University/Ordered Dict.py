"""
módulo collections - Ordered Dict

OrderedDict -> é um dicionario que garante a ordem de inserção dos elementos

"""
# # em um dicionário a ordem de inserção não é garantida.
# dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#
# for chave, valor in dicionario.items():
#     print(f'chave = {chave}, valor = {valor}')

# from collections import OrderedDict
# dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
# print(dicionario)
#
# for chave, valor in dicionario.items():
#     print(f'chave = {chave}, valor = {valor}')



# entender a diferença entre Dict e Ordered Dict
from collections import  OrderedDict
# Dicionários comum

Dict1 = {'a': 1, 'b': 2}
Dict2 = {'b': 2, 'a': 1}

print(Dict1 == Dict2)  # True -> a Ordem dos elementos não importa para o dicionário

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False -> A Ordem dos elementos importa para o OrderedDict

