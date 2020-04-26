# Muitas funções disponiveis
# para coleçoes, vairaveis e etc...

# no caso da string, todas as funções retornam varios valores
# Os valores originais não são alterados

# # captalize(), deixa a frase formal
# valor = 'ESTA É UMA FRASE DE TESTE'
# print(valor.capitalize())

# # casefold(), deixa o texto em minusculo
# valor = 'ESTA É UMA FRASE DE TESTE'
# print(valor.casefold())

# # center(). coloca a frase exatamente no meio da distancia descrita
# valor = 'Palavra'
# valor2 = 'letras'
# print('.' + valor.center(20) + '.' + valor2.center(20) + '.')
#
# for indice, letra in enumerate(valor2):
#     print('.' + letra.center(indice * 4) + '.')

# # startswith() e endswith()
# valor = 'Palavra'
# print(valor)
#
# if valor.startswith('P'):  # Verifica se a string começa com P
#     print('começa com P')
# else:
#     print('Não começa com P')
#
# if valor.endswith('e'):  # verifica se termina em e
#     print('Termina em "e"')
# else:
#     print('não termina em "e"')

# # verifica a posição de uma string dentro de outra string
# valor = 'Sistema operacional precisa ser testando diante a lei de parcia'
# print(valor.index('ser'))  # se encontrar devolve sua posição
# print(valor[28])

# # verificar se existe uma string dentro da string
# valor = 'Sistema operacional precisa ser testando diante a lei de parcia'
# print(valor.find('ser'))  # se encontrar devolve sua posição
# print(valor[valor.find('ser')])
# print(valor.find('hh'))  # caso não exista a string informada retorna -1

# # isnumeric() - Verifica se é número
# valor = '001500'
# if valor.isnumeric():
#     print('OK', valor.isnumeric())
#     print(int(valor))
# else:
#     print('NO!', valor.isnumeric())

# # Retirar os espaços
# valor = '  Nome  '
# print('>' + valor.strip() + '<')

# zfill() - coloca a string em quantidade de caractere determinada e acrescenta 0 nas posições vazias
valor = '10'
print(valor.zfill(10))


