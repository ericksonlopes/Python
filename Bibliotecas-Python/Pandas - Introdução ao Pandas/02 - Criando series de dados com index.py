import pandas as pd

# Criando Series de dados com index
notas = pd.Series([1, 2, 4, 8, 7, 5], [["Wilfred", "Abbie", "Harry", "Julia", "Carrie", "Carlos"]])

# imprimindo os index
print(notas.index)
# imprimindo os valores
print(notas.values, "\n")

# imprimindo o objeto com os valores de modo organizado pelo pandas
print(notas, "\n")

# imprimindo o index definido
print(notas['Julia'])


