from random import randint


def gerar_numero():
    x = randint(0, 9)
    y = randint(0, 9)
    try:
        print(x / y)
    except ZeroDivisionError:
        print('Ocorreu um erro, não é possivel diviri números por 0')


gerar_numero()
