"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória.
mas fim de maneira especificada.

Forma geais:

range(valor_deparada)
OBS: Valor_de_parada não inclusive(inicio padrão 0, e passo 1 em 1)

rang(10) - irá até o 9 pois a sequencia começa em 0
 4 - 5 - 6
 0 - 1 - 2
"""

# Exemplo Forma 1 - Apenas 1 valor
# range(valor_de_parada) - apartir do 0
for num in range(11):
    resul = num * 4
    print(resul, end='- ')


print('\n')
# Exemplo Forma 2
# range(valor_de_inicio, valor_de_parada) - passo de 1 em 1
for num in range(4, 11):
    print(num, end='- ')


print('\n')
# Exemplo forma 3
# range(valor_de_inicio, valor_de_parada, passo) passo pelo usuario
for num in range(5, 50, 5):
    print(num, end='- ')


print('\n')
# Exemplo forma 4(inversa)
# range(valor_de_inicio, valor_de_parada, passo)
for num in range(10, -1, -1):  # decrementar
    print(num, end=', ')


print('\n')
# Imprimir lista usando range
# Convertendo range pra uma lista
lista = list(range(10, -10, -1))
print(lista, end=' ')
