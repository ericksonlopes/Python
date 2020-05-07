"""
Bloco with

Passo apra trabalhar com arquivos
-abrir
-manipular
-fechar

O bloco with é utilizado para trabalhar com algo.
with ja abre e fecha o arquivo.
"""

# with - Forma pythonica de manipulaçao de arquivos
with open('texte.txt') as arquivo:
    print(arquivo.readlines())


if arquivo.close:
    print('o arquivo esta: fechado')
else:
    print('o aqrquivo esta: aberto')