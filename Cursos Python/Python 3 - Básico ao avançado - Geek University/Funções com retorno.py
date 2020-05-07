"""
Funções com retorno

"""

# # exemplo de retorno com pop na lista
# num = [1, 2, 3]
# print(num)
# x = num.pop()
# print(x)
# print(num)

# # em python, quando a função não retorna nenhum valor, o retorno é None
#
#
# def quadrado_de_7():
#     print(7 * 7)
#
# ret = quadrado_de_7()
# print(ret)  # None

# def quadrado_de_n(n):
#     print(f'O valor ao quadrado de {n} é {n * n}')
#
#
# x = int(input('Valor ao quadrado de : '))
#
# quadrado_de_n(x)

# vamos refatorar uma função para que ela retorne um valor
# OBS Funções em python que retornam valores, devem retornar estes valores com a
# palavra reservada return


# def quadrado_de_7():
#     return 7 * 7  # o resultado elemento vai ser retornado na função
#
#
# # Não precisamos necessariamente criar uma variável para receber valor
# # podemos passar a execução da função para outras funções.
# retorno = quadrado_de_7()  # Recebe o retorno da função
#
# print(f'O retorno é {retorno}')
# print(f'O retorno é {quadrado_de_7()}')
#
#
# def diz_oi():
#     return 'oi'
#
#
# diz_oi()  # Não acontece nada
# x = diz_oi()
# print('\n', diz_oi(), x)

# sobre: return
# 1 - ela finaliza a função, ou seja , ela sai da execução da função;
# 2 - podemoster, diferentes return;
# 3 - podemos em uma função retornar qualquer itpo de dado
#
# # exemplo 1
#
#
# def diz_ai():
#     return 'dd'
#     # print('esse print nunca sera executado, pelo motivo de estar depois do return')
#
#
# # exemplo 2
#
#
# def nova_funcao():
#     variavel = True
#     if variavel:
#         return 4
#     elif variavel is None:
#         return 3.2
#     return 'b'
#
#
# print(nova_funcao())
#
# # Exemplo 3
#
#
# def outra_funcao():
#     return 2, 3, 4, 5
#
#
# # desempacotando
# n1, n2, n3, n4 = outra_funcao()
#
# # dentro de uma lista
# lista = []
# for x in outra_funcao():
#     lista.append(x)
# print(lista)

# # Criar uma função para jogar a moeda
# from random import random
#
#
# def joga_moeda():
#
#     if random() > 0.5:
#         return 'cara'
#     return 'Coroa'
#
#
# print(joga_moeda())

# Codificação desnecessária
from random import random


def eh_impar():
    numero = random()
    if numero % 2 != 0:
        return True, numero
    return False


print(eh_impar())
