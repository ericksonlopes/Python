from tkinter import *

menu_iniciar = Tk()
menu_iniciar.title('008')

# Dimensoes da janela
largura = 500
altura = 300

# Resolução do nosso sistema
largura_screen = menu_iniciar.winfo_screenwidth()
altura_screen = menu_iniciar.winfo_screenheight()

# posição da janela
posx = largura_screen/2 - largura/2
poxy = altura_screen/2 - altura/2

# definir a geometry
menu_iniciar.geometry(f'{largura}x{altura}+{int(posx)}+{int(poxy)}')

print(largura_screen, altura_screen)

menu_iniciar.mainloop()
