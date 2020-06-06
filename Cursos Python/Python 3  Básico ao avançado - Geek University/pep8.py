"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The zen of python

import this

A ideia da PEP8 é que possamos escrever códigos python de forma pythônica.
visualmente agradavel

[1] - utilize camel case(detalhes com nome) para nomes de classes;
[2] - Utilize nomes em minúsculos, separados por unuderline para funções ou variaveis;
[3] - utilize 4 espaços para identação!
[4] - Linhas em branco
- separar funções e definições dem classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;
[5] - Imports devem ser sempre feitos em linhas separadas
[6] - espaços em expressões e instruções
"""


# 1


class Calculadora:
    pass

# 2


def soma_dois():
    pass


numero = 4

numero_impar = 5

# 3
if 'a' in 'banana':
    print('tem')

# 4


class Classe:
    pass


class Outra:
    pass

# 5
# im porte errado
# import sys, os

# --import Certo
# import sys
# import os

# não há problemas em utilizar:

# from type import StringType, ListType

# caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

# from types import (
#    StryngType,
#    ListType,
#    SetType,
# )

# imports devem ser colocados no top do arquivo, logo depois de quais quer comentários ou docstrings e
# antes de constantes ou variaveis globais

# 6
# Não faça
# funcao( algo { 1 })

# faça

# funcao(algo{1})

# Não faça

# algo ( 1 )

# faça

# algo(1)

