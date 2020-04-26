from tkinter import *

# Funções

# GUI
janela = Tk()
janela.title('022')

# WIDGETS
frame_nome = Frame(janela)
frame_morada = Frame(janela)

label_nome = Label(frame_nome, text='Nome: ')
label_apelido = Label(frame_nome, text='apelido: ')
label_rua = Label(frame_morada, text='Rua: ')
label_cidade = Label(frame_morada, text='Cidade: ')

text_nome = Entry(frame_nome)
text_apelido = Entry(frame_nome)
text_rua = Entry(frame_morada)
text_cidade = Entry(frame_morada)

cmd_salvar = Button(janela, text='Executar')

# LAYOUT
# frame nome
label_nome.grid(row=0, column=0)
label_apelido.grid(row=1, column=0)
text_nome.grid(row=0, column=1)
text_apelido.grid(row=1, column=1)

# frame morada
label_rua.grid(row=0, column=0)
label_cidade.grid(row=1, column=0)
text_rua.grid(row=0, column=1)
text_cidade.grid(row=1, column=1)

# janela
frame_nome.grid(row=0, column=0)
frame_morada.grid(row=0, column=1)
cmd_salvar.grid(row=2, column=1)

janela.mainloop()
