from tkinter import *


def cmd_Click(mensagem):  # Função do botão
    print(mensagem)


menu_inicial = Tk()
menu_inicial.geometry('500x400+500+400')
menu_inicial.title('Aula 6')

cmd1 = Button(menu_inicial, text='Executar', command=lambda: cmd_Click('Daniel?Moulo'))
cmd1.pack()

cmd2 = Button(menu_inicial, text='Clicar', command=lambda: print([num for num in range(4)]))
cmd2.pack()

menu_inicial.mainloop()

