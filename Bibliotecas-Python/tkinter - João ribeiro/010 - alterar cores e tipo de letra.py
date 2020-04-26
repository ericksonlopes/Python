from tkinter import *

tela = Tk()
tela.title('010')
tela.geometry('500x300')

label_1 = Label(tela,
                text='Este é o label1',  # texto
                bg='#FFCC99',  # Background
                fg='#6600FF',  # cor da letra
                font='Arial 20 bold italic')  # Fonte da letra / Tamanho da letra
label_1.pack()

label_2 = Label(tela,
                text='este é o label 2',
                bg='#99FFCC',
                fg='#6600CC',
                font='Verdana 42 bold')
label_2.pack()

tela.mainloop()
