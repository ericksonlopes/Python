# -*- coding: utf-8 -*-
"""
Lendo arquivos csv

CSV - Comma separeted Values Valores separados por vírgulas

"""

from csv import reader, DictReader

# with open('lutadores.csv', encoding='UTF-8') as arquivo:
#     leitor_csv = reader(arquivo)
#     next(leitor_csv)
#     for linha in leitor_csv:
#         print(linha)

# with open('lutadores.csv', encoding='utf-8') as arquivo:
#     leitor_csv = DictReader(arquivo)
#     next(leitor_csv)
#     for linha in leitor_csv:
#         print(f"Nome:", linha['Nome'].center(20),
#               "País:", linha['País'].center(20))

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    next(leitor_csv)
    for linha in leitor_csv:
        print(f"Nome:", linha['Nome'].center(20),
              "País:", linha['País'].center(20))