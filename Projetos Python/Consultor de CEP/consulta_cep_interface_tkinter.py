"""
O programa consiste em pegar o cep fornecido pelo usuário
e através da interface transmitir os dados recebediso de uma
API para visualização de quem esteja usando o programa
"""

from tkinter import *
from tkinter import messagebox
import requests


class Interface_Consulta(Frame):
    # widgets no Frame do master
    def __init__(self, master=None):
        # cria uma frame, no master principal
        Frame.__init__(self, master)

        # variavel com a fonte do sistema
        self.fonte = ''

        # variaveis que armazena os dados recebido da API
        self.string_cep = ''
        self.string_logradouro = ''
        self.string_bairro = ''
        self.string_localidade = ''
        self.string_complemento = ''

        # frame com widgets de pesquisa
        self.frm_pesquisa = LabelFrame(self)
        self.frm_pesquisa.grid(row=0, column=1, padx=10, pady=10, sticky='W')

        # botão e caixa de texto dentro da frm_pesquisa
        self.caixa_texto = Entry(self.frm_pesquisa)
        self.btn_pesquisa = Button(self.frm_pesquisa)
        # posicionamento do btn e caixa
        self.btn_pesquisa.grid(row=0, column=1, pady=10, padx=10)
        self.caixa_texto.grid(row=0, column=0, padx=10)

        # frame com widgets de resultados
        self.frm_resultados = Frame(self)
        self.frm_resultados.grid(row=1, column=0, columnspan=2, padx=10)

        # labels da frm_pesquisa
        self.lbl_cep = Label(self.frm_resultados)
        self.lbl_logradouro = Label(self.frm_resultados)
        self.lbl_bairro = Label(self.frm_resultados)
        self.lbl_localidade = Label(self.frm_resultados)
        self.lbl_complemento = Label(self.frm_resultados)
        # posicionamento das labels
        self.lbl_cep.grid(row=0, column=0, sticky='W')
        self.lbl_logradouro.grid(row=1, column=0, sticky='w', pady=5)
        self.lbl_bairro.grid(row=2, column=0, sticky='W', pady=10)
        self.lbl_localidade.grid(row=3, column=0, sticky='W', pady=10)
        self.lbl_complemento.grid(row=4, column=0, sticky='W', pady=10)

        # instancia a frame contendo todos os widgets na janela
        self.grid()

    def personaliza_widgets(self):
        # frm_pesquisa
        self.frm_pesquisa['text'] = 'Pesquisa'
        self.frm_pesquisa['font'] = f'{self.fonte} 12'
        # botão
        self.btn_pesquisa['text'] = 'Buscar'
        self.btn_pesquisa['font'] = f'{self.fonte} 12'
        self.btn_pesquisa['command'] = lambda: self.lista_info_cep()
        # caixa de texto
        self.caixa_texto['font'] = f'{self.fonte} 12'
        self.caixa_texto['justify'] = CENTER

        # frm_resultados
        labels_resultados = [self.lbl_logradouro,
                             self.lbl_bairro, self.lbl_localidade,
                             self.lbl_cep, self.lbl_complemento]

        # verifica cada item da lista e realiza uma ação
        for label in labels_resultados:
            # alterando fonte de texto de cada label
            label['font'] = f'{self.fonte} 16'

        self.lbl_cep['text'] = f'Cep: {self.string_cep}'
        self.lbl_logradouro['text'] = f'Logradouro: {self.string_logradouro}'
        self.lbl_bairro['text'] = f'Baixo: {self.string_bairro}'
        self.lbl_localidade['text'] = f'Localidade: {self.string_localidade}'
        self.lbl_complemento['text'] = f'Complemento: {self.string_complemento}'

    # cria classe contendo a interface e alguns de seus métodos e funções
    def lista_info_cep(self):
        if self.caixa_texto.get() != '':
            cep = ''.join(filter(lambda num: num.isnumeric(), self.caixa_texto.get()))
            dados_site = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

            if dados_site.status_code == 200:
                # lança os dados convertidos para um dicionario
                dicionario = dados_site.json()
                try:
                    self.string_cep = dicionario['cep']
                    self.string_logradouro = dicionario['logradouro']
                    self.string_bairro = dicionario['bairro']
                    self.string_localidade = dicionario['localidade']
                    if dicionario['complemento'] != '':
                        self.string_complemento = dicionario['complemento']
                    else:
                        self.string_complemento = 'Não há complemento'
                except KeyError:
                    messagebox.showinfo('Error', 'O CEP informado não pode ser encontrado'
                                                 '\nPor favor digite novamente um CEP válido')

                self.personaliza_widgets()

            else:
                # Exibe uma mensagem de erro
                messagebox.showinfo('Error', 'O CEP informado não pode ser encontrado'
                                             '\nPor favor digite novamente um CEP válido')
            self.caixa_texto.delete(0, END)
        else:
            # caso a caixa esteja vazia
            messagebox.showinfo('Erro', 'A caixa esta vazia! Não a referencia de CEP')

    # centraliza a janela ao centro da tela
    def centralizar_janela(self, altura, largura):
        # pega as informaçoes de altura e largura da tela
        so_altura = self.winfo_screenheight()
        so_largura = self.winfo_screenwidth()

        # realiza o calculo para saber as posições adequada
        posx = abs(int((altura / 2) - (so_altura / 2)))
        posy = abs(int((largura / 2) - (so_largura / 2)))

        # retorna uma função na qual se define a altura e largura da janela e sua posição
        return self.master.geometry(f'{altura}x{largura}+{posy}+{posx}')


# instancia a classe
interface = Interface_Consulta()

# ajustes da janela
interface.master.title('Consultar endereço com CEP')
interface.centralizar_janela(500, 350)
interface.master.resizable(False, False)

# fonte do programa
interface.fonte = 'Ebrima'

# exibe todos os widgets
interface.personaliza_widgets()

# chama a função principal de loop
mainloop()
