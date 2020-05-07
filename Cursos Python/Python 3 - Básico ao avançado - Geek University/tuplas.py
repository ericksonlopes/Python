"""
Tuplas(tuple)

tuplas são bastante parecidas com listas.

existem basicamente duas diferenças básicas:

1 - as tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela são muda. Toda
operação em uma tupla gera uma nova tupla
"""

# # CUIDADO 1: As tuplas são representadas por (), mas veja:
#
# tupla1 = (1, 2, 3, 4, 5, 6)
#
# print(type(tupla1))
# print(tupla1)
#
# tupla2 = 1, 2, 3, 4, 5, 6
# print(tupla2)
# print(type(tupla2))
#
# # CUIDADO 2: Tuplas com 1 elemento
#
# tupla3 = (4)  # isso não é uma tupla
# print(tupla3)
# print(type(tupla3))
#
# tupla4 = (4,)  # isso é uma tupla!
# print(tupla4)
# print(type(tupla4))
#
# tupla5 = 4,  # isso é uma tupla!
# print(tupla5)
# print(type(tupla5))
#
# Tuplas são definidas pela vírgula e nao pelo parenteses
#
# podemos concluir que tuplas são definidas pelo virgula e nao pelo uso do parentese
# (4) Não é tupla
# (4,) é tupla
# 4, é tupla

# # Podemos criar uma tupla dinamicamente com range(início, fim, passo)
# tupla = tuple(range(11))
# print(tupla)
# print(type(tupla))

# # Desempacotamento de tupla
#
# tupla = ('Geek University', 'Programação em python: Essencial')
#
# escola, curso = tupla
#
# print(escola)
# print(curso)
#
# # OBS: Gera erro se colocarmos um número diferente de elementos para desempacotar

# # Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis.
#
# # Soma*, Valor maximo, valor minimo e tamanho
# # Se os valores forem todos inteiros ou reais
# tupla = (1, 2, 3, 4, 5, 6)
# print(sum(tupla))
# print(max(tupla))
# print(min(tupla))
# print(len(tupla))

# # Concatenação de tuplas(juntar)
#
# tuple1 = 1, 2, 3
# print(tuple1)
# tuple2 = 4, 5, 6
# print(tuple2)
#
# print(tuple1 + tuple2)  # concatenando
# print(tuple2 + tuple1)
#
# tuple3 = tuple1 + tuple2  # Criando nova tupla
# print(type(tuple3))
#
# tuple1 = tuple1 + tuple2  # sobreescrevendo o valor dela, mas podemos sobrescrever seus valores

# # Verificar se determinado elemento esa contido na tupla
# tupla = 1, 2, 3
# print(3 in tupla)

# # iterano sobre uma tupla
# tupla = 1, 2, 3
# for n in tupla:
#     print(n)
#
# for indice, valor in enumerate(tupla):
#     print(indice, valor)

# # contando elementos dentro de uma tupla
# #
# # tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
# # print(tupla.count('c'))
# #
# # escola = tuple('Geek university')
# # print(escola)
# # print(escola.count('e'))

# # Dicas na utilização de tuplas
#
# # Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
#
# # exemplo 1
#
# meses = ('Janeiro', 'fevereiro', 'Março', 'Abril', 'Junho', 'Julho', 'agosto')
#
# # O acesso a elementos de uma tupla é semelhante a de uma lista
# print(meses[5:])
# print(meses[-1])
#
# # iterar com while
# i = 0
# while i < len(meses):
#     print(meses[i])
#     i = i + 1

# meses = ('Janeiro', 'fevereiro', 'Março', 'Abril', 'Junho', 'Julho', 'agosto')
#
# # Verificamos em qual indice um elemento esta na tupla
# print(meses.index('Junho'))
#
# # OBS: Caso o elemento não exista, será gerado erro ValueError.

# meses = ('Janeiro', 'fevereiro', 'Março', 'Abril', 'Junho', 'Julho', 'agosto')
# # slicing
# # Tupla[Inicio: fim: passo]
# print(meses[2:])

# Por quê utilizar tuplas?
# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro.

# * Isso porque trabalhar com elementos imutáveis traz segurança para o código

# Copiando uma tupla para outra
tupla = 1, 2, 3
print(tupla)

tuplaNova = tupla  # Na tupla não temos problema de shallow Copy

print(tuplaNova)
print(tupla)

outra = (3, 4, 5)

tuplaNova = tupla + outra

print(tuplaNova)
print(tupla)


