import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados.csv')

# # percorre todos os tipos de estilos e exibe na tela
# for item in plt.style.available:
#     print(item)

#     # estilizando o gráfico
#     plt.style.use(item)

#     # instânciando os valores
#     df.plot.scatter(x='preco', y='area')

#     plt.show()

# s = tamanho do Circulo
df.plot.scatter(x='preco', y='area', s=.5)
# df.plot(x='preco', y='area')


plt.show()

