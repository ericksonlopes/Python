"""
List comprehension

"""

# Exemplos

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# Refatorar
# qualquer número par por modulo de 2 é 0 e 0 em python é false e not False = True
print([numero for numero in numeros if not numero % 2])
print([numero for numero in numeros if numero % 2])

# exemplo 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

