# grid manager

from tkinter import *

janela = Tk()
janela.title('Login')

Label(janela, text='Usuário: ').grid(row=0, sticky=W)
Label(janela, text='Senha: ').grid(row=1, sticky=W)

text_usuario = Entry(janela).grid(row=0, column=1)
text_senha = Entry(janela).grid(row=1, column=1)

btn = Button(janela, text='Logar').grid(row=2, column=1, sticky=E)

janela.mainloop()
