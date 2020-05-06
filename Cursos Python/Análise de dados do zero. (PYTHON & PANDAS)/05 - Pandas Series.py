import pandas as pd

quantidade = [5, 3, 4]
ind = ['Laranja', 'Abacate', "Maça"]

df = pd.Series(quantidade, index=ind)

print(df, '\n'*2)

# Exibir valor de um index
print('preço do Abacate:', df['Abacate'], '\n'*2)

# operação matematica com o resultado
print('preço da Maça ->x2',
      df['Laranja'],
      df['Laranja']*2,
      '\n'*2)

# para encontrar a média dos valores
print('Média dos valores: ', df.mean(), '\n'*2)

# para encontrar o maior valor
print('Maior dos valores: ', df.max(), '\n'*2)

# para encontrar o menor valor
print('Menor dos valores: ', df.min(), '\n'*2)

# para encontrar o desvio padrão
print('Menor dos valores: ', df.std(), '\n'*2)

# para encontrar o soma dos valores
print('Menor dos valores: ', df.sum(), '\n'*2)



