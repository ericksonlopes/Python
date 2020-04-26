num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para  BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opc = int(input('sua opção: '))
if opc == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)}')
elif opc == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)}')
elif opc == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)}')