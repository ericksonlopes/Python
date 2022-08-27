# map(function, iterables)

frutas = ('apple', 'banana', 'cherry')

print(list(map(len, frutas)))
print(list(map(lambda fruta: len(fruta), frutas)))


# Output
# [5, 6, 6]


def remove_space(string):
    return string.replace(' ', '')


music = ['Unknown: Howie Weinberg',
         'Vocals: Damon Albarn',
         'Unknown: Danger Mouse']

print(list(map(remove_space, music)))
print(list(map(lambda item: remove_space(item), music)))


# Output
# ['Unknown:HowieWeinberg', 'Vocals:DamonAlbarn', 'Unknown:DangerMouse']

def soma(x, y):
    return x + y


list_1 = [1, 2, 3]
list_2 = [1, 2, 3]

print(list(map(soma, list_1, list_2)))
print(list(map(sum, zip(list_1, list_2))))
print(list(map(lambda x, y: x + y, list_1, list_2)))
print(list(map(lambda x: x[0] + x[1], zip(list_1, list_2))))
# Output
# [2, 4, 6]
