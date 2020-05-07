"""
Escrever em arquivos

"""

# # exemplo de escrita - 'w' -> Cria se não existe
# with open('novo.txt', 'w', encoding='UTF-8') as arquivo:
#     arquivo.write('Olá mundo\n')
#     arquivo.writelines('asdasdas\n')
#     arquivo.writelines('asdasdas\n')

# # escrevendo de 0 a 10 em um arquivo
# with open('novo.txt', 'w') as arquivo:
#     for num in range(10):
#         arquivo.writelines('{}\n'.format(num))

# usando laço infinito para escrever
from typing import TextIO

with open('texte.txt', 'w') as arquivos:
    print('para sair digite "Sair".\n')
    while True:
        fruta = input('Informe o nome da fruta: ')
        if fruta != 'Sair':
            arquivos.write(fruta + '\n')
        else:
            break
