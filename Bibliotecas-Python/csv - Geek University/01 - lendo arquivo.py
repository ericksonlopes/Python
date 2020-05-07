from csv import reader

# faz uma busca pelo arquivo e abre em modo leitura
with open('arquivos/lutadores.csv', 'r', encoding='utf-8') as arquivo_csv:
    # declara o método reader(ler) e cria uma lista com os dados recebidos do arquivo
    leitor = reader(arquivo_csv,  # - arquivo com os dados
                    delimiter=','  # - define o que ira separar os dados recebidos
                    )

    for coluna in leitor:
        print(coluna)