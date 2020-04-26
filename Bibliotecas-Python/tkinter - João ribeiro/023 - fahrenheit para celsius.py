from tkinter import *


# Funções
# C = (F-32) * 5/9
def calcular():
    F = float(textbox.get())
    C = (F-32) * 5/9
    varfinal.set(str(round(C, 1)) + ' Graus Celcios')


# GUI
janela = Tk()
janela.title('022')

varfinal = StringVar()

# WIDGETS
label1 = Label(janela, text='Graus em fahrenheit: ')
textbox = Entry(janela)
btn = Button(janela, text='Executar', command=calcular)
label_resultado = Label(janela, textvariable=varfinal)

# LAYOUT
label1.grid()
textbox.grid()
btn.grid()
label_resultado.grid()

janela.mainloop()
