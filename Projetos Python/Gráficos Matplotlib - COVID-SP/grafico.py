import matplotlib.pyplot as plt

# primeiro tenta se conectar ao arquivo
try:
    # cria uma lista com cada linha(linha.split())
    # em cada linha ele cria uma lista com a string separando pelo ";" ([0].split(';') )
    # pegando a informação do arquivo especificado
    lista = [linha.split()[0].split(';') for linha in open('COVID19_20200417.csv')]
except FileNotFoundError:
    print('Não foi possível encontrar o arquivo')
else:
    lista_data = []
    lista_casosA = []

    for item in lista:
        # se o item[1] for igual a 'SP'
        if item[1] == 'SP':
            # coloca na lista as datas
            lista_data.append(item[2])
            # coloca na lista os casosAcumulados
            lista_casosA.append(int(item[4]))

    # Legendas
    plt.title('Casos Acomulados de Covid em SP')  # titulo
    plt.xlabel("Datas")  # titulo eixo x
    plt.ylabel('Casos')  # titulo eixo y

    # Plota os valores dentro do gráfico
    plt.plot(lista_data, lista_casosA)
    # gira os dados
    plt.tick_params(axis='x', rotation=90)
    # chama função que exibe a tela, com todos os dados recebidos
    plt.show()
