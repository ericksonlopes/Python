# -*- coding: iso-8859-1 -*-
"""
Teste de memória com generators

"""


# função usando lista
def seq_fibo(maxl):
    nums = []
    a, b = 0, 1
    while len(nums) < maxl:
        nums.append(b)
        a, b = b, a + b
    return nums


# função usando generators
def fib_gen(maxl):
    a, b, contador = 0, 1, 0
    while contador < maxl:
        a, b = b, a + b
        yield a
        contador += 1


print(seq_fibo(10))
for n in fib_gen(20):
    print(n)
print(list(fib_gen(52)))
