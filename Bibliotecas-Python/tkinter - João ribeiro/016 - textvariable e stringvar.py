from tkinter import *

janela = Tk()
janela.title('012')
janela.geometry('500x200')

texto = StringVar()
texto.set('Novo texto')

label1 = Label(janela,
               font='Arial 20',
               bg='black',
               fg='white',
               textvariable=texto
               )

label1.pack()

label1 = Label(janela,
               font='Arial 20',
               bg='black',
               fg='white',
               textvariable=texto
               )

label1.pack()

label1 = Label(janela,
               font='Arial 20',
               bg='black',
               fg='white',
               textvariable=texto
               )

label1.pack()

label1 = Label(janela,
               font='Arial 20',
               bg='black',
               fg='white',
               textvariable=texto
               )

label1.pack()

# label1['text'] = 'Olá mundo'

janela.mainloop()
