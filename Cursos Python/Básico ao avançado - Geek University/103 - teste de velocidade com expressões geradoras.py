# -*- coding: iso-8859-1 -*-

"""
teste de velocidade com expressões geradoras

"""

import time


def nums():
    for num in range(1, 10):
        yield num


print(next(nums()))  # ...

# Expressoes geradoras
nums_ge = (num for num in range(1, 10))
print(nums_ge)

ge_inicio = time.time()
print(sum((num for num in range(50000000))))
ge_final = time.time() - ge_inicio

print(ge_final)

