"""
Módulo colletions - named tuple

named tuple -> são tupla, diferenciadas, onde, especificamos um nome para a mesma e também parametros
"""
# # recap
# tupla = (1, 2, 3)
# print(tupla[1])

from collections import namedtuple

# precisamos definir o nome e parâmetro.

# forma 1 - Declaração named tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

dog = cachorro(idade=2, raca='Shitsu', nome='Rammus')
print(dog)

# acessando os dados

# forma 1
print(dog[0])   # idade
print(dog[1])   # raça
print(dog[2])   # nome

# forma 2
print(dog.idade)    # idade
print(dog.raca)     # raça
print(dog.nome)     # nome

# quantas ocorrências desse valor tem na tupla
print(dog.count('Rammus'))

# procura o índice do valor dentro da tupla
print(dog.index('Rammus'))

