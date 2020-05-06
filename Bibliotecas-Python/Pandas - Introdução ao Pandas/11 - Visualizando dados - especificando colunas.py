import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados.csv')

df.plot.scatter(x='preco', y='area')

plt.show()