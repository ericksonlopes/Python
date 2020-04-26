"""
Mapas - São conhecidos em python como dicionrios

Dicionarios em python são representados por chaves {}
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Iterar spbre dicionarios (laços)
# for chave in receita:   # chave
#     print(chave)
#
# for chave in receita:   # valor
#     print(receita[chave])
#
# for chave in receita:  # Os dois elementos
#     print(f'{chave} recebi R${receita[chave]}')

# # Acessando as chaves
# print(receita.keys())   # busca chaves
#
# for chave in receita.keys():
#     print(receita[chave])

# # acessando os valores
# print(receita.values())
#
# for valor in receita.values():
#     print(valor)

# # Desempacotamento de dicionario
# for chave, valor in receita.items():
#     print(f'chave={chave} e valor={valor}')

# soma, maximo minimo tamanho

# * Se os valores dorem todos inteiros ou reais

print(sum(receita.values()))  # soma de todos os valores
print(max(receita.values()))  # valor maximo
print(min(receita.values()))  # valor minimo
print(len(receita))  # quantidade de elemento
