def gerador():
    for i in range(5):
        yield i


g = gerador()

print(next(g))
print(next(g))
print(next(g))
