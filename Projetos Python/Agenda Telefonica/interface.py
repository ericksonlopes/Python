# bibliotecas usadas
from tkinter import *


class Interface_gui(Frame):
    def __init__(self, janela=None):
        # cria uma frame principal
        Frame.__init__(self, janela)
        # título da janela
        self.master.title('AGENDA')

        # chama afunção que retorna o método geometry da janela, podendo definir seu tamanho e posicionando ao centro
        self.centralizar(500, 500)

        # travar redimensionamento da janela
        self.master.resizable(False, False)

        # estrutura de widgets da janela
        self.lista_contatos = Listbox(self.master)
        self.lbl_agenda = Label(self.master)
        self.btn_exibir = Button(self.master)
        self.btn_adicionar = Button(self.master)
        self.btn_remover = Button(self.master)
        self.btn_editar = Button(self.master)
        self.btn_sair = Button(self.master)
        self.lbl_versao = Label(self.master)

        # configurações de cada widgets
        self.conf_widgets()

    # funçao que retorna o método que configura posicionamento e tamanho da janela
    def centralizar(self, altura, largura):
        # variaveis com os valores da altura e largura do monitor
        largura_sistema = self.master.winfo_screenwidth()
        altura_sistema = self.master.winfo_screenheight()

        # calcula a posição de X e Y para exibir a janela no monitor
        pox_x = abs(int((altura / 2) - (largura_sistema / 2)))
        pos_y = abs(int((largura / 2) - (altura_sistema / 2)))

        # retorna o método geometry com as coordenadas
        return self.master.geometry(f'{altura}x{largura}+{pox_x}+{pos_y}')

    def conf_widgets(self):
        largura_btn = 20
        font = 'Arial 12'

        # label titulo agenda
        self.lbl_agenda['text'] = 'AGENDA TELEFÔNICA'
        self.lbl_agenda['font'] = 'Impact 30'
        self.lbl_agenda.pack()

        self.lista_contatos.pack()

        # exibir contatos
        self.btn_exibir['text'] = 'EXIBIR'
        self.btn_exibir['width'] = largura_btn
        self.btn_exibir['font'] = font
        self.btn_exibir['bg'] = '#C1CDCD'
        self.btn_exibir['command'] = lambda: print('exibir')
        self.btn_exibir.pack(pady=5)

        # Botao adicionar
        self.btn_adicionar['text'] = 'ADICIONAR'
        self.btn_adicionar['width'] = largura_btn
        self.btn_adicionar['font'] = font
        self.btn_adicionar['bg'] = '#C1CDCD'
        self.btn_adicionar['command'] = lambda: print('adicionar')
        self.btn_adicionar.pack(pady=5)

        # remover
        self.btn_remover['text'] = 'REMOVER'
        self.btn_remover['width'] = largura_btn
        self.btn_remover['font'] = font
        self.btn_remover['bg'] = '#C1CDCD'
        self.btn_remover['command'] = lambda: print('remover')
        self.btn_remover.pack(pady=5)

        # editar
        self.btn_editar['text'] = 'EDITAR'
        self.btn_editar['width'] = largura_btn
        self.btn_editar['font'] = font
        self.btn_editar['bg'] = '#C1CDCD'
        self.btn_editar['command'] = lambda: print('EDITAR')
        self.btn_editar.pack(pady=5)

        # sair
        self.btn_sair['text'] = 'Sair'
        self.btn_sair['width'] = largura_btn
        self.btn_sair['font'] = font
        self.btn_sair['bg'] = '#C1CDCD'
        self.btn_sair['command'] = lambda: self.master.quit()
        self.btn_sair.pack(pady=5)


        # label versao
        self.lbl_versao['text'] = 'V1.0'
        self.lbl_versao.pack()


if __name__ == '__main__':
    interface = Interface_gui()
    mainloop()
