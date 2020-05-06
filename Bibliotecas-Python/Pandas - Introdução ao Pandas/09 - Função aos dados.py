import pandas as pd


def truncar(bairro):
    return bairro[:3]


df = pd.read_csv('dados.csv')

# Com apply chama uma função par aplicar aos dados
print(df['bairro'].apply(truncar))

# com funções lambda
print(df['bairro'].apply(lambda x: x[:3]))
