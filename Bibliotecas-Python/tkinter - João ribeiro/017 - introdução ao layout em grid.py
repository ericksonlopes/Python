# grid manager

from tkinter import *

janela = Tk()
janela.title('017')
janela.geometry('500x500')

label1 = Label(janela, text="label1", bg='red', font='Arial 20')
label2 = Label(janela, text="label2", bg='green', font='Arial 20')
label3 = Label(janela, text="label3", bg='blue', font='Arial 20')

btn1 = Button(janela, text='Clique1')
btn2 = Button(janela, text='Clique2')
btn3 = Button(janela, text='Clique2')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)

janela.mainloop()
