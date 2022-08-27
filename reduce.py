from functools import reduce


def add(x, y):
    return x + y


numbers = [1, 1, 1]
print(reduce(add, numbers))
# Output
# 3

numbers = [1, 1, 1]
print(reduce(lambda x, y: x + y, numbers, 10))
# Output
# 13

try:
    print(reduce(lambda x, y: x + y, []))
except TypeError as error:
    print(error)
# Output
# reduce() of empty sequence with no initial value
