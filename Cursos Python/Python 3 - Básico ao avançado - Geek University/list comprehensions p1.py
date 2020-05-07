"""
list comprehensions(compreensão de lista)

- utilizando list comprehension nós podemos gerar novas lista com dados processados a partir
de outro iterável.

# Sintaxe da list comprehension
[ dado for dado in iterável]
"""
#
# # exemplos
# numeros = [1, 2, 3, 4, 5]
#
# res = [numero * 10 for numero in numeros]   # essa list comprehension simplifica o for de baixo
#
# # res2 = []
# # for numero in numeros:
# #     res2.append(numero * 10)
#
# print(res)
#
# """
# - a primeira parte : for numero in numeros
# - a segundo parte: numero * 10
# """
#
# res = [numero / 2 for numero in numeros]
# print(res)
#
#
# def funcao(valor):
#     return valor * valor
#
#
# res = [funcao(numero) for numero in numeros]
# print(res)

# # List comprehension X loop
#
# # loop
# numeros = [1, 2, 3, 4, 5]
# numeros_dobrado = []
# for numero in numeros:
#     numero_dobrado = numero * 2
#     numeros_dobrado.append(numero_dobrado)
# print(numeros_dobrado)
#
# # list Comprehension
# print([valor * 2 for valor in numeros])

# outros exemplos

# 1 - pegando cara caractere da string e deixando em maiúscula

nome = 'Erickson'
print([letra.upper() for letra in nome])

# 2 - Pegando a inicial de cada letra
amigos = ['Lucas', 'Pedro', "Guilherme"]
print([amigo.upper() for amigo in amigos])

# 3 - deixando a primeira letra em maiúscula


def caixa_alta(name):
    name = name.replace(name[0], name[0].upper())
    return name


amigos = ['carlos', 'emmanuel', 'leticia', 'renan']
print([caixa_alta(amigo) for amigo in amigos])

# 4 - tabuada do 3
print([num * 3 for num in range(1, 10)])

# 5 - conferindo em booleano
print([bool(valor) for valor in [0, '', (), 5, 5]])

# 6 - transformando lista de inteiros em lista de string
print([str(num) for num in range(1, 10)])




