"""
Any e All

all() - Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

any() -  Retorna True se qualquer elemento do iterável for verdadeiro, se estiver vazio retonar False.
"""

# # Exemplo all()
#
# print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros ? Não pois o 0 é False
#
# print(all([2, 3, 5, 4, 5]))  # True, Pois todos os elementos são positivos
#
# print(all([]))  # True, se o iterável dor vazio
#
# nomes = ['Ceque', 'Cucia', 'Camadeu', 'Cirineu']
#
# print(all([nome[0] == 'C' for nome in nomes]))  # Verifica se todos os nomes começam com 'C'
# print(all([nome[-1] == 'e' for nome in nomes]))  # Verifica se todos terminam com 'e'
# print([nome[-1] == 'e' for nome in nomes])  # verifica cada um termina com 'e'
#
# # OBS: Um iterável vazio convertido pra boolean é False, mas o all entende como True
# print(all([letra for letra in 'aiod' if letra in 'ifo']))
#
# print(all([num for num in [2, 3, 4, 5, 6] if num % 2 == 0]))
# print([num for num in [2, 3, 4, 5, 6] if num % 2 == 0])

# Exemplo any

print(any([0, 1, 0, 0]))  # True, pois 0 = false mas 1 é True
print(any([]))  # False - Vazio
print(any([0, 0, 0]))  # False -  todos os valores são False
print(any([[], False, '']))  # False, elementos vazios=false, e false que é false, todos false
print(any([[], False, '', 1])) # True, por conta do 1=True

nomes = ['Ceque', 'Cucia', 'Camadeu', 'Cirineu', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes])) # True, tem quatro nomes com a letra 'C'

print(any([num for num in [2, 3, 4, 5, 6] if num % 2 == 0]))  # True, 2, 4, 6 divisiveis por 2
