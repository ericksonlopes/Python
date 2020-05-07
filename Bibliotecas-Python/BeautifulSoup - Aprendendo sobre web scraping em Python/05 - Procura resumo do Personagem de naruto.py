import requests
from bs4 import BeautifulSoup


class NarutoAPI:
    def __init__(self, pesquisa):
        self.pagina = requests.get('https://naruto.fandom.com/pt-br/wiki/' + pesquisa.lower())
        if self.pagina.status_code == 200:
            print('sucesso ao encontrar a página')
            soup = BeautifulSoup(self.pagina.content, 'html.parser')

            nome_personagem = soup.find(class_="page-header__title").get_text()
            lista = []
            for item in soup.find_all('p'):
                personagem = item.get_text()
                lista.append(personagem.strip('\n'))
            else:
                for item in lista:
                    if nome_personagem in item:
                        print(item)
                        break
        else:
            print('erro ao encontrar a página', pesquisa)


if __name__ == '__main__':
    NarutoAPI('naruto')
