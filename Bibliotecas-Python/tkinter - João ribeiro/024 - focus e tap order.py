from tkinter import *

janela = Tk()

janela.title("021")


# frunções
def executar():
    l1['text'] = t1.get()
    l2['text'] = t2.get()
    l3['text'] = t3.get()


# Widgets
t1 = Entry(janela)
t2 = Entry(janela)
t3 = Entry(janela)

l1 = Label(janela)
l2 = Label(janela)
l3 = Label(janela)
b = Button(janela, text='executar', command=executar)

# Layuot

t1.grid()
t2.grid()
t3.grid()


l1.grid()
l2.grid()
l3.grid()
b.grid()

t1.focus()

janela.mainloop()
