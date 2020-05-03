import matplotlib.pyplot as plt

x_i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_i = [1, 3, 5, 7, 9, 2, 4, 8, 1, 3, 5]

x_p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_p = [0, 2, 4, 8, 1, 3, 5, 7, 9, 2, 4]

titulo = 'Scartterplot: Gráfico de pontos'
eixo_x = "Eixo X"
eixo_y = 'Eixo Y'

# Legendas
plt.title(titulo)  # titulo
plt.xlabel(eixo_x)  # titulo eixo x
plt.ylabel(eixo_y)  # titulo eixo y

# cria pontos
plt.scatter(x_i, y_i, edgecolors='red', label='1, 3, 5, 7, 9, 2, 4')
# cria uma linha que liga os pontos
plt.plot(x_i, y_i)

# cria pontos
plt.scatter(x_p, y_p, edgecolors='red', label='0, 2, 4, 8, 1, 3, 5')
# cria uma linha que liga os pontos
plt.plot(x_p, y_p)

# adiciona a legenda da label
plt.legend()

plt.show()
