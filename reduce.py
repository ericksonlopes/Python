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


numbers = [1, 2, 3, 4, 5]
# Capture maximum value
print(reduce(lambda a, b: a if a > b else b, numbers))
print(max(numbers))
# output
# 5

# Capture minimum value
print(reduce(lambda a, b: a if a < b else b, numbers))
print(min(numbers))
# output
# 1
