from tkinter import *


def fun(n):
    if n:
        label2['text'] = 'Acionei a função'
        label2['font'] = 'Cambria 20'
        for item in label2.keys():
            print(item, ' : ', label2[item])
    else:
        label2['text'] = 'frase de teste'
        label2['font'] = 'Calibri 20'
        for item in label2.keys():
            print(item, ' : ', label2[item])


janela = Tk()
janela.title('012')
janela.geometry('500x200')

label1 = Label(janela,
               text='frase de teste',
               font='Arial 20',
               bd=1,
               relief='solid',
               )
label1.pack()

label2 = Label(janela)
label2['text'] = [num for num in range(0, 10, 2)]
label2['font'] = 'Arial 20'
label2['bd'] = 1
label2['relief'] = 'solid'
label2.pack()

btn1 = Button(janela, text='prosseguir', command=lambda x=1: fun(x)).pack()
btn2 = Button(janela, text='voltar', command=lambda x=0: fun(x)).pack()

# print(label1['font'])  # mostra o que foi definido na fonte
# print(label2.keys())  # Visualiza todas as chaves que podem ser usadas

# for item in label2.keys():
#     print(item, ' : ', label2[item]) # Visualizar quais chaves estão sendo usadas e seus valores

janela.mainloop()


