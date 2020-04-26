"""
entendendo *args

- *args é um parâmetros como outro qualquer (parâmetro de entrada de uma função)
isso significa que você poderá chamar de qualquer coisa desde que comece com asteristico.

Exeplo

*xin
mas por convenção,  utilizamos *args para definí-lo

o parâmetro args utilizado em uma função coloca os valores extras informados como entrada em uma tupla
então desde ja lembre-se que tuplas são imutaveis
"""

# # Exemplo
#
#
# def soma_todos_numeros(n1, n2, n3):
#     return n1 + n2 + n3
#
#
# print(soma_todos_numeros(1, 2, 3))

# # entendedo o args
#
#
# def soma_todos_numeros(nome, *args):
#     lista = []
#     for num, a in enumerate(args):
#         lista.append(args[num])
#         num += 1
#     return lista  # retorna a lista
#
#
# print(soma_todos_numeros('Erickson'))
# print(soma_todos_numeros('Erickson', 1.4, 2))
# print(soma_todos_numeros('Erickson', 'a', 3))
# print(soma_todos_numeros('Erickson', 2, True, 4))
# print(soma_todos_numeros('Erickson', 3, 4, 5, 6))

# # Outro exemplo de utilização do args
#
#
# def verifica_info(*args):
#     if 'geek' in args and 'University' in args:
#         return 'Bem-vindo '
#     return 'Eu não tenho certeza de quem você é ...'
#
#
# print(verifica_info())
# print(verifica_info(1, True, 'University', 'geek'))
# print(verifica_info('geek', 5))


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1, 5, 3))

numero = [1, 2, 3]
# Desempacotador
print(soma_todos_numeros(*numero))
numero = (1, 7, 5, 6, 9)
print(soma_todos_numeros(*numero))

# o asteristico serve para que informemos ao python que estamos passando como argumento uma coleção de dados
# Ele saberá que precisa desempacotar esses dados

