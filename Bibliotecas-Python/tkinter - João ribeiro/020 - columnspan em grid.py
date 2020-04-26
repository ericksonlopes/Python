from tkinter import *  # Importar tudo

janela = Tk()  # para inicar o tk
janela.title('aplicação teste')  # Nomear aba

Label(janela, width=20, text='Texto', fg='white', bg='black').grid()
Label(janela, width=20, text='Texto', fg='white', bg='green').grid(column=1)
Label(janela, width=20, text='Texto', fg='white', bg='pink').grid(column=2)
Label(janela, width=40, text='Texto', fg='white', bg='blue').grid(columnspan=3, sticky='WE')

janela.mainloop()  # iniciar interface
