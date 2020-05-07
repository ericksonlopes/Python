"""
Reduce

OBS: A partir do python3+ a função reduce() não é mais uma função integrada (built - in)
agora temos que importar a utilizar esta função do módulo 'functools'

guido van Rossum: utilize a função reduce() se você realmente precisa dela . em todo caso,
99% das vezes um loop for é mais legível.

Para entender o reduce()

a função reduce recebe dois parâmtros: a função e o iterável.

reduce(funcao, dados) - funcao que recebe dois parâmetros

"""

from functools import reduce

dados = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# utilizando

res = reduce(lambda x, y: x + y, dados)
print(res)

# Utilizando umk loop normal
res = 0
for n in dados:
    res = res + n

print(res)
