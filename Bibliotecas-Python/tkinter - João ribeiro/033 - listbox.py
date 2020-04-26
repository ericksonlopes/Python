from tkinter import *


def apagar():
    lista.delete(0, END)


def executar():
    print(lista.get(ACTIVE))


janela = Tk()
janela.resizable(False, False)


lista = Listbox(janela,
                justify=CENTER,  # Deixando letras ao centro
                height=20,  # tamanho da lista
                width=20,  # largura da lista
                )
lista.pack()

btn = Button(janela, text='Click', command=executar).pack()

Button(janela, text="Apagar", command=lambda: apagar()).pack()  # btn para apagar a lsita completa
# inserir um item de cada vez do tipo string
numeros = [num for num in range(1, 21)]
[lista.insert(END, str(num)) for num in numeros]

janela.mainloop()
