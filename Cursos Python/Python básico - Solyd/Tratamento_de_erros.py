try:
    numero = float(input('Digite um número par ser um divisor: '))
    div = 5154 / numero
except ZeroDivisionError as err:
    print('Não é possível dividir por 0', err)
except ValueError as err:
    print('Digite apenas números!', err)
else:
    print(div)
 