"""
Dicionarios

OBS: Em algumas linguagens de programação, os dicionarios Python são conhecidos por mapas

Dicionarios são coleções do tipo chave/valor

Dicionarios são representados por chaves

OBS: Sobre dicionarios
    -Chave e valor são separados por dois pontos 'chave:valor',
    -Tanto chave quanto valor podem ser de qualquer tipo de dado:
    -podemos misturar tipos de dados:

    O tipo None é sempre considerado False
"""

# # Criação de dicionarios
#
# # forma 1 (Mais comum)
# # Explica melhor o tipo de dado
# paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
#
# print(paises)
# print(type(paises))
#
# # forma 2 (menos comum)
#
# paises = dict(br='Brasil', eua='Estados unidos', py='Paraguai')

# # Acessando elementos
# paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
#
# # Forma 1 - acessando via chave, da mesma forma que lista/tupla
#
# print(paises['br'])
# print(paises['py'])
#
# # Forma 2 - acessando via get - Recomendada
# print(paises.get('br'))
# print(paises.get('ru'))  # Retorna None, pelo motivo de não existir a chave 'ru'

# paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado keyError
# pais = paises.get('ru', 'Não encontrado')
# if pais:  # Se russia for None
#     print(f'encontrei o pais {pais}')
# else:
#     print('Não encontrei')

# # Podemos definir um valor padrao caso nao encontremos o objeto com a chave informada
# paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# pais = paises.get('py', 'Não encontrado')
# print(f'Encontrei o país {pais}')

# paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
#
# # Podemos verificar se uma chave se encontra em um dicionario
# print('br' in paises)
# print('eua' in paises)
# print('r' in paises)
#
# if 'br' in paises:
#     russia = paises['br']
#     print(russia)

# # Podemos itulizar qualquer tipo de dado inclusive(int, float, string, boolean),(listas, tupla dicionario)
# # como chaves de dicionario.
#
# # Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionário pois as mesmas são
# # imutaveis
# localidades = {
#     (35.8422, 79.2644): 'Escritório em Tókio',
#     (65.1122, 89.3554): 'Escritório em Nova York',
#     (75.8855, 29.2884): 'Escritório em São Paulo',
# }
#
# print(localidades)
# print(type)

# # Adicionar elementos em um dicionário
# receita = {'jan': 100, 'fev': 120, 'mar': 300}
# print(receita)
#
# # forma 1 - Mais comum
# receita['abr'] = 350
# print(receita)
# # forma 2
#
# novo_dado = {'mai': 500}
# receita.update(novo_dado)   # receita.update({'mai': 500})
# print(receita)
#
# # Atualizando dados em um dicionario
#
# # forma 1
# receita['mai'] = 550
# print(receita)
#
# receita.update({'mai': 600})
# print(receita)
#
# # forma 1: para adicionar novos elementos ou atualizar dados em um dicionario é a mesma.
# # forma 2: Em dicionarios, NÃO podemos ter chaves repetidas.

# # Remover dados de um dicionario
# receita = {'jan': 100, 'fev': 120, 'mar': 300}
# # forma 1 mais comum
# print(receita)
# ret = receita.pop('mar')
# print(receita)
# print(ret)
# # Precisamos sempre informar a chave, caso nao encontre retorna erro
# # Ao remover um objeto, o valor deste objeto é sempre retornado pelo .pop()
#
# # forma 2
# del receita['fev']
#
# print(receita)

# # Imagine que você tem um comercio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.
# """
# Carinnho de compras:
#     produto 1:
#         nome:
#         quantidade:
#         preço:
#     produto 2:
#         nome;
#         quantidade;
#         preço;
# """
# # - 1 Utilizar com Lista
#
# carinho = []
#
# produto1 = ['Playstation 4', 1, 2300.000]
# produto2 = ['God of war 4', 1, 150.00]
#
# carinho.append(produto1)
# carinho.append(produto2)
#
# print(carinho)
#
# # Teriamos que saber , qual é o indice de cada informação no produto.
# # x = carinho[1]
# # print(x[1])
#
# # 2 - Poderiamos utilizar uma tupla para isso
# produto1 = ['Playstation 4', 1, 2300.000]
# produto2 = ['God of war 4', 1, 150.00]
#
# carinho = (produto1, produto2)
#
# print(carinho)
# # Teriamos que saber , qual é o indice de cada informação no produto.
# # x = carinho[1]
# # print(x[0])
#
# # 3 - Poderiamos utilizar dicionarios - Forma que evita varios problemas
# carinho = []
#
# produto1 = {'nome': 'Playstation 4', 'Quantidade': 1, 'Preço': 2300.00}
# produto2 = {'nome': 'god of war', 'Quantidade': 1, 'Preço': 150.00}
#
# carinho.append(produto1)
# carinho.append(produto2)
#
# print(carinho)
#
# # Desta forma, adicionamos ou removemos produtos no carrinho e em casa produto
# # Podemos ter a certeza sobre cada informação

# # Métodos de dicionários.
# d = dict(a=1, b=2, c=3)
#
# print(d)
# print(type(d))
# print('\n')
# # Copiando um dicionario para outro
# """
# # Forma 1 - Deep Copy
#
# novo = d.copy()
#
# print(novo)
#
# novo['d'] = 4
# novo['e'] = 5
# print(novo, 'novo')
# print(d, 'd')
# """
# # Forma 2 - Shallow copy
# novo = d
# print(novo)
#
# novo['d'] = 4
# print(d)
# print(novo)
#
# print('\n')
# # Limpar o dicionario (Zerar Dados)
# d.clear()
# print(d)

# Forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# o método fromkays recebe dois parametros: um iteráveç e um valor.
# ele vai ferar para cada valor do iteravel uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('abcc', 'valor')
# uma string em python pode ser iterável, nessa caso ele pegou caractere por caractere, porem nao pode repetirse
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)