import pandas as pd
import numpy as np

# Criando Series de dados com index
notas = pd.Series([1, 3, 3, 3, 3, 9, 10], [["Wilfred", "Abbie", "Harry", "Julia", "Carrie", "Carlos", 'Welliton']])
print(np.log(notas))

# podemos aplicar expressões matemáticas e funções do numpy
print(notas*2)