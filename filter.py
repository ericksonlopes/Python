# filter(function, iterable)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda num: num > 5, lista)))

# Output
# [6, 7, 8, 9]

nomes = ['Ana', 'Maria', 'João', 'Pedro', 'José']
print(list(filter(lambda nome: 'o' in nome, nomes)))


# Output
# ['João', 'Pedro', 'José']

def is_even(num):
    return num % 2 == 0


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(filter(is_even, lista)))

# Output
# [0, 2, 4, 6, 8]
