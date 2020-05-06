import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados.csv', encoding='utf-8')

# exibindo gráfico em barras (cima para baixo)
# df['bairro'].value_counts().plot.bar()

# barras invertidas (esquerda para direita)
# df['bairro'].value_counts().plot.barh()

# adicionando um título
df['bairro'].value_counts().plot.barh(title='Números de apartamentos')

plt.show()

