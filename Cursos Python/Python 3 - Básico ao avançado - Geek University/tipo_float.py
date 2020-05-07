"""
Tipo float

Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais na programação é o ponte e não a vígula

"""

# Errado do ponto de vista do Float, mas gera uma tupla
valor = 1, 44

# Certo do ponto de vista do Float
valor = 1.44

print(type(valor))

# é possivel fazer duas atribuições
valor1, valor2 = 1, 44

print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um Floar para int
"""
OBS: Ao converter valores float para inteiros, nós perdemos precição
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
