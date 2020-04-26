from tkinter import *

janela = Tk()
janela.title('Primeira aplicação')
janela.geometry('300x300')

texto = StringVar()

label = Label(janela, text='Mude clicando no botão', textvariable=texto)
label.pack()


def muda():
    texto.set('texto mudado')


btn = Button(janela, text='Mudar', command=muda)
btn.pack()
janela.mainloop()
