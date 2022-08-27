from functools import reduce


# todo: create list of sum of two lists
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

# todo: error if list is empty

try:
    print(reduce(lambda x, y: x + y, []))
except TypeError as error:
    print(error)
# Output
# reduce() of empty sequence with no initial value


numbers = [1, 2, 3, 4, 5]
# todo: Capture maximum value
print(reduce(lambda a, b: a if a > b else b, numbers))
print(max(numbers))
# output
# 5

# todo: Capture minimum value
print(reduce(lambda a, b: a if a < b else b, numbers))
print(min(numbers))
# output
# 1
