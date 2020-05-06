import pandas as pd

coluna = ['Frutas']

itens = ['Laranja', 'maça', 'abacate']

df = pd.DataFrame(itens, columns=coluna)

print(df, '\n'*2)

coluna = ['Frutas', 'Preco']

itens = [['Laranja', 10], ['Maça', 10], ['Abacate', 15]]

df = pd.DataFrame(itens, columns=coluna, dtype=float)

print(df) 