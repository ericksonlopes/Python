"""
Tipo Booleano

Álgebra Booleana, criada por Georfe Boole

2 constante, Verdadeiro OU Falso

True -> Verdadeiro
False -> False

Obs: sempre com a inicial maiúscula

"""

ativo = False

print(ativo)

"""
Operações básicas:
"""
# Negação (NOT):
"""
Fazendo a negação, se o valor booleano for vedadeiro o resultado será falso.
se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""

print(not ativo)

logado = False
# Ou (or)
"""
É uma operação binaria, ou seja, depende de dois valores, Ou um ou outro deve ser verdadeiro.

True or True = True
True or False = True
False or True = True
False or False = False
"""

print(ativo or logado)

# E (and)
"""
Também é uma operação binaria, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiro.

True and True = True
True and False = False
False and True = False
False and True = False
"""

