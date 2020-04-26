"""
try - except - else - finally

Dica de quando e onde tratar erros:

Toda entrada de dado:
OBS: A função do usuário é destruir o sistema por falta de conhecimento
"""


# # O else é executa em conjunto com o try, sae não houver erros o else é executado de imediato
# try:
#     numero = int(input('Digite um número: '))
# except ValueError:
#     print('Valor incorreto, Digite um número!')
# else:
#     print('Você Digitou:', numero)

# # O finally é executado depois das verificação de try, else e except Error
# try:
#     numero = int(input('Digite um número: '))
# except ValueError:
#     print('Valor incorreto, Digite um número!')
# else:
#     print('Você Digitou:', numero)
# finally:
#     print('Depois de todo código esse é executado, idependente do que aconteça')
#     # geralmente ele é executado para fechar ou deslocar recursos


# exemplo mais complexo
def dividir(a, b):
    try:
        return a / b
    except ValueError:
        print('Não foi possível dividir {} por {}'.format(a, b))
    except ZeroDivisionError as zero:
        print('Não é possível dividir um número por 0: ', zero)


try:
    num_a = float(input('informe o primeiro número: '))
    num_b = float(input('informe o segundo número: '))
except ValueError:
    print('Coloque apenas números dentro das entradas')
else:
    if dividir(num_a, num_b) is not None:
        print(dividir(num_a, num_b))

# # tupla de erros
# try:
#     numero = float(input('Digite um número'))
# except (ValueError, ZeroDivisionError) as conjuntoerror:
#     print('Aconteceu um erro', conjuntoerror)
# else:
#     print(numero)
