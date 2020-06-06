"""
Set comprehension
"""

numeros = {num for num in range(1, 7)}
print(numeros)

# outro exemplo
numeros = {x: x * 2 for x in range(10)}
print(numeros)


print([valor * 2 for chave, valor in numeros.items()])

# finalizar

letras = {letra for letra in 'geek University'}
print(letras)

letras = [letra for letra in 'geek university']
print(letras)
