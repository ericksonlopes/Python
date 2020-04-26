"""
Loop while

while expressão_booleana:
    //execição do loop

o bloco do while sera reperido enquanto a expressão booleana for verdadeira.

expressão Booleana é toda expressão onde o resultado é True ou False.
exemplo:

num = 5
num < 5 - False (expressão boleana)
num == 5 - True
num < 10  - True

"""

# Exemplo 1
numero = 1

while numero < 10:  # numero é menor que 10?
    print(numero)
    numero += 1  # numero = numero + 1

# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito


# Exemplo 2
resposta = ' '

while resposta != 'sim':  # resposta é diferente de sim ?
    resposta = input('Já acabou Jéssica? ')
