# map(function, iterables)

# todo: count the number of characters in a string
fruits = ('apple', 'banana', 'cherry')

print(list(map(len, fruits)))
print(list(map(lambda fruit: len(fruit), fruits)))


# Output
# [5, 6, 6]

# todo: create list of strings without spaces
def remove_space(string):
    return string.replace(' ', '')


music = ['Unknown: Howie Weinberg',
         'Vocals: Damon Albarn',
         'Unknown: Danger Mouse']

print(list(map(remove_space, music)))
print(list(map(lambda item: remove_space(item), music)))


# Output
# ['Unknown:HowieWeinberg', 'Vocals:DamonAlbarn', 'Unknown:DangerMouse']

# todo: create list of sum of two lists
def add(x, y):
    return x + y


list_1 = [1, 2, 3]
list_2 = [1, 2, 3]

print(list(map(add, list_1, list_2)))
print(list(map(sum, zip(list_1, list_2))))
print(list(map(lambda x, y: x + y, list_1, list_2)))
print(list(map(lambda x: x[0] + x[1], zip(list_1, list_2))))
# Output
# [2, 4, 6]
