from tkinter import *


class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self['height'] = 120
        self['width'] = 200
        self['bg'] = 'green'


janela = Tk()

frm = MinhaFrame(janela).grid()

janela.mainloop()
