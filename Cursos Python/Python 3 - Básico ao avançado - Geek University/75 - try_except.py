"""
Try - except

tratar erros que podem ocorrer, previnindo assim que o programa pare de funcionar.

"""

# # SyntaxError
# try:
#     geek()
# except:
#     print('ops')

# #  como tratar esse erro
# try:
#     geek()  # NameError
# except NameError:
#     print('Não foi encontrado o nome pedido')

# try:
#     len(5)  # TypeError
# except TypeError:
#     print('ops')

# # Detalhes especificos de erro
# try:
#     len(5)
# except TypeError as err:
#     print(f'O seguinte erro aconteceu: {err}')

# # podemos efetuar diversos tratamentos de erros
# try:
#     print('4'[5])
# except TypeError as tr:
#     print('Erro', tr)
# except NameError as Ne:
#     print('Erro', Ne)
# except IndexError as s:
#     print('Aconteceu outro erro', s)


# Retornando algo com tratamento de erro
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        print('Essa chave não existe')
        return None


dic = {'nome': 'geek'}
print(pega_valor(dic, 'nome'))
