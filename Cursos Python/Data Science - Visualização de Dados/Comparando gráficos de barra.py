import matplotlib.pyplot as plt

x1 = [2, 4, 6, 8, 10]
y1 = [7, 3, 5, 7, 9]

x2 = [1, 3, 5, 7, 9]
y2 = [5, 1, 3, 7, 4]

titulo = 'Gráfico de barras 2'
eixo_x = "Eixo X"
eixo_y = 'Eixo Y'

# Legendas
plt.title(titulo)  # titulo
plt.xlabel(eixo_x)  # titulo eixo x
plt.ylabel(eixo_y)  # titulo eixo y

# Plota os valores dentro do gráfico
plt.bar(x1, y1, label='Grupo 1')
plt.bar(x2, y2, label='Grupo 2')

plt.legend()
plt.show()
