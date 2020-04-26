class Error(Exception):
    pass


class Input_Error(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Digite um número de 0 a 10: '))
        if x > 10:
            raise Input_Error('Nota é maior que 10, inválido')
        if x < 0:
            raise Input_Error('Nota é menor que 0')
    except ValueError:
        print('Valor invalido')
    except Input_Error as ex:
        print(ex)
