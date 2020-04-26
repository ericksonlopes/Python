"""
Listas aninhadas
- alumas linguagens de programação possuem  uma estrutura de dados chamada arrays:
    - unidimensionais arrays/vetores
    - multidimencionais matrizes

em python temos listas.

"""

# # exemplos
#
# listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # matriz 3 x 3
#
# print(listas)
# print(type(listas))
#
# # acessar os dados
# print(listas[1][2])  # faz acesso ao número 6
#
# # iterando com loops em uma linha aninhada
# for lista in listas:
#     for numero in lista:
#         print(f'[{numero}]', end='')
#     print()
#
# # usando list comprehension
# [[print(f'[{numero}]', end='') for numero in lista]for lista in listas]

# Outros exemplos

# gerando um tabuleiro/matriz 3 x 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)]for valor in range(1, 4)]
print(velha)

# gerando valores iniciais
print([['*' for i in range(1, 4)]for j in range(1, 4)])
