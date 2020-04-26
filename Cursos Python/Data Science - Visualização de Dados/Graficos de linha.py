# Visualização de dados com python

import matplotlib.pyplot as plt 

x = [num for num in range(1, 11)]
y = [1, 2, 4, 8, 7, 5, 1, 2, 4, 8]

titulo = ' Gráfico de linhas'
eixo_x = "Eixo X"
eixo_y = 'Eixo Y'

# Legendas
plt.title(titulo)  # titulo
plt.xlabel(eixo_x)  # titulo eixo x
plt.ylabel(eixo_y)  # titulo eixo y

# Plota os valores dentro do gráfico  
plt.plot(x, y)
plt.show()
