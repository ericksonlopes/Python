from tkinter import *

janela = Tk()
janela.title('012')
janela.geometry('500x500')

border = 3  # tamanho de todas as bordar

label1 = Label(janela,
               text='borda \n solid',
               fg='black',
               font='Arial 20',
               bd=border,  # Tamanho da borda
               relief='solid',  # tipo da borda
               ).pack()

label2 = Label(janela,
               text='borda \n groove',
               fg='black',
               font='Arial 20',
               bd=border,  # Tamanho da borda
               relief='groove',  # tipo da borda
               ).pack()

label3 = Label(janela,
               text='borda \n flat',
               fg='black',
               font='Arial 20',
               bd=border,  # Tamanho da borda
               relief='flat',  # tipo da borda
               ).pack()

label4 = Label(janela,
               text='borda \n raised',
               fg='black',
               font='Arial 20',
               bd=border,  # Tamanho da borda
               relief='raised',  # tipo da borda
               ).pack()

label5 = Label(janela,
               text='borda \n sunken',
               fg='black',
               font='Arial 20',
               bd=border,  # Tamanho da borda
               relief='sunken',  # tipo da borda
               ).pack()

label6 = Label(janela,
               text='borda \n ridge',
               fg='black',
               font='Arial 20',
               bd=border,  # Tamanho da borda
               relief='ridge',  # tipo da borda
               ).pack()

janela.mainloop()
