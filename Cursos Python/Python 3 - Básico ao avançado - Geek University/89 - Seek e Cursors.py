"""
Seek e Cursors

Seek - Utiliza-se para  moveimentar o cursor pelo arquivo
Cursors -
"""
# Seek
# arquivo = open('texte.txt', encoding='UTF-8')
# print(arquivo.read())
# print()
# # movimentar o cursos pelo aarquivo com a função Seek
# arquivo.seek(12)
# print(arquivo.read())

# # imprimir linha e separando strings
# arquivo = open('texte.txt', encoding='UTF-8')
# ret = arquivo.readline()  # Imprime uma linha
# print(ret)
# print(ret.split(' '))  # Separa cada palavra por string

# cria uma lista com todas as linhas
arquivo = open('texte.txt', encoding="UTF-8")
arquivo = arquivo.readlines()

print(len(arquivo))

# # Curcors
# arquivo = open('texte.txt', encoding='UTF-8')
# print(arquivo.read())
