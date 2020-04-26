import math
numero = input('Digite um número')
if numero.isnumeric():
    print(f'Dobro: {numero}')
    print(f'Triplo: {numero}')
    print(f'Raiz: {math.sqrt(int(numero))}')
else:
    print(numero)