lista = ['primeiro', 2, 85, 4, 125, 5, 'ultimo']

n1, *n2 = lista
print(n1)
print(n2, '\n')

*n1, n2 = lista
print(n1)
print(n2, '\n')

n1, *n2, n3 = lista
print(n1)
print(n2)
print(n3, '\n')

n1, *_, n3 = lista
print(n1)
print(n3, '\n')