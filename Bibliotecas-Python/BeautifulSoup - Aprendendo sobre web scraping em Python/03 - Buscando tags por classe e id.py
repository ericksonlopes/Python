from bs4 import BeautifulSoup
import requests

pagina = requests.get('http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html')

soup = BeautifulSoup(pagina.content, 'html.parser')

# Buscando por tag com a classe
print(soup.find_all('p', class_='outer-text'), '\n'*3)

# Buscando por qualquer tag com a classe especificada
print(soup.find_all(class_='outer-text'), '\n'*3)

# Buscando tag com o id
print(soup.find_all(id='first'), '\n'*3)

texto = soup.find(class_='outer-text').get_text()
print('encontrado: ', texto.strip())