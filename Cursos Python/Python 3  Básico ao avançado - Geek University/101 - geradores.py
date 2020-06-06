# -*- coding: iso-8859-1 -*-
"""
geradores

 - geradores são iterators
OBS: nem todos iterator é um generator

"""


# exemplo de Generator Function:
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


gen = conta_ate(20)
print(next(gen))
print(next(gen))
print(next(gen))

for num in gen:
    print(num)
