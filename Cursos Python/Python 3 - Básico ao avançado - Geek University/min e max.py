"""
Min e max
max - retorna o maior valor em um iterável
min - retorna o menor valor em um iteravel
"""
#
# # exemplo
# lista = [0, 8, 9, 41]
# print(max(lista))
#
# # ordena pela chave
# dicio = {'a': 5, 'b': 3}
# print(max(dicio))
# print(max(dicio.values()))
# # programa que receba dois valores
# v1, v2 = 3, 7
# print(max(v1, v2))  # retorna o valor maior
#
# print(max('a', 'abc', 'g'))
# print(max('b', 'z', 'g'))
# # print(max(1, 'v'))  # Valores não compatíveis

# # exemplo
# lista = [0, 8, 9, 41]
# print(min(lista))
#
# # ordena pela chave
# dicio = {'a': 5, 'b': 3}
# print(min(dicio))
# print(min(dicio.values()))
#
# # programa que receba dois valores
# v1, v2 = 3, 7
# print(min(v1, v2))  # retorna o valor maior
#
# print(min('a', 'abc', 'g'))
# print(min('b', 'z', 'g'))
# # print(max(1, 'v'))  # Valores não compatíveis
# print(min(-1, 0, 1))

# OUTROS EXEMPLOS

nomes = ['marcelo', 'adriana', 'giseli', 'pedro lemos ', 'ana', 'zarrit']

print(max(nomes))  # adriana
print(min(nomes))  # zarrit

print(max(nomes, key=lambda nome: len(nome)))  # pedro lemos
print(min(nomes, key=lambda nome: len(nome)))  # ana

musicas = [
    {'titulo': 'Jesus chorou', 'tocou': 3},
    {'titulo': 'Cana braba', 'tocou': 2},
    {'titulo': 'Giz', 'tocou': 4}
    ]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])  # exibir apenas o nome da musica
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])
