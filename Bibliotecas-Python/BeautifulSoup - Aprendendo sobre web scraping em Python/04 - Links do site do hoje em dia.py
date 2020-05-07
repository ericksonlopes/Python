from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.hojeemdia.com.br/')

soup = BeautifulSoup(page.text, 'html.parser')

lista_link = soup.find_all('a', class_='teaser-link')
for item in lista_link:
    print(item.get_text())