try:
    with open('arquivo.txt', 'w') as arquivo:
        arquivo.write('Escreva isso')
except:
    print('erro')
