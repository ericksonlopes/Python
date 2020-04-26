# -*- coding: utf-8 -*-
"""
Escrevendo em arquivos csv

reader() leitor
writer() escritor

writerow() ->  Escreve uma linha

"""


def write_escreve():
    from csv import writer

    with open('filmes.csv', 'w', encoding='utf-8') as arquivo:
        # objeto de escrita
        escritor = writer(arquivo, delimiter=',', lineterminator='\n')

        # variavel nome filme
        filme = None

        # cabeçalho
        escritor.writerow(['titulo', 'genero', 'duracao'])

        while filme != 'sair':
            filme = input('Digite o nome do filme: ')
            if filme != 'sair':
                genero = input('Digite o genero: ')
                duracao = int(input('Duração (em minutos): '))
                escritor.writerow([filme, genero, duracao])
            else:
                break


def dictwrite_escreve():
    from csv import DictWriter

    with open('filmesdict.csv', 'w') as arquivo:
        # variavel com o cabçalho
        cabecalho = ['titulo', 'genero', 'duracao']
        # definindo que o dictwrite ira escrever o cabecalho
        escritor = DictWriter(arquivo, fieldnames=cabecalho, lineterminator='\n')
        # escrevendo no arquivo o cabeçalho
        escritor.writeheader()
        filme = None
        while filme != 'sair':
            filme = input('Digite o nome do filme')
            if filme != 'sair':
                genero = input('Gênero do filme')
                duracao = input('Duracao (em minutos)')
                escritor.writerow({"titulo": filme, "genero": genero, "duracao": duracao})


dictwrite_escreve()
