from tkinter import *

janela = Tk()

img = PhotoImage(file='imagens/img1.png')

label_imagem = Label(janela, image=img).pack()

janela.mainloop()
