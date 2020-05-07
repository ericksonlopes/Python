"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia á Teoria dos conjuntos
da matemática

- aqui no python, os conjuntos são chamados de Sets.

Dito isso, da mesma dorma que na matemática:
- Sets (conjuntos) não possuem valores duplicados:
- Sets (conjuntos) não possuem valores ordenados:
- elementos não são acessados via índice, ou seja, conjuntos não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. quando não precisamos se preocupa
com chaves valores e itens duplicados.

Os conjuntos Sets São referenciados em python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionarios)
    - Um dicionario tem chave/valor;
    - Um conjunto tem valor;
"""

# # Definindo um conjunto
#
# # forma 1
#
# s = set({1, 2, 3, 4, 5, 6, 5, 3, 4})
#
# # Obs: ao criar um conjunto, caso seja adicionado um valor ja existente, o mesmo
# # será ignorado sem gerar error e não fara parte do conjunto
# print(s)
# print(type(s))
#
# # forma 2 - mais comum
# s = {1, 2, 3, 4, 5, 5}
# print(s)
# print(type(s))
#
# # Podemos verificar se determinado elemento esta contido no conjunto
#
# if 3 in s:
#     print('Tem o 3')
# else:
#     print('Não tem o 3')

# # converter string para dentro do conjunto
# s = set('erickson')
# print(s)
#
# # convertendo lista para conjunto
# lista = [1, 2, 3, 4, 5, 5]
# print(set(lista))
#
# # convertendo tupla para conjunto
# tupla = (1, 2, 3, 5, 4, 4, 5)
# print(set(tupla))

# importante lembrar que alem de nao termos valores duplicados, não temos ordem


# dados = 99, 4, 54, 2, 1, 5, 2, 5
#
# lista = list(dados)
# tupla = tuple(dados)
# dicionario = {}.fromkeys(dados, 'dict')
# s = set(dados)
#
# print(lista, '-', len(lista), 'elementos')  # aceitam valores duplicados
# print(tupla, '-', len(tupla), 'elementos')  # Tuplas aceitam valores duplicados
# print(s, '-', len(s), 'elementos')  # não repete valores
# print(dicionario, '-', len(dicionario), 'elementos')  # Não repete chaves
#
# # Assim como todo outro conjunto Puthon podemos colocar todos os tipos de dados misturados em Sets
# s = {1, 'b', 1.40, 55.22, True}
# print(s)
# print(type(s))
#
# # podemos iterar em um Set normalmente
# for valor in s:
#     print(valor)

# Uso interessantes com sets

# imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram .

# nós adicionamos cada cidade em uma lista Python, ja que podemos adicionar novos elementos
# e ter repetição.


# cidades = ['Belo Horizonte', 'São paulo', 'Campo grande', 'cuiaba', 'São paulo', 'Campo grande', 'cuiaba']
# print(len(cidades))
#
# # Agora precisamos saber quantas cidades destindas, ou seja, unica, temos.
#
# # podemos utilizar o set para isso
#
# print(len(set(cidades)))


# # adicionando elementos em um conjunto
# # são mutaveis, e tuplas são imutaveis
# s = {1, 2, 3}
# s.add(4)
# s.add(4)  # duplicidade não gera erro, duplicidade não gera erro mas é ignorado e nao adicionado
# print(s)
#
# # Remover elementos em um conjunto
# # forma 1
# s.remove(3)  # Não é indice, informamos o valor pra ser adicionado
# print(s)
#
# # forma 2
# s.discard(2)
# print(s)
#
# # copiando um conjunto
# # Forma 1 - Deep Copy
# print('\n')
#
# novo = s.copy()
# print(novo)
# novo.add(5)
#
# print(novo)
# print(s)
#
# print('\n')
# # Forma 2 = Shallow Copy
# novoS = s
# novoS.add(5)
#
# print(novo)
# print(s)
#
# # apaga todos os elementos
# s.clear()


# # Métodos Matemáticos de conjuntos
# estudantes_python = {'Marcos', 'Patricia', 'pedro', 'elen', 'gabriel', 'Julia'}
# estudantes_java = {'Julia', 'Fernando', 'Gustavo', 'Patricia'}
#
# # Veja que existe repetições
# # Gerar um conjunto com estudantes unicos
#
# # forma 1 - utilizando union
# unicos1 = estudantes_python.union(estudantes_java)
# # {'Gustavo', 'Fernando', 'Patricia', 'elen', 'Marcos', 'pedro', 'Julia', 'gabriel'}
#
# # unicos1 = estudantes_java.union(estudantes_python)
# # {'Gustavo', 'gabriel', 'Julia', 'Patricia', 'Marcos', 'pedro', 'elen', 'Fernando'}
# print(unicos1)
#
# # forma 2 - utilizando o carectere pipe |
# unicos2 = estudantes_java | estudantes_python
# print(unicos2)


# estudantes_python = {'Marcos', 'Patricia', 'pedro', 'elen', 'gabriel', 'Julia'}
# estudantes_java = {'Julia', 'Fernando', 'Gustavo', 'Patricia'}
#
# # gerar um conjunto que estão com ambos elementos
#
# # forma 1  - utilizando intersection
# ambos1 = estudantes_python.intersection(estudantes_java)
# print(ambos1)
#
# # forma 2 - utulizando o &
# ambos2 = estudantes_java.intersection(estudantes_python)
# print(ambos2)

# estudantes_python = {'Marcos', 'Patricia', 'pedro', 'elen', 'gabriel', 'Julia'}
# estudantes_java = {'Julia', 'Fernando', 'Gustavo', 'Patricia'}
#
# # Gerar um conjunto de estudantes que não estão no outro
#
# so_python = estudantes_python.difference(estudantes_java)
# print(so_python)
#
# so_java = estudantes_java.difference(estudantes_python)
# print(so_java)

# Soma, valor maximo. valor minimo, tamanho
# se os valores dorem reais ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
