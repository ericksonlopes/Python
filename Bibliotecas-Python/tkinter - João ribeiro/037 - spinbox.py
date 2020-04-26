from tkinter import *
janela = Tk()
janela.title('037')
janela.geometry('300x200')


def valor():
    print(Spinbox.get(s1))


s1 = Spinbox(janela, from_=1, to=10, width=5, command=valor, justify=CENTER, wrap=True)
s1.pack()

s2 = Spinbox(janela, value=[num for num in range(0, 20, 2)], justify=CENTER)
s2.pack()

s3 = Spinbox(janela, value=[num for num in 'Erickson'], justify=CENTER)
s3.pack()

cmd = Button(janela, text="Executar")

janela.mainloop()
