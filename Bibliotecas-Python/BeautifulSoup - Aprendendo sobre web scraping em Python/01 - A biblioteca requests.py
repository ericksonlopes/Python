import requests
import bs4

page = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')

# imprime a solicitação de um response
print(page.status_code)

# imprime o código conte do site
print(page.content)

