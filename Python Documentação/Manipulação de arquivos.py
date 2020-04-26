# Tudo sobre Manipulação de arquivos
f = open("manipulação-arquivos/arquivo.txt")
for item in dir(f):
    print(item)
print()

# # # Para abrir um arquivo para leitura, basta especificar o nome do arquivo:
# # f = open("manipulação-arquivos/demofile.txt")
# # O código acima é o mesmo que:
# f = open("manipulação-arquivos/demofile.txt", "rt")
# r - para leitura
# t - para texto

# # Para abrir o arquivo, use a função open() interna.
# # A função open() retorna um objeto de arquivo, que possui um método read() para ler o conteúdo do arquivo:
# f = open("manipulação-arquivos/demofile.txt", "r")
# print(f.read())

# # Retorne os 5 primeiros caracteres do arquivo:
# f = open("demofile.txt", "r")
# print(f.read(5))

# # Leia uma linha do arquivo:
# f = open("demofile.txt", "r")
# print(f.readline())
#
# # ler todas as linhas com loop
# for item in f:
#     print(item)

# # fechar arquivo
# f = open("demofile.txt", "r")
# print(f.readline())
# f.close()

# # Abra o arquivo "demofile2.txt" e acrescente conteúdo ao arquivo:
# # "a" - Anexar - será anexado ao final do arquivo
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()
# # abra o arquivo para ver as mudanças
# f = open("demofile2.txt", "r")
# print(f.read())
#
# # "w" - Write - substituirá qualquer conteúdo existente
# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()
# # abra o arquivo para ver as mudanças
# f = open("demofile3.txt", "r")
# print(f.read())

# # criar um arquivo, com x que retorna erro casa ele nao exista
# f = open('newfile.txt', 'x')
# # criar um arquivo, com w que cria caso não exista
# f = open('newfile.txt', 'w')

# # excluir arquivo, usando biblioteca
# import os
# os.remove('newfile.txt')

# # verificando se o arquivo existe, usando biblioteca
# import os
# if os.path.exists('Listas.py'):
#     print('Existe')
# else:
#     print('Não existe')

# # criar pastas
# import os
# os.mkdir('novapasta')

# # excluir pastas, apenas vazias
# import os
# os.rmdir('tesas')

f = open('demofile2.txt', 'r')
print(f.readline())
