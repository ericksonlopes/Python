from tkinter import *

janela = Tk()


def executar():
    print('Salvo')


janela.title('038')
janela.geometry('300x200')

meuMenu = Menu(janela)
fileMenu = Menu(meuMenu, tearoff=0)

fileMenu.add_command(label='Novo')
fileMenu.add_command(label='Abrir')
fileMenu.add_separator()
fileMenu.add_command(label='Salvar', command=executar)
meuMenu.add_cascade(label='file', menu=fileMenu)

editMenu = Menu(meuMenu, tearoff=0)
editMenu.add_command(label='Ajutas')
editMenu.add_separator()
editMenu.add_command(label='editar arquivos')
meuMenu.add_cascade(label='edit', menu=editMenu)

janela.config(menu=meuMenu)


janela.mainloop()
