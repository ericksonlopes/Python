# Tudo sobre Dicionarios
# d = {key1 : value1, key2 : value2 }

for item in dir(dict):
    print(item)

print()

# # Acessar valores de dicionério
# dicionario = {'chave sala': 551, 'chave porta': 455}
# print(dicionario['chave sala'])   # acessar valor da chave
# print(dicionario['chave porta'])  # acessar valor da chave
#
# dicionario_lista = {'Usuarios': ['erickson', 'Lucas']}
# print('Você escolheu > {} <'.format(dicionario_lista['Usuarios'][1]))
#
# dicionario_dicio = {'Jogos': {'Minecraft': 8, 'CSGO': 7}}
# print('O valor da chave Minecraft é {}'.format(dicionario_dicio['Jogos']['Minecraft']))

# # Criar uma sequencia de chaves com o mesmo valor
# dicionario = dict.fromkeys([1, 2, 3], 0)
# print(dicionario)

# # Excluir todos os elementos no dicionário
# dicionario = {'chave sala': 551, 'chave porta': 455}
# dicionario.clear()
# print(dicionario)

# # fazer uma cópia do dicionario
# dicionario = {'chave sala': 551, 'chave porta': 455}
# dicionario_copia = dicionario.copy()
# print(dicionario_copia)

# # Retorna o valor da chave especificada
# dicionario = {'chave sala': 551, 'chave porta': 455}
# print(dicionario.get('chave porta'))

# # Retorna uma lista travessia array (chave, valor) tuplas
# dicionario = {'chave sala': 551, 'chave porta': 455}
# for chave, valor in dicionario.items():
#     print('A chave {} contém o valor {}'.format(chave, valor))

# # Retorna um dicionário de toda a chave.
# dicionario = {'chave sala': 551, 'chave porta': 455}
# for chave in dicionario.keys():
#     print(chave)
# print([chave for chave in dicionario.keys()])

# # se a chave não existir no dicionário, e irá adicionar valor para o padrão chaves
# dicionario = {'chave sala': 551, 'chave porta': 455}
# print(dicionario.setdefault('chave sala', 7))  # existe
# dicionario.setdefault('chave cozinha', 'chave nao encontrada')  # não existe, seja adicionado
# print(dicionario)

# # adicionar outro dicionário ao final do dicionario escolhido
# dicionario = {'chave sala': 551, 'chave porta': 455}
# dicionario_up = {'chave cozinha': 448, 'chave quarto': 335}
# dicionario.update(dicionario_up)
# print(dicionario)

# # Para retornar uma lista de todos os valores no dicionário
# dicionario = {'chave sala': 551, 'chave porta': 455}
# for valor in dicionario.values():
#     print(valor)

# # remover do dicionario e retornar uma chave e valor
#
# print(dicionario.pop('chave sala'))
# print(dicionario)

# # remover itens do dicionario
# dicionario = {'chave sala': 551, 'chave porta': 455}
# del dicionario['chave porta']
# print(dicionario)

meus_contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999',
                 'Ana': '8765-4321', 'João': '8887-7778'}

contatos_do_pedro = {'Yan': '1234-5678', 'Fernando': '4345-5434',
                     'Luiza': '4567-7654'}

meus_contatos.update(contatos_do_pedro)

# adicionar numero 9 a todos os valores de numeros
meus_contatos_novo = {nome: '9' + meus_contatos[nome] for nome in meus_contatos}
print(meus_contatos_novo)

print(meus_contatos)
