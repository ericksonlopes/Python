import pandas as pd

df = pd.read_csv('dados.csv')

# imprimindo as informações do csv
print(df, '\n')

# exibe por padrão as 5 primeiras linhas
print(df.head(), '\n')

# exibe por padrão as 5 últimas linhas
print(df.tail(), '\n')

# exibe por padrão as 20 primeiras linhas
print(df.head(n=20), '\n')
