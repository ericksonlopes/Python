"""
Reversed

OBS: não confundir com reverse() que só funciona em listas
a função reversed funciona com qualquer iteravel

"""

tupla = (1, 5, 6, 9, 7)
res = reversed(tupla)  # cria um objeto que pode ser convertido para qualquer iteravel

print(res)
print(type(res))
print(tuple(res))

print(list(reversed(tupla)))
