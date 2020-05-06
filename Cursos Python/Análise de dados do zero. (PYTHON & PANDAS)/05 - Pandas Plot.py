import pandas as pd
import matplotlib.pyplot as plt

quantidade = [5, 3, 4]
ind = ['Laranja', 'Abacate', "Maça"]

df = pd.Series(quantidade, index=ind)

print(df, '\n'*2)

# barra
# df.plot(kind='bar', title='Quantidade')

# pizza
# df.plot(kind='pie', title='Quantidade')

# linha
df.plot(kind='line')

plt.show()