"""
Utilizando lambdas

Conhecidas por expressões lambdas ou simplesmente lambdas são funções sem nome,
ou seja, funções anônimas
"""
# # função python
#
#
# def funcao(x):
#     return 3 * x + 1
#
#
# print(funcao(4))
#
# # expressão lambda
# # lambda x: 3 * x + 1
#
# # como utilizar
# calc = lambda x: 3 * x + 1
#
# print(calc(4))

# # podemos ter expressões lambdas com varias entradas
#
# nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# print(nome_completo('erickson', 'Lopes'))
# print(nome_completo('   zacarias', 'ds dd'))

# # em funções python podemos ter nenhuma ou varias entradas em lambdas tbm
#
# amo_python = lambda: 'como não amar python'
# print(amo_python())
#
# uma = lambda x: 3 * x + 1
# duas = lambda x, y: (x * y) ** 0.5
# tres = lambda x, y, z: f'{x},{y},{z}'
#
# print(uma(5), duas(4, 5), tres(6, 5, 7))

# # outro exemplo
#
# autores = ['luiz aasconcelo', 'zezé de bamargo', ' luciano com c', 'x dom d', 'varjar eomingues']
#
# print(autores)
#
# # ordenando com sort
# autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
# print(autores)

# função quadratica
# f(x) = a * x ** 2 + b * x  + c

# definindo a funcao


def geradora_quadratica(a, b, c):
    """retorna a função f(x) = a * x ** 2 + b * x  + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
