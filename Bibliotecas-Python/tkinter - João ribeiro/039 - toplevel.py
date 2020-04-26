from tkinter import *

janela = Tk()
janela.title('039')
janela.geometry('300x200')


def chamar():
    # toplevel # janela separada
    top = Toplevel()
    top.title('Novo formulário ')
    top.geometry('200x100')
    lbl1 = Label(top, text='Label na nova janela')
    lbl1.pack()


btn = Button(janela, text='Chamar aba', command=chamar)
btn.pack()
janela.mainloop()
