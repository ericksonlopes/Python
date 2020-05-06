import pandas as pd

df = pd.DataFrame({'Aluno': ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                   'Faltas': [3, 4, 2, 1, 4],
                   'Prova': [2, 7, 5, 10, 6],
                   'seminario': [8.5, 7.5, 9.0, 7.5, 8.0]})

df.to_csv('Alunos_histórico.csv', index=False)

print(pd.read_csv('Alunos_histórico.csv'))
