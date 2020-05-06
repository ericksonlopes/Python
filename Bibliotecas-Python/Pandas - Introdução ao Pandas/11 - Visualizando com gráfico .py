import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados.csv', encoding='utf-8')

# Visualizando por um gráfico
df["preco"].plot.hist()
# df["preco"].plot.area()
# df["preco"].plot.pie()
# df["preco"].plot.scatter()

# Executando função iniciadora
plt.show()


