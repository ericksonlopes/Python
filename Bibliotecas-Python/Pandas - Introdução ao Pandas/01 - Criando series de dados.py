import pandas as pd

# Criando Series de dados
notas = pd.Series([2, 7, 4, 8, 10, 6])

# exibe uma estrutura com os dados e indices
print(notas, '\n')

# exibir apenas notas
print(notas.values, '\n')

# exibir os indices
print(notas.index, '\n')

# retonra o tipo do objeto, valores, tamanho, tipo de dado
print(notas.array)

