"""
estruturas lógicas: and(e), or(ou), not(não), is(é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or, is

Regras de funcionamento
para o 'and', ambos os valores precisam ser True
para o 'or',  um ou outro valor precisa ser True
para o 'not', o valor do booleano é invertido, se for True vira False, se for False vira True
para o 'is',
"""

ativo = True
logado = False


# Se os dois estiverem ativo = True
if ativo and logado:
    print('(and) Bem-vindo usuário!')
else:
    print('(and) precisa ativar sua conta, Por favor, cheque seu e-mail')


# Se um ou os dois estiverem ativo = True
if ativo or logado:
    print('(or) Bem-vindo usuário!')
else:
    print('(or )Você precisa ativar sua conta, Por favor, cheque seu e-mail')


# Se estiver ativo = False (se nao esta ativo voce precisa ativar sua conta)
if not ativo:
    print('(not) Você precisa ativar sua conta, Por favor, cheque seu e-mail')
else:
    print('(not) Bem-vindo usuário')

# print(not True)


# Vai de acordo com o seu acompanhante
if ativo is True: # Ativo é True
    print('(is True) Bem-vindo usuário!')
else:
    print('(is True) Você precisa ativar sua conta, Por favor, cheque seu e-mail')


if ativo is False:  # Ativo é False
    print('(is False) Bem-vindo usuário!')
else:
    print('(is False) Você precisa ativar sua conta, Por favor, cheque seu e-mail')

# Outras ultilizações do is integrado a funções

nome = 'Geek'
print(nome)

print(f'{nome} é um titulo? ', nome.istitle())
print(f'{nome} é um caractere decimal?', nome.isdecimal())
print(f'{nome} está todo em minúsculo?', nome.islower())
print(f'{nome} está todo em maiúsculo?', nome.isupper())
print(f'{nome} é numérico?', nome.isnumeric())



