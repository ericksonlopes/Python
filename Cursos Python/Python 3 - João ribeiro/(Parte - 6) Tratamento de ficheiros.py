# tratamento de ficheiros
# a função principal para tratamento de ficheiros é a função open()
# open(ficheiro, modo)

# modo
# 'r' - Read - Abre ficheiro para leitura, erro se não existir
# 'a' - Append - Abre o fixeiro para acrescentar dados, Cria se não existe
# 'w' - Write - abre um ficheiro para escrita. Cria se não exite
# 'x' - Criar - apnas Cria o ficheiro, retorna erro se ja existe

# adicionalmente podemos usar outros dois modos:
# 't' - texto - modo de texto
# 'b' - binário - pode guardar imagens por exemplo...

# abrir ficheiro
# ficheiro = open('ficheiro.txt')
# o mesmo que
# ficheiro = open('ficheiro.txt', 'rt')

# # ler o ficheiro
# ficheiro = open('ficheiro.txt')
# print(ficheiro.read())

# # ler partes do ficheiro
# # a função read lê o ficheiro por completo, mas permite ler apenas uma parte
# ficheiro = open('ficheiro.txt')
# print(ficheiro.read(10))

# # ler linhas de um ficheiro
# ficheiro = open('ficheiro.txt')
# print(ficheiro.readline())
# print(ficheiro.readline())

# # podemos fazer um loop para ler todas as linhas
# ficheiro = open('ficheiro.txt')
# for linha in ficheiro:
#     print(linha)

# # é uma boa prática fechar o ficheiro após sua abertura e uso
# ficheiro = open('ficheiro.txt')
# for linha in ficheiro:
#     print(linha)
# ficheiro.close()


# # escrever dados em um ficheiro
# # utilização do modo 'a' (append) e 'w' (wirte)
# ficheiro = open('ficheiro_dois.txt', 'a')
# ficheiro.write('\nfrase acrescentada ao ficheiro')
# ficheiro.close()
#
# ficheiro = open('ficheiro.txt')
# for linha in ficheiro:
#     print(linha)
# ficheiro.close()

# # usando o 'w', formata o ficheiro colocando apenas 'Frase escrita no ficheiro'
# ficheiro = open('ficheiro_w.txt', 'w')
# ficheiro.write('Frase escrita no ficheiro')
# ficheiro.close()

# # criando ficheiro
# # modos 'a', 'x' e 'w'
# ficheiro = open('ficheiro_x.txt', 'x')
# ficheiro.close()

# # eliminar um ficheiro usando a importação do módulo 'os'
# import os
# os.remove('ficheiro_w.txt')


# # verificar se o ficheiro existe e eliminar ou criar
# import os
# if os.path.exists('ficheiro_AC.txt'):
#     os.remove('ficheiro_AC.txt')
# else:
#     ficheiro = open('ficheiro_AC.txt', 'x')
#     ficheiro.write('Programado para morrer')
#     ficheiro.close()

# remover uma pasta vazias
import os
    
os.rmdir('docs')  # indique o caminho

