# Crescimento de casos. estudo da população brasileira 1980-2016
# DataSUS - para pegar dados sobre a saude do brasil

import matplotlib.pyplot as plt

# armazena cada linha em uma posição da lista
dados = open('original.csv').readlines()
print(dados)
x_anos = []
y_populacao = []

# # pegar todos e separar pelo ';' colocando cada elemento em uma lista
# for i in range(len(dados)):
#     print(dados[i].split(';'))

for i in range(len(dados)):  # pega a quantidade de elementos na lista
    if i != 0:  # retira a primeira linha
        linha = dados[i].split(';')
        x_anos.append(int(linha[0]))
        y_populacao.append(int(linha[1]))


plt.bar(x_anos, y_populacao, color='#e4e4e4')
plt.plot(x_anos, y_populacao, color='k', linestyle='--')

plt.title('Crescimento de casos. estudo da população brasileira 1980-2016')
plt.xlabel('Ano')
plt.ylabel('população x 100.000.000')
plt.show()
# plt.savefig('população.png', dpi=300)
