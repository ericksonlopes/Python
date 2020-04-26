from tkinter import *

menu_iniciar = Tk()
menu_iniciar.title('Botão')
menu_iniciar.iconbitmap('imagens/botao.ico')
menu_iniciar['bg'] = 'pink'
menu_iniciar.geometry('500x400+500+400')

# botão
btn = Button(menu_iniciar, text='Executar')
btn.pack()

menu_iniciar.mainloop()
