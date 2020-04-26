from tkinter import *

janela = Tk()
janela.title('012')
janela.geometry('500x200')

label1 = Label(janela,
               text='Frase de teste\nteste\nteste\ndfdfgdf',
               font='Arial 20',
               bd=1,
               relief='solid',
               width=20,
               height=5,
               justify=LEFT,
               anchor=W)
label1.pack()

# label1 = Label(janela,
#                text='Frase de teste\nteste\nteste',
#                font='Arial 20',
#                bd=1,
#                relief='solid',
#                pady=50,
#                padx=50,
#                justify=RIGHT)
# label1.pack()

janela.mainloop()
