from tkinter import *

janela = Tk()
janela.title('')
janela.geometry('300x200')

slide = Scale(janela,
              from_=0,
              to=20,
              # resolution=0.7,
              width=20,
              orient=HORIZONTAL,
              )
slide.pack()


def vervalor():
    print(slide.get())


cmd = Button(janela, text='Ver Valor', command=vervalor)
cmd.pack()

janela.mainloop()

# # Intimamente em contado com o Scale
# def vervalor(x):
#     print(x)
#
#
# slide = Scale(janela,
#               from_=0,
#               to=20,
#               # resolution=0.7,
#               width=20,
#               orient=HORIZONTAL,
#               command=vervalor,
#               )
# slide.pack()
