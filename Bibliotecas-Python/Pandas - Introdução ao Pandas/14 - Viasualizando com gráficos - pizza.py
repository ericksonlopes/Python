import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados.csv')

df["quartos"].value_counts().plot.pie()

plt.show()
