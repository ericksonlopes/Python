import pandas as pd
# import os
#
# for item in os.listdir('../Análise de dados do zero. (PYTHON & PANDAS)'):
#     print(item)

df = pd.read_csv('2020-02-gasolina-etanol.csv', encoding='utf-16', sep=',')

# sem duplicidade
siglas = df['Estado - Sigla'].unique()
print(siglas, len(siglas))

print(df.groupby(['Valor de Venda']))