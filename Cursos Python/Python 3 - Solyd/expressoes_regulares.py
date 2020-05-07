# Padrões em textos

# biblioreca reponsavel por expresões regulares
import re

string_teste = 'O gato é bonito e conjunto a gata, gatinhos, gatoes'

# r'' -> RAW sting remove os caracteres especiais como o \n
# caractere. -> acha qualquer paralvra que contenha o valor especificado com . no final
# \w -> caractere de Aa-Zz 1-9
# \w\w\w\w - > primeira palavra com 4 caracteres
padrao = re.search(r'\w\w\w\w', string_teste)

# findall para procurar por tudo, retorna uma lista '\w+' <-  repete uma ou mais vezes
padrao1 = re.findall(r'gat\w+', string_teste)
padrao2 = re.findall(r'[gat]+', string_teste)

if padrao and padrao1 and padrao2:
    print(padrao.group())
    print(padrao1)
    print(padrao2)
else:
    print('Padrao não foi encontrado')

# # .group imprime o texto
# print(padrao.group())
