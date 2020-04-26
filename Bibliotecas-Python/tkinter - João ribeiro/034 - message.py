from tkinter import *

janela = Tk()
janela.title('034')
janela.geometry('200x200')

t = Message(janela, text='este é o texto do message widget.', width=50)
t.pack()

janela.mainloop()
