import pandas as pd

df = pd.read_csv('dados.csv')

# mostra os 5 primeiros e os 5 últimos
print(df, '\n')

# exibe uma lista com todos os itens encontrado nessa coluna (como um SET)
print(df['bairro'].unique(), '\n')

# Quantas ocorrências cada item aparece
print(df["bairro"].value_counts(), '\n')

# quantas ocorrências cara item aparece (em porcentagem)
print(df['bairro'].value_counts(normalize=True), '\n')

# para termos um objeto GroupBy com informações das médias agrupadas pelos valores da coluna bairro
print(df.groupby('bairro').mean(), '\n')

# para obtermos os valores da média do preço do metro quadrado em ordem crescente, por exemplo:
print(df.groupby("bairro").mean()["pm2"].sort_values())
