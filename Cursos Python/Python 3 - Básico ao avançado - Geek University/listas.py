"""
Listas

Listas são mutáveis: elas podem mudar constantemente

Listas em python funcionam como vetores/matrizes (arrays) em outras linguagem, com a diferença
de serem DINÂMICO e tambEm podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    seré SEMPRE do tipo inteiro e tera 5 valores.

- Dinâmico: Não possuem tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- qualquer tipo de dado: as listas não possuem tipo de dado fixo ou seja podemos colocar qualquer tipo de daddo

As listas em python são representadas por conlchetes: []
"""
type([])

lista1 = [1, 11, 11, 15, 42, 32, 11, 32, 29]

lista2 = ['f', 'a', 'e', 'b', 'd', 'e', 'g']
lista02 = list('fgedabc')

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')


# # Podemos facilmente checar se determinado valor está contido na lista
# num = 7
# if 8 in lista4:
#     print(f'Encontrei o número {num}')
# else:
#     print(f"Não encontrei o número {num}")
#
# print('\n')
#
# # Podemos facilmente ordenar uma lista
# lista1.sort()  # Números
# lista2.sort()  # Letras
# lista02.sort()  # Letras na list()
# print(lista1)
# print(lista2)
# print(lista02)
#
# print('\n')
#
# # Podemos facilmente contar o número de ocorrência de um valor em uma lista
# print(lista1.count(11), 'número 11')  # Quantos números 11 tem dentro de lista1
# print(lista5.count('e'), 'Letras "e"')  # quantas letras 'e' tem dentro de lista5
#
# print('\n')
#
# #  Adicionar elementos em listas
# """
# Para adicionar elementos em lista, utilizamos a dunção append
# """
# print(lista1)
# lista1.append(53)
# print(lista1)
#
# # OBS: com append só conseguimos adicionar 1 elemento por vez
# # lista1.append(1, 12, 10) Erro
#
# lista1.append([0, 1, 2])  # colocando lista como elemento unico(sublista)
#
# if [0, 1, 2] in lista1:
#     print('Encontrei a lista\n', lista1)
# else:
#     print('Não encontrei a lista')
#
# lista1.extend([123, 44, 67])  # adiciona cada elemento da lista como valor á lista
# print(lista1)
#
# print('\n')
#
# # Podemos inserir um novo elemento na lista informando a posição do indice
# # Isso não substitui o outro valor que estana na posição, o mesmo sera deslocado para a direita da lista
# lista1.insert(2, 'Novo indice')
# print(lista1)
#
# print('\n')
#
# # juntar duas listas
# lista1 = lista1 + lista2
# # lista1.extend(lista2)
# print(lista1)


# #  Forma 1 de inverter a lista
# lista1.reverse()  # inverte a lista
# lista2.reverse()  # inverte a lista

# #  Forma 2 de inverter a lista
# print(lista1[::-1])  # inverte a lista com slice
# print(lista2[::-1])  # inverte a lista com slice

# #  Copiar uma lista
# lista6 = lista2.copy()
# print(lista6)


# # Saber o tamanho da lista, contar quantos elementos tem dentro da lista
# print(len(lista2))

# Podemos remover facilmente o ultimo elemento de uma lista
# x = [1, 2, 3]
# y = [4, 5, 6]
#
# x.pop(2)  # remove o número 3
# a = x.pop()  # Remove o ultimo elemento e tambem retorna o valor
# y.insert(0, a)  # inseri na primeira casa o valor do ultimo indice da lista x
# print(a)
# print(x)
# print(y)
# # Podemos remover um elemento pelo indice
# y.pop(2)

# # podemos remover todos os elementos(zerar a lista)
# print(lista5)
# lista5.clear()
# print(lista5)

# # Repetir os elementos da lista
# nova = [1, 2, 3]
# nova = nova * 3
# print(nova)

# # podemos converter uma string para uma lista
# curso = 'Programação em python: Essencial'
# print(curso)
# curso = curso.split()
# print(curso)
#
# # OBS: Por padrao o split separa os elementos pelo espaço entre elas
#
# # Exemplo 2
# curso = 'Programação,em,python:,Essencial'
# print(curso.split(','))

# # Convertendo uma lista em uma string
# lista6 = ['Programação', 'em', 'python:', 'Essencial']
# print(lista6)
#
# # Pega lista6 e coloque espaço entre cada elementoe transforme em string
# curso = ' '.join(lista6)
# print(curso)
#
# # Pega lista6 e coloque cifrão entre cada elementoe transforme em string
# curso = '$'.join(lista6)
# print(curso)

# # Podemos realmente colocar qualquer tipo de dado em uma lista inclusive misturando esses dados
# lista7 = [1, 1.5, True, 'Geek', 'd', [1, 2, 3], 213246345]
# print(lista7)
# print(type(lista7))

# # iterando sobre listas
# # Exemplo 1 - utilizando for
# soma = 0
# for elemento in lista1:
#     print(elemento)
#     soma = soma + elemento
#     print(soma)

