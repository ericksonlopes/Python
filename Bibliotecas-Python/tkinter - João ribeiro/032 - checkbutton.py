from tkinter import *


# Funções

def executar():
    if valor_checkbutton.get() == 0:
        print('Foi desativado')
    elif valor_checkbutton.get() == 1:
        print('Foi ativo')


# GUI
janela = Tk()
janela.title('032')

valor_checkbutton = IntVar()

check = Checkbutton(janela,
                    text='Esta é nossa aplicação!',
                    variable=valor_checkbutton,
                    command=executar
                    ).pack()

print(valor_checkbutton)

janela.mainloop()
