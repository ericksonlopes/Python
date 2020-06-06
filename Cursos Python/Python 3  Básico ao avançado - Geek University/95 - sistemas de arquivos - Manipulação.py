# -*- coding: utf-8 -*-

"""
Sistemas de arquivos - Manipulação

"""
# importação do módulo
import os

# # saber se o diretório existe
# # arquivo
# print(os.path.exists('Conjuntos.py'))  # True
#
# # pasta
# print(os.path.exists('geek'))  # True

# # Criar arquivos
# # forma 1
# open('arquivo_criado.txt', 'w').close()
#
# # forma 2
# with open('arquivo_criado_2.txt', 'w') as arquivo:
#     pass

# # Criar pasta / diretório
# os.mkdir('Pasta mkdir')

# # cria varais pastas
# os.makedirs('p1/p2')

# # cria varais pastas mas não retornar erro se existir
# os.makedirs('p1/p2', exist_ok=True)

# # renomear arquivos e diretórios
# os.rename('p1/p2/teste.txt', 'p1/p2/modificado.txt')

# # remover arquivos e se o arquivo estiver em uso retorna erro
# os.remove('p1/p2/modificado.txt')

# # removendo pastas
# os.rmdir('p1/p2')

# # criando varias pastas e arquivos
# for i in range(10):
#     os.mkdir(f'p1/asdasda/{i}')
#     with open(f'p1/asdasda/{str(i)}.txt', 'w') as arquivo:
#         pass

# # remover arvore de diretoriso e arquivos
# for item in os.scandir('p1/asdasda'):
#     if item.is_file():
#         os.remove(item)
#     if item.is_dir():
#         os.rmdir(item)

# # remover arvores de diretório
# os.rmdir('p1/asdasda/0')

# # mover itens para lixeira
# from send2trash import send2trash
# send2trash('path')

# criar itens temporarios na pasta temp
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print('criado!' + tmp)
    with open(os.path.join(tmp, 'arquivo_criado.txt'), 'w') as arquivo:
        arquivo.write('Olá mundo')
    input()
