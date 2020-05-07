"""
Dictionary comprehension

pense o seguinte
se quisermos criar :
lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = {'a': 1, 'b' : 2, 'c': 3}

# sintaxe
{chave:valor}
{chave:valor for valor in iterável}
[valor for valor in iterável]
"""

# # exemplos
#
# numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# quadrado = {chave: valor for chave, valor in numeros.items()}
# print(quadrado)

# numero = [1, 2, 3, 4, 5]
# print({valor: 'par' if valor % 2 == 0 else 'impar' for valor in numero})

# chaves = 'abcde'
# valores = [1, 2, 3, 4, 5]
#
# mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
#
# print(mistura)

# exemplo com lógica condicional

numeros = [1, 2, 3, 4, 5]
print({numero: 'Par' if numero % 2 == 0 else 'Ímpar' for numero in numeros})