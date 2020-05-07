"""
Sorted

Não confunda com sort, apesar do nome. o sort() só funciona em listas

podemos utilizar o sorted() com qualquer iterável.

sorted, ordena elementos.
"""

# numeros = {6, 1, 5, 3, 7, 8, 4, 1}
# print(numeros, 'set sem ordenação')
# print(sorted(numeros), 'set transformado em lista ordenada')
# print(numeros, 'set sem ordenação sem modificações')

# # adicionando parâmetros ao sorted
# numeros = [6, 1, 5, 3, 7, 8, 4, 1]
#
# print(sorted(numeros))  # convertendo pra set
# print(set(sorted(numeros)))
# print(sorted(numeros, reverse=True))  # invertendo ordem do maior para menor

# # podemos utilizar o sorted() para coisas mais complexas
#
# usuario = [
#     {"usarname": 'samuel', 'tweets': ['eu adoro bolo', 'eu adoro charles e lola']},
#     {"usarname": 'farlos', 'tweets': ['33', 44]},
#     {"usarname": 'nicole', 'tweets': ['eu adoro saco', 'eu adoro dinheiro']},
#     {"usarname": 'banilo', 'tweets': ['eu adoro pilulas']},
#     {"usarname": 'caukkan', 'tweets': []},
#     {"usarname": 'dilas', 'tweets': ['eu adoro skate', 'eu adoro dinheiro']},
#     {"usarname": 'ajonas', 'tweets': ['eu adoro skate', 'eu adoro dinheiro', 'coelho azul']},
#     {"usarname": 'kolas', 'tweets': []},
# ]
#
# print(usuario)
#
# # recolhe os usuarios que não tem postagem alguma
# # print({nome['usarname']: nome['tweets'] for nome in usuario if len(nome['tweets']) == 0})
#
#
# # ordenando por ordem alfabetica
# print(sorted(usuario, key=lambda usuarios: usuarios["usarname"]))
#
# # ordenando pelo número de tweets
# print(sorted(usuario, key=lambda usuarios: len(usuarios['tweets'])))

# ultimo exemplo

musicas = [
    {'titulo': 'Jesus chorou', 'tocou': 3},
    {'titulo': 'Cana braba', 'tocou': 2},
    {'titulo': 'Giz', 'tocou':4}
    ]

# ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda tocada: tocada['tocou']))
print(sorted(musicas, key=lambda tocada: tocada['tocou'], reverse=True))
