"""
Módulo Collections - Default Dict

"""
# # Recap Dicionário
# 
# dicionario = {'Curso': 'Programação em python: Essencial'}
#
# print(dicionario)
#
# print(dicionario['Curso'])
#
# print(dicionario)
"""
 Default Dict -> Ao criar dicion[ario utilizando-o, n[os informamos um valor default,
 podendo utilizar um lambda para isso. Este valor será utilizadpo sempre que não houver
 um valor definido. Caso tentemos acessar uma chave que não exista, essa chave será
 criada e o valor default será atrivuido.
"""

# fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)
print(dicionario)
dicionario['curso'] = 'programação em python'
print(dicionario['outro'])
print(dicionario)

