from tkinter import *


def mostrar_nome():
    nome = txtbox1.get()
    label_final = Label(janela, text='O teu nome é: ' + nome)
    label_final.grid()


# GUI
janela = Tk()
janela.title('021')
janela.geometry('200x100')

# criar os widgets
label1 = Label(janela, text='Escreve seu nome: ')
txtbox1 = Entry(janela)
btn1 = Button(janela, text='Executar', command=mostrar_nome)

# Organizar os widgets
label1.grid()
txtbox1.grid()
btn1.grid()

txtbox1.focus()

janela.mainloop()
