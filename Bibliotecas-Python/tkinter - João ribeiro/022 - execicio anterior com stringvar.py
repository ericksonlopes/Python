from tkinter import *


# Funções
def mostrar_nome():
    textovar.set(txt.get())


# GUI
janela = Tk()
janela.title('022')

textovar = StringVar()

# WIDGETS
label = Label(janela, text='O teu nome é: ')
txt = Entry(janela)
btn = Button(janela, text='Executar', command=mostrar_nome)

label2 = Label(janela, textvariable=textovar)
label23 = Label(janela, textvariable=textovar)
label24 = Label(janela, textvariable=textovar)

# LAYOUT
label.grid()
txt.grid()
btn.grid()
label2.grid()
label23.grid()
label24.grid()

janela.mainloop()
