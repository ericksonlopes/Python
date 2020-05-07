from csv import writer

# busca o arquivo em modo que acicione ao final
with open('arquivos/lutadores.csv', 'a', encoding='utf-8') as arquivo:

    # declarando objeto de escrever, determinando onde quer escrever e como
    escrever = writer(arquivo,  # arquivo especificado
                      delimiter=',',  # o que ira separar os dados -> delimitador
                      lineterminator='\n'  # qual era o ultimo elemento -> determinador de linha
                      )

    # intanciando o escritor e passando a função writerow (escrever em linha)
    escrever.writerow(
                     ['carlos', 'Brasil', '190']  # Os valores devem bater com o número de colunas
                     )
