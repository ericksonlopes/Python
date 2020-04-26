nome = str(input('Digite seu nome completo: ')).strip()

nome_lista = nome.split()

print(f'Seu primeiro nome é: {nome_lista[0]}')
print(f'Seu último nome é: {nome_lista[-1]}')