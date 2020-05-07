# -*- coding: utf-8 -*-

"""
sistemas de arquivo - Navegação

os - sistema oporacional
"""

# # importanto biblioteca
# import os
#
# # descobrindo endereço atual
# print(os.getcwd())
#
# # Mudar o diretório
# os.chdir('..')
#
# print(os.getcwd())


# # importanto biblioteca
# import os
#
# # checar se o diretório é absoluto ou relativo
# esta_aqui = os.getcwd()
# print(os.path.isabs(esta_aqui))

# # importanto biblioteca
# import os
# import platform
#
# # identificar o sistema operacional  com módulo os
# print(os.name)
#
# # mais detalhes sobre o sistema
# print(platform.uname())

# # importanto biblioteca
# import os
#
# # pegar diretório atual e juntar com outro
# # diretorio que sera juntado ao atual
# print(os.getcwd())
# diretorio_arquivo = os.path.join(os.getcwd(), 'geek', 'university')  # entrar na pasta 'geek' e dentro dela a univers.
# print(diretorio_arquivo)

# # listar os arquivos de um diretório
# import os
# direct_atual = os.getcwd()
# [print(x) for x in os.listdir(direct_atual)]
# print('Arquivos encontrados: ', len(os.listdir(direct_atual)))

# # obter mais detalhes sobre o arquivo dentro da listagem listar os arquivos de um diretório
# import os
# direct_atual = os.getcwd()
# [print(x) for x in os.scandir(direct_atual)]

# mais detalhes sobre um arquivo
import os
dict_atual = os.getcwd()
arquivos_past_atual_lista = os.scandir(dict_atual)
lista_dados = list(arquivos_past_atual_lista)
# pegar primerio arquivo e verificar
print(lista_dados[5].name)  # nome
print(lista_dados[5].is_dir())  # é uma pasta ?
print(lista_dados[5].is_file())  # é um arquivo ?
print(lista_dados[5].path)  # caminho até ele
print(lista_dados[5].stat())  # estatísticas
print(lista_dados[5].stat()[6])  # saber o tamanho em byte

arquivos_past_atual_lista.close()
# quando utilizamos a função scardir() nós precisamos fechala




