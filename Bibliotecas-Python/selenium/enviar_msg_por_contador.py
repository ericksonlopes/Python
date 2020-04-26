from selenium import webdriver
import time


class Irritar:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(15)

        conversa = self.driver.find_element_by_xpath('//span[@title="Pra jogar um lolzin"]')
        time.sleep(3)
        conversa.click()

        contador = 1

        while True:
            mensagem = f'{contador}° Mensagem'
            contador += 1

            caixa_texto = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(1)
            caixa_texto.click()

            caixa_texto.send_keys(mensagem)
            time.sleep(1)

            btn_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            time.sleep(1)
            btn_enviar.click()


bot = Irritar()

