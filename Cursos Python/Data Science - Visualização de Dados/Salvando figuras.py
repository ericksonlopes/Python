import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 4, 5, 7, 5]

titulo = ' Gráfico de barras'
eixo_x = "Eixo X"
eixo_y = 'Eixo Y'
tamanho_scatter = [num * 50 for num in y]

# Legendas
plt.title(titulo)  # titulo
plt.xlabel(eixo_x)  # titulo eixo x
plt.ylabel(eixo_y)  # titulo eixo y

plt.scatter(x, y, marker='h', color='k', s=tamanho_scatter, label='1, 2, 4, 5, 7, 5')

plt.plot(x, y, color='k', linestyle='--')

# salvar figuras
plt.savefig('Figura_salva.png')
