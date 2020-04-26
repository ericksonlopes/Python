from tkinter import *

tela = Tk()
tela.title('011')
# tela.geometry('500x500')

label_1 = Label(tela,
                text='Este é o label 1',
                bg='red',
                font='Arial 10',
                width=50
                ) 

label_1.pack()

tela.mainloop()
