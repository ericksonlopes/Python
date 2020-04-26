from tkinter import *

tela = Tk()
tela.title('009')

lbl1 = Label(tela, text='Este é o Label 1')
lbl2 = Label(tela, text='Este é o label 2')
botao = Button(tela, text='Este é o botão')

# pack 
lbl1.pack()
botao.pack()
lbl2.pack()

tela.mainloop()
