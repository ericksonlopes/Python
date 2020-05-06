import pandas as pd

# Criando Series de dados com index
notas = pd.Series([1, 3, 3, 3, 3, 9, 10], [["Wilfred", "Abbie", "Harry", "Julia", "Carrie", "Carlos", 'Welliton']])

# função que pega a média dos valores
print("média: ", notas.mean())
# função que pega o desvio padrão
print("Desvio padrão", notas.std(), '\n')

# Geralmente para resumir brevemente as estatísticas dos dados se usa o .describe()
print(notas.describe())
