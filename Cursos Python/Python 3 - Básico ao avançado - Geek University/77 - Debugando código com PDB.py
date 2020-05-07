"""
77 - Debugando código com PDB
PDB -> Python Debugger

bug -> inseto
"""


# # Existem formas profissionais de fazer esse 'debug' , utilizando o debugger
# # em python , podemos fazer isso em diferentes IDEs, como pycharm
# # Degugar código com print é uma péssima prática
# def dividir(a, b):
#     print('a={}. b={}'.format(a, b))
#     try:
#         return a / b
#     except ValueError:
#         print('Não foi possível dividir {} por {}'.format(a, b))
#     except ZeroDivisionError as zero:
#         print('Não é possível dividir um número por 0: ', zero)
#
#
# print(dividir(4, 7))

# # import pdb
#
# nome = 'Erickson'
# sobrenome = 'Lopes'
# # pdb.set_trace()
#
# breakpoint()  # não é mais necessário importar a biblioteca pdb
#
# nome_completo = nome + ' ' + sobrenome
# curso = 'Programação de python completo'
# final = '{} faz curso de {}'.format(nome_completo, curso)
#
# print(final)
#
# # podemos importar dessa forma tambem
# # import pdb; pdb.set_trace()
#
# # o debug é utilizado durante o desenvolvimento

# # a partir do python 3.7 o debug é incorporado como função built-in chamada breackpoint
# breakpoint()
