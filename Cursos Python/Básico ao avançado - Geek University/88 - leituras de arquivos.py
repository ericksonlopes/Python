dados = open('texte.txt', encoding='UTF-8')

# [print(item) for item in dir(dados)]
des_dado = dados.read()
print(des_dado)

dados.close()

