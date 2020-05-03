# Visualização de dados com python

import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 4, 8, 7, 5]

# Adicionar titulos 
plt.title('Meu primeiro grádivo em python')

# Contruir titulos em cada eixo
# X
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Plota os valores dentro do gráfico  
plt.plot(x, y)
plt.show()