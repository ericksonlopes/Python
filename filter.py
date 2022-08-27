# filter(function, iterable)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda num: num > 5, numbers)))

# Output
# [6, 7, 8, 9]

names = ['Ana', 'Maria', 'João', 'Pedro', 'José']
print(list(filter(lambda nome: 'o' in nome, names)))


# Output
# ['João', 'Pedro', 'José']

def is_even(num):
    return num % 2 == 0


numbers = range(10)

print(list(filter(is_even, numbers)))

# Output
# [0, 2, 4, 6, 8]
