import pandas as pd

df = pd.DataFrame({'Aluno': ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                  'Faltas': [2, 3, 4, 5, 6],
                   'Prova': [8, 7, 5, 4, 9],
                   'Seminário': [4.9, 5.4, 6.3, 7.5, 9]})

# Organizando de forma intuitiva
print(df['Aluno'], '\n')

# Organiza por determinada coluna
print(df.sort_values(by='Seminário'), '\n')

# Selecionar pelo index
print(df.loc[2], '\n')

# selecionar apenas as linhas em que o valor da coluna Seminário seja acima de 8.0
print(df[df["Prova"] > 5], '\n')

# filtragem de dados
print(df[(df["Prova"] > 5) & (df['Faltas'] > 4)])
# usam operadores bitwise, ou seja, &, |, ~ ao invés de and, or, not,
