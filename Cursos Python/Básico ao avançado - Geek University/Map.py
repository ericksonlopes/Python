"""
Map

com map fazemos mapeamento de valores para função.
"""

# import math
#
#
# def are(r):
#     """Calcula a area de de um círculo 'r'"""
#     return math.pi * (r ** 2)
#
#
# print(are(2))
# print(are(5.3))
#
# raios = [2, 5, 9.8, 7, 2, 9]
#
# # forma comum
# areas = []
# for r in raios:
#     areas.append(are(r))
# print(areas)
#
# # forma 2 - map
#
# # map é uma função que recebe dois parâmetros: função, iterável. e retorna um map object
#
# areas = map(are, raios)
# print(type(areas))
# print(list(areas))  # convertendo para lista
#
# # Forma 3 - lambda
#
# print(list(map(lambda r: math.pi * (r ** 2), raios)))
#
# # após utilizar a função map depois da primeira utilização do resultado ele zerar

# mais um exemplo

cidades = [('berlin', 29), ('Cairo', 39), ('são paulo', 32), ('itapecerica', 27)]
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))
