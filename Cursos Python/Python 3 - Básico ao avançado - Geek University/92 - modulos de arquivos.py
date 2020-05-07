# -*- coding: iso-8859-1 -*-

# # cria se não existe
# try:
#     with open('categorias_treino.txt', 'x', encoding='UTF-8') as arquivo:
#         arquivo.write('Novo arquivo criado')
# except FileExistsError:
#     print('O arquivo ja foi criado')

# # escreve infinitamente até usar o break, deleta tudo e escreve
# with open('categorias_treino.txt', 'w') as arquivo:
#     while True:
#         fruta = input('Digite uma fruta: ')
#         if fruta == 'Sair':
#             break
#         else:
#             print('Digite "Sair" para sair.')
#             arquivo.write(fruta + '\n')

# # Adiciona ao final do arquivo como um append
# try:
#     with open('categorias_treino.txt', 'a') as arquivo:
#         texto = input('Digite um texto que sera adicionado ao final: ')
#         arquivo.write(texto)
# except FileExistsError:
#     print('O arquivo não existe')

with open('categorias_treino.txt', '') as arquivo:
    arquivo.seek(0)
    arquivo.write('No topo\n')
