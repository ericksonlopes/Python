from tkinter import *


class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self['bd'] = 'black'


print(help(MinhaFrame))  # documentação da minha class, com base no Frame do tkinter

# print(help(Frame))  # imprimira a ajuda que tens sobre a classe Frame
