from csv import DictReader

# Para ler um arquivo CSV com o DictReader pode não ter muita diferença do método reader.

with open('arquivos/lutadores.csv', 'r', encoding='utf-8') as arquivo_csv:
    # cria um objeto com o método que coloca os dados recebidos em um dicionário
    leitor = DictReader(arquivo_csv,  # dados do arquivo recebido
                        delimiter=','  # como os dados estão separados
                        )

    for coluna in leitor:
        print(coluna['Nome'])  # exibe somente os elementos de key -> "Nome"
