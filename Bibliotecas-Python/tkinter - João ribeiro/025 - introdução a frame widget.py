from tkinter import *

# ------------------------------
# Funções

# ------------------------------
# GUI
janela = Tk()
janela.title('022')
janela.geometry('500x500')
# ------------------------------
# WIDGETS
frame_login = Frame(janela)


label_usuario = Label(frame_login, text='Usuário: ')
label_senha = Label(frame_login, text='Senha: ')
txt_usuario = Entry(frame_login)
txt_senha = Entry(frame_login)
cmd_entrar = Button(frame_login, text='Entrar')

# ------------------------------
# LAYOUT
label_usuario.grid(row=0, column=0)
label_senha.grid(row=1, column=0)
txt_usuario.grid(row=0, column=1)
txt_senha.grid(row=1, column=1)
cmd_entrar.grid(row=2, column=1)

frame_login.grid()

janela.mainloop()

