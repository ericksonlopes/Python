from tkinter import *  # Importar tudo

menu_inicial = Tk()  # para inicar o tk
menu_inicial.title('aplicação teste')  # Nomear aba

menu_inicial.geometry('500x400+700+300')  # Tamanho do formulário
menu_inicial.resizable(True, True)  # Ajustar a largura e altura
# menu_inicial.resizable(0, 1)  # Podemos utilizar 0=False e 1=True

# menu_inicial.minsize(width=500, height=250)  # Valor minimo de redimensionamento
# menu_inicial.maxsize(700, 400)  # Valor maximo de redimensionamento

menu_inicial.state('zoomed')  # Maximizar
# menu_inicial.state('iconic')  # Minimizar

menu_inicial.iconbitmap('imagens/icon.ico')  # Mudar o icone

menu_inicial.mainloop()  # iniciar interface
