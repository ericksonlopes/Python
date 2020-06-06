"""
**hwargs

Poderiamos chamar esse parametro de :**xis mas por convenção chamamos de **Kwargs

este é só mais um parâmetro mas diferente do args que coloca os valores extras em uma tupla
o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em
um dicionário.

"""


# def cores_favoritas(**kwargs):
#     for pessoa_chave, cor_valor in kwargs.items():
#         print(f'A cor favorita de {pessoa_chave.title()} é {cor_valor}')
#
#
# cores_favoritas(marcos='verde', julia='vermelho', fernanda='azul')
#
# # Os parâmetros *args e **kwargs não são obrigatórios.
#
# cores_favoritas()
# cores_favoritas(geek='interso')

# # exemplo mais complexo
#
#
# def cumprimento_especial(**kwargs):
#     if 'geek' in kwargs and kwargs['geek'] == 'python':
#         return 'Você recebeu um cumprimento pythonico Geek'
#     elif 'geek' in kwargs:
#         return f"{kwargs['geek']} - Geek!"
#     return 'Não tenho certeza de quem seja!'
#
#
# print(cumprimento_especial())
# print(cumprimento_especial(geek='python'))
# print(cumprimento_especial(geek='oi'))
# print(cumprimento_especial(geek='especial'))

# nas nossas funções , podemos ter: (nesta ordem)
# - parametros obrigatorios
# - *args ;
# parametros default(não obrigatorios)
# - **kwargs


# def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
#     print(f'{nome} tem {idade} anos')
#     print(args)
#     if solteiro:
#         print('solteiro')
#     else:
#         print('casado')
#     print(kwargs)
#     print('')
#
#
# minha_funcao(8, 'Julia')
# minha_funcao(8, 'Felicity', 4, 8, 9, solteiro=True)
# minha_funcao(78, 'felipe', eu='Não', voce='vai')
# minha_funcao(21, 'Carla', 9, 4, 3, java=False, python='True')


# #  motivo no qual é importante manter  ordem dos parâmetros
# # função com a ordem correta de parâmetros
# # def mostra_info(a, b, *args, instrutor='geek', **kwargs):
# #     return [a, b, args, instrutor, kwargs]
#
# # função com a ordem incorreta dos parâmetros
# def mostra_info(a, b, instrutor='geek', *args,  **kwargs):
#     return [a, b, args, instrutor, kwargs]
#
# """
# a = 1
# b = 2
# args = (3,)
# kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}
# """
# print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# # Desempacotar com **kwargs
#
#
# def mostra_nomes(**kwargs):
#     return f"{kwargs['nome']} {kwargs['sobrenome']}"  # retorna os valores das chaves
#
#
# nomes = {'nome': 'José', 'sobrenome': 'Luide'}
# print(mostra_nomes(**nomes))


def soma_multiplos_numeros(a, b, c, **kwargs):  # Desempacota qualquer coleção
    print(a + b + c)


tupla = (1, 2, 3)
conjunto = {1, 2, 3}
lista = [1, 2, 3]


soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
soma_multiplos_numeros(*lista)

# os nomes das chaves em um diiconario devem ser o mesmo do parammetros da função.
# dicionario = dict(a=1, b=2, c=3)
dicionario = {'a': 1, 'b': 2, 'c': 3}
soma_multiplos_numeros(**dicionario, nome='João')

