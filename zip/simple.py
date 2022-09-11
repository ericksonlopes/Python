ids = (1, 2, 3)
names = ("Jenny", "Christy", "Monica")

result = list(zip(ids, names))

print(result)
# [(1, 'Jenny'), (2, 'Christy'), (3, 'Monica')]

# todo: Unzip
print(list(zip(*result)))
# [(1, 2, 3), ('Jenny', 'Christy', 'Monica')]

# todo: to dict
print(dict(zip(ids, names)))
# {1: 'Jenny', 2: 'Christy', 3: 'Monica'}

# todo: check if the length of the two lists are the same
print(list(zip(range(5), range(100), strict=True)))
