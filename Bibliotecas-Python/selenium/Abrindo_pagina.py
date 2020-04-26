# instalar a biblioteca -> pip install selenium
# e faça o download do chromedriver para utilizarmos

# importe a biblioteca para utilização do selenium, usando o módulo webdriver
from selenium import webdriver
import time


# crie a classe
class AbrirPagina:
    def __init__(self):
        # insira o caminho do seu webdriver, crie um objeto que irá executar suas funções
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

        # Abrir uma página com .get('')
        self.driver.get('https://www.youtube.com/')

        # dar um tempo para página ficar aberta
        time.sleep(5)

        # fechar a paginá
        self.driver.close()


# instâncie a classe
bot = AbrirPagina()