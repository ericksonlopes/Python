from tkinter import *

janela = Tk()
janela.title('012')
janela.geometry('500x200')

tamanho_da_font = 20

label1 = Label(
    janela,
    text='Frase de teste\nFrase de teste',
    bd=1,
    font='Arial {}'.format(tamanho_da_font),
    relief='solid',
    width=20,
    height=7,  # Quantidade de linhas, em função do tamanho da fonte
    anchor=CENTER  # Centralzar texto
    ).pack()

janela.mainloop()
