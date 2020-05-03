def armazenar_contatos(**kwargs):
    with open('contatos.csv', 'a', encoding='utf-8') as arquivo_csv:
        arquivo_csv.write(','.join(kwargs.values())+'\n')
        print(kwargs.keys())
        print(kwargs.values())
        # flush -> função para escrever em disco na hora
        arquivo_csv.flush()


if __name__ == '__main__':
    armazenar_contatos(nome='erickson', email='ericskon@gmail.com', telefone='1194360487')
