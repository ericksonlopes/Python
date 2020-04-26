numero = input('Digite um número: ')

if numero.isnumeric():
    print('Sucessor', int(numero) + 1)
    print('Antecessor', int(numero) - 1)
else:
    print(numero)
