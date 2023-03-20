# todo: Sum with lambda
sum1 = lambda x, y: x + y

print(sum1(1, 2))
# Output
# 3


# todo: compare values
# if x > y: result = x or y
compare = (lambda x, y: x if x > y else y)
print(compare(2, 9))
# Output
# 9

# todo: Surrounding the function and its arguments with parentheses:
print((lambda x, y: x + y)(1, 2))

soma = (lambda x, y: x + y)
print(soma(1, 2))
# Output
# 3

person = {'name': 'Ana', 'age': 23}
print((lambda x: f"My name is {x['name']}, and I am {x['age']} years old")(person))
# Output
# My name is Ana, and I am 23 years old
