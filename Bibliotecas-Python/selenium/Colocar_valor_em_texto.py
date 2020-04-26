from selenium import webdriver
import time


class Colocar_valor:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get('https://www.youtube.com/')

    def pesquisar_YT(self, pesquisa):
        time.sleep(3)
        # caminho caixa de texto
        url_caixa = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/div'
        url_12347 = '//*[@id="container"]'

        # procurando a caixa
        txt = self.driver.find_element_by_xpath(url_12347)
        time.sleep(1)

        # clicar na caixa de texto
        txt.click()
        time.sleep(1)

        frase_chave = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/div/div[1]/div/div[2]/input'
        input_pesquisa = self.driver.find_element_by_xpath(frase_chave)
        # colocar string no input
        input_pesquisa.send_keys('Universo interior')

        # caminho botão
        btn_pesquisar = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/button'

        # procurar botão
        self.driver.find_element_by_xpath(btn_pesquisar).click()

        time.sleep(3)
        # procurar canal
        url_canal = '//*[@id="info"]'
        self.driver.find_element_by_xpath(url_canal).click()


bot = Colocar_valor()
bot.pesquisar_YT('Universo Interior')
