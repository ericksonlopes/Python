# chama biblioteca
from selenium import webdriver
import time


class ClicaPagina:
    def __init__(self):
        # caminho do chromedriver
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

        # especificar site para abrir
        self.driver.get('https://www.youtube.com/')

    def clicar_menu(self):
        # especificar o caminho ou nome identificando
        menu_xpath = 'guide-icon'

        # procurando elemento na página
        menu_guia = self.driver.find_element_by_id(menu_xpath)
        time.sleep(3)

        # clicar no elemento indicado
        menu_guia.click()

    def clicar_jogos(self):
        jogos_class = '/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-g' \
                      'uide-renderer/div[1]/ytd-guide-section-renderer[3]/div/ytd-guide-entry-renderer[3]/a/paper-item'

        jogos = self.driver.find_element_by_xpath(jogos_class)
        time.sleep(3)

        jogos.click()


# instancie a classe
bot = ClicaPagina()
bot.clicar_menu()
bot.clicar_jogos()
