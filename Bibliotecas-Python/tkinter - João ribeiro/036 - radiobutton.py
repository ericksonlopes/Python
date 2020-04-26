from tkinter import *


def valor():
    print(valor_a.get())


def fui_selecionado():
    if valor_a.get() == 1:
        print('opção 1')
    elif valor_a.get() == 2:
        print('opção 2')
    elif valor_a.get() == 3:
        print('opção 3')


janela = Tk()
janela.title('035')

frameA = Frame(janela)
frameA.pack()
frameB = Frame(janela)
frameB.pack()

valor_a = IntVar()

va_1 = Radiobutton(frameA, text='Opção 1', variable=valor_a, value=1, command=fui_selecionado, indicatoron=0)
va_2 = Radiobutton(frameA, text='Opção 2', variable=valor_a, value=2, command=fui_selecionado, indicatoron=0)
va_3 = Radiobutton(frameA, text='Opção 3', variable=valor_a, value=3, command=fui_selecionado, indicatoron=0)
btn = Button(frameA, text='Executar', command=valor)

va_1.pack()
va_2.pack()
va_3.pack()
btn.pack()

vb_1b = Radiobutton(frameB, text='Opção 1', variable=valor_a, value=1, command=fui_selecionado, indicatoron=0)
vb_2b = Radiobutton(frameB, text='Opção 2', variable=valor_a, value=2, command=fui_selecionado, indicatoron=0)
vb_3b = Radiobutton(frameB, text='Opção 3', variable=valor_a, value=3, command=fui_selecionado, indicatoron=0)
btn = Button(frameB, text='Executar', command=valor)

vb_1b.pack()
vb_2b.pack()
vb_3b.pack()
btn.pack()

va_1.select()

janela.mainloop()
