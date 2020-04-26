with open('arquivo-w.txt', 'w') as arquivo:
    arquivo.write('Essa mensagem sempre preenche o arquivo')

with open('arquivo-a.txt', 'a') as arquivo:
    arquivo.write('Essa mensagem sempre acrescenta no final do arquivo\n')

with open('arquivo-a.txt', 'r') as arquivo:
    # lendo o arquivo
    print(arquivo.read())
