"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre áspas simples -> 'uma string'
- Estiver entre áspas duplas -> "uma string"

nome = '''Geek'''

print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'luiza \ncarolina'
print(nome)
print(type(nome))

nome = "Luiza
Carolina
"
print(nome)
print(type(nome))

nome = 'Angelina \' Jolie'
print(nome)
print(type(nome))



"""

nome = 'Geek University'

# Tudo para maiúsculo
print(nome.upper())

# Tudo para minúsculo
print(nome.lower())

# Devolve uma lista com todas as palavras em string
print(nome.split())

# Slice de String
# [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14 ]
# ['G' 'e' 'e' 'k' ' ' 'U' 'n' 'i' 'v' 'e' 'r' 's' 'i' 't' 'y']
print(nome[0:4])  # Geek

print(nome[5:15])  # University

print(nome[0:15-4])  # É possivel realizar calcúlos


# [   1,     2,     ]
# ['Geek University']
print(nome.split()[0])  # Geek

print(nome.split()[1])  # University

"""
[::-1] -> Comece do primeiro elemento, vá até o ultimo elemente e inverta
"""
print(nome[::-1])  # Inverção da string Pythônico

print(nome.replace('e', '1'))  # Trocando dados por outro

print(type(nome))


# Texto palindromo
texto = 'socorram me subino onibus em marrocos'
print(texto[::-1])
print(texto)

x = "texto"
n = x + ' fim'  # Concatenar string
print(n)

print(x * 4)  # No Python é possivel multiplicar strings

# Colocando emoji

# Original : U+1F970
# Modificado : U0001F970

for num in range(1, 11):
    print('\U0001F9DF' * num)







