"""
zip

zip() - Cria um iteravel(zip object) que agrega elemento de cada um dos iteráveis passados como parâmetro

"""

# # exemplos
#
# lista = [1, 4, 7]
# lista1 = [2, 5, 8]
# lista2 = []
#
# zip1 = zip(lista, lista1)
# print(type(zip1))
#
# # podemos transformar em qualquer iterável
# print(list(zip1))
#
# zip1 = zip(lista, lista1)
# print(dict(zip1))
#
# zip1 = zip(lista, lista1)
# print(set(zip1))
#
# zip1 = zip(lista, lista1)
# print(tuple(zip1))
#
# # o zip trabalha com o iteravel de menor valor de itens, se um iteravel
# # for maior que o outro a contagem só vai até o de menor número

# # podemos utilizar diferentes tipos de iteráveis
#
# tupla = 1, 2, 3, 4, 5
# lista = [6, 7, 8, 9, 10]
# dicio = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}
#
# zt = zip(tupla, lista, dicio.values())
# print((list(zt)[0]))
#
# zt = zip(tupla, lista, dicio.values())
# print(list(zt))
#
# zt = zip(tupla, lista, dicio.values())
# dados = zt
#
# print(list(zip(*dados)))

# exemplo mais complexo
prova1 = [80, 91, 78]
prova2 = [78, 54, 99]
alunos = ['maria', 'pedro', 'carlos']

# cria um dicionario, passa como chave o dado que esta na posição 0, e pega o valor maior
# do dado da posição 1 e 2, para cada elemento, ('maria', 80, 78), ('pedro', 91, 54), ('carlos', 78, 99)
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# podemos utilizar o map() pra fazer isso

# cria um zip que cria uma lista com tuplas onde (aluno, nota) nota é a soma de cada elemento da prova1e prova2
final = list(zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2))))
print(final)
