"""
Generators

em aulas anteriores estudamos sobre:
    -List comprehension
    -Dictionary comprehension
    -Set Comprehension

não vimos:
    -Tuple Comprehension... pois elas se chamam generators

"""

# # poderiamos ter feito usando Generators
# nomes = ['Ceque', 'Cucia', 'Camadeu', 'Cirineu', 'Vanessa']
#
# print(any(nome[0] == 'C' for nome in nomes))  # Generators
# print(nome[0] == 'C' for nome in nomes)  # Generators
# print(tuple(nome[0] == 'C' for nome in nomes))  # Convertendo para tupla o generators
#
# # List Comprehesion
# res = [nome[0] == 'C' for nome in nomes]
# print(type(res))
#
# # Generators
# res = (nome[0] == 'C' for nome in nomes)
# print(type(res))

# qual a utilidade de getsizeof()
# Mostra em memória a quantidade de byte usados pelo elemento em memória como elemento
# from sys import getsizeof
#
# nomes = ['Ceque', 'Cucia', 'Camadeu', 'Cirineu', 'Vanessa']
# # List Comprehesion
# res = [nome[0] == 'C' for nome in nomes]
# print(type(res), 'Gasta =', getsizeof(res))
#
#
# # Generators
# res = (nome[0] == 'C' for nome in nomes)
# print(type(res), 'Gasta =', getsizeof(res))
#
# # print(list(map(getsizeof, range(1, 100, 2)))) Aparentemente todos os números até 100 gastam a mesma quantidade de
# byte
#
# print(getsizeof(1))
# print(getsizeof(True))  # 28 - True gasta mais energia
# print(getsizeof(False))  # 24 - False gasta menos energia
# print(getsizeof(1.2))  # 24 - Ponto flutuante gasta menos
# print('Lista -', [numero for numero in range(1, 10)], 'Gasto de energia = ',
#       getsizeof([numero for numero in [1, 2, 3, 4, 5, 6, 7, 8, 9]]), 'Na memória')  # or range(1, 10)
#
# # Uma letra equivale a 50 bytes, caso seja adicionado mais letra o byte aumenta 1 por letra
# print(getsizeof('a'))
# print(getsizeof('ab'))
# print(getsizeof('abc'))
# print(getsizeof('abcd'))

# importando biblioteca
from sys import getsizeof

#  gerando uma lista de numeros com list comprehension
lista_comprehension = [x * 10 for x in range(1000)]

#  gerando uma set de numeros com list comprehension
set_comprehension = {x * 10 for x in range(1000)}

#  gerando uma dicionario de numeros com list comprehension
dictionary_comprehension = {x: x * 10 for x in range(1000)}

# Gerando uma lista de números com generators
gene_comprehension = (x * 10 for x in range(1000))

print(getsizeof(lista_comprehension), 'lista')
print(getsizeof(set_comprehension), 'set')
print(getsizeof(dictionary_comprehension), 'dictionary')
print(getsizeof(gene_comprehension), 'generators')

# invertendo string com reserved
for letra in reversed('Erickson e Renan'):
    print(letra, end='')

print('\n', ''.join(list(reversed('erickson lopes'))))  # imprimir uma lista sem espaço reversa
print('geek university'[::-1])  # podemos inverter string com slice7

# podemos utilizar o reversed para fazer um loop for reverse

for n in reversed(range(1, 10)):
    print(n)

for n in range(10, -1, -1):
    print(n)