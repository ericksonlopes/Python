import pandas as pd
import matplotlib.pyplot as plt

data = {"Laranja": [1.50, 1.20, 8.55],
        'Maça': [4.80, 2.20, 1.85],
        'Jaca': [7.99, 22.50, 12.10]}

ind = ['jan', 'fev', 'mar']

df = pd.DataFrame(data, index=ind)

print(df, '\n'*2)

# Dados estatisticos
print(df.describe(), '\n'*2)

# Dados estatisticos de um item
print(df['Laranja'].describe(), '\n'*2)

# Dados referentes a um indice
print(df.loc['fev'].describe())

# plotando gráfico de pizza
df.plot(kind='pie', y='Laranja')
plt.show()

