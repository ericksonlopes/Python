"""
recebendo dados do usuário

input -> Todo dado recebido via input é do tipo String

em python,tudo que estiver entre :
- Aspas simples ''
- Aspas duas ""
- Aspas simples triplas ''''''
- Aspas duas triplas """"""

"""

# entrada de dados
# print("Qual é o seu nome? ")
# nome = input()  # input -> entrada
nome = input('qual é o seu nome? ')

# exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) {0}' .format(nome))

# Exemplo do print moderno 3.x
# Print('Seja bem-vindo(a) %s' % nome)

# exemplo de print 'mais atual'
print(f'Seja bem-vindo(a) {nome.strip().title()}')


# print('Qual sua idade? ')
# idade = input()
idade = int(input('Qual sua idade ?'))

# processamento

# Saída de dados

# Exemplo de print 'antigo' 2.x
# print('A {0} tem {1} anos' .format(nome, idade))
# print('A %s tem %s anos' % (nome.title().strip(), idade.strip()))

# Forma atual 3.8
print(f'A(o) {nome.title().strip()} tem {idade}')

# int(idade)=> cast
"""
Cast é a converção de um tipo de dado para outro
"""

print(f'A(o) {nome.title().strip()} nasceu em {2020 - idade}')