# # Exemplo 2 - utilizando while
# carrinho = []
# produto = ''
#
# while produto != 'sair':
#     print('Adicione um produto na lista ou digite "fechar" para sair: ')
#     produto = input()
#     if produto != 'fechar':
#         carrinho.append(produto)
# for produto in carrinho:
#     print(produto)


# # utilizar variáveis em listas
# numeros = [1, 2, 3, 4, 5]
# print(numeros)
# num1 = 1
# num2 = 2
# num3 = 3
# num4 = 4
# num5 = 5
#
# numeros = [num1, num2, num3, num4, num5]
# print(numeros)

# # Fazemos acesso aos elementos de forma indexada
# cores = ['verde', 'amarelo', 'azul', 'branco']
# print(cores[0])
#
# # Fazer acesso aos elementos de forma indexada inversa
# print(cores[-2])

# cores = ['verde', 'amarelo', 'azul', 'branco']
# for cor in cores:
#     print(cor)
#
# indice = 0
# while indice < len(cores):
#     print(cores[indice])
#     indice += 1

# # Gerar indice em um for
# cores = ['verde', 'amarelo', 'azul', 'branco']
# for indice, cor in enumerate(cores):
#     print(indice + 1, cor)
#
# # Criando uma lista dentro da variavel com indice e valor enumerate de cores
# cores = list(enumerate(cores))
# print(cores)

# # listas aceitam valores repetidos
# lista = []
#
# lista.append(22)
# lista.append(22)
# lista.append(99)
# lista.append(99)
#
# print(lista)

# # métodos não tão importantes, porém uteis
# # Encontrar o índice de um elemento na lista
#
# # em qual indice da lista esta o valor 6
# numeros = [5, 6, 7, 5, 8, 9, 10]
#
# # Retorna o indice do primeiro elemento encontrado
# print(numeros.index(6))
#
# # em qual indice da lista esta o valor 9
# # Retorna o indice do primeiro elemento encontrado
# print(numeros.index(9))
#
# # OBS: Caso não tenha ese elemento na lista, sera erro
#
# # Podemos fazer busca dentro de um range, qualindice começar a buscar
# print(numeros.index(5, 1))  # buscando a partir do indice
# # Caso não tenha esse item a partir do numero de inicio gera um erro
#
# # Podemos fazer busca dentro de um range, inicio/fim]
# print(numeros.index(5, 2, 4))  # buscar o indice entre os indice 6 a 8

# revisão de slicing
# lista[inicio:fim:passo]
# renge[inicio:fim:passo]

# # Trabalhando com slice de lista com o parâmetro inicio
# lista = [1, 2, 3, 4]
#
# # inicio
# print(lista[::])  # Pegando todos os elementos
# print(lista[1:])  # iniciando no indice 1 e pegando todos os elementos restantes
# print(lista[-1:])  # pegando o primeiro valor de traz para frente
#
# # fim
# print(lista[:2])  # Pega todos os elementos do começo ao indice 2 -1
# print(lista[:4])  # começa do 0, pegsa até o indice 4 - 1
# print(lista[1:3])  # começa no indice 1, até o indice 3-1
# print(lista[0:-1])  # começa do 0 e vai até o primeiro valor de traz para frente
#
# # passo
# print(lista[::2])  # Começando do 0, indo até o final, passando de 2 em 2
# print(lista[1::2])  # Começando do 1, indo até o final, passando de 2 em 2
#
# nome = 'Erickson Lopes Da Silva'
# print(nome[0:7+1])
# print(nome[9:15])
# print(nome[::2])

# # invertendo valores em uma lista
# # nomes = ['Geek', 'University']
# #
# # # ambos fazem a mesma coisa
# # nomes[0], nomes[1] = nomes[1], nomes[0]
# # nomes.reverse()
# #
# # print(nomes)

# # Soma*, valor Máximo*, Valor minimo*, tamanho*
#
# # * Se os valores forem todos inteiros ou reais
#
# lista = [1, 2, 3, 4, 5, 6]
# print(sum(lista))  # soma a lista (1+2+3...)
# print(max(lista))  # pega o valor mais alto
# print(min(lista))  # pega o menor valor
# print(len(lista))  # tamanho da lista

# # transformar uma lista em tupla
# lista = [1, 2, 3, 4, 5, 6]
# print(lista)
# print(type(lista))
#
# tupla = tuple(lista)
# print(tupla)
# print(type(tupla))

# # Desempacotamento de listas
# lista = [1, 2, 3]
# num1, num2, num3 = lista
#
# print(num1)
# print(num2)
# print(num3)
# # Os elementos tem que ser na mesma quantia de variaveis

# copiando uma lista para outra(Shallow Cpoty e Deep copy)

# forma 1
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
# isso é chamado de deep copy

print(nova)
nova.append(4)

print(lista)
print(nova)

print('\n')
# forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)
nova = lista    # Cópia

print(nova)
nova.append(4)

print(nova)
print(lista)


