from bs4 import BeautifulSoup
import requests

# faz o requerimento a página
pagina = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

# inserindo ao BeautifulSoup a página que iremos usar
soup = BeautifulSoup(pagina.content, 'html.parser')

# imprimir de forma organizada, formatado corretamente
print(soup.prettify(), '\n'*2)

