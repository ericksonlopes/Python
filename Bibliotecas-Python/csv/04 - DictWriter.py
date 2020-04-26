from csv import DictWriter

with open('arquivos/empresario.csv', 'w', encoding='utf-8') as arquivo:
    # colas que a
    colunas = ['nome', 'clube sigla']

    # criando o cabeçalho
    escrever = DictWriter(arquivo,
                          fieldnames=colunas,  # - cabecalho
                          delimiter=',',  # - O que ira dividir os dados
                          lineterminator='\n'  # - ultimo elemento
                          )
    # escrevendo no arquivo o cabeçalho
    escrever.writeheader()

    # escrever em linhas, informando 
    escrever.writerow({'nome': 'Russo', 'clube sigla': 'SJe'})