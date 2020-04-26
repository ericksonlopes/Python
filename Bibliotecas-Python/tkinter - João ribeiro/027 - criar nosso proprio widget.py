from tkinter import *


# Funções

# o meu widget
class FrameNome(Frame):  # indica o que fazer com os frames
    def __init__(self, ajanela):
        super().__init__()  # inicia a função de cima
        self['height'] = 150  # define a altura
        self['width'] = 200  # define a largura
        self['bd'] = 2  # borda e tamanho dela
        self['relief'] = 'solid'  # tipo da borda

        label_nome = Label(self, text='nome: ')
        text_nome = Entry(self)
        label_nome.grid(row=0, column=0)
        text_nome.grid(row=0, column=1)


# GUI
janela = Tk()
janela.title('022')

# WIDGETS

# LAYOUT

frame1_nome_1 = FrameNome(janela).grid()
frame1_nome_2 = FrameNome(janela).grid()
frame1_nome_3 = FrameNome(janela).grid()
frame1_nome_4 = FrameNome(janela).grid()


janela.mainloop()
