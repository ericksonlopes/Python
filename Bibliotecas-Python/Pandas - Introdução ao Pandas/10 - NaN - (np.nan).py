import pandas as pd
import numpy as np

df = pd.read_csv('dados.csv')

print(df.head(), '\n')

# O np.nan é um valor especial definido no Numpy,
# sigla para Not a Number, o pandas preenche células sem valores em um DataFrame lido com np.nan.

print('ubstituir um valor específico por um NaN.')
df2 = df.replace({"pm2": {12031.25: np.nan}})
print(df2, '\n')

print('Retorna as linhas que não contém NaN')
print(df2.dropna(), '\n')

print('Preenxher todos os valores de NaN por um outro específico')
print(df2.fillna('Não contém nada'), '\n')

print('Indica quais valores da dataframe são NaN com True')
print(df2.isna())





