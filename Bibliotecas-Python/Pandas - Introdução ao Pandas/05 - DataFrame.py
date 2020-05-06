import pandas as pd

df = pd.DataFrame({'Aluno': ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                  'Faltas': [2, 3, 4, 5, 6],
                   'Prova': [8, 7, 5, 4, 9],
                   'Seminário': [4.9, 5.4, 6.3, 7.5, 9]})

# exibe de forma organizada
print(df, '\n')

# traz uma descrição das colunas
print(df.describe(), '\n')

# exibe os tipos de dados
print(df.dtypes, '\n')


