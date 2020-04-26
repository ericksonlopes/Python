from tkinter import *


class MinhaFrame(Frame):
    def __init__(self, tela):  # Formula do frame
        super().__init__()  # inicia a forma

        self.text1_text = StringVar()  # stringvar que armazena a informação do Entry
        self.label1_text = StringVar()  # string var para armazenar informação e exibir na label

        self['bd'] = 5
        self['relief'] = 'solid'
        self['bg'] = 'green'

        # Widget
        self.label1 = Label(self,
                            textvariable=self.label1_text,
                            bg='green', fg='black').grid()  # cria a label no grid do frame

        text1 = Entry(self, textvariable=self.text1_text,
                           bg='green', justify=CENTER).grid()  # cria a textbox no grid do frame

        cmd1 = Button(self, text='Click',
                      bg='green',
                      command=self.Executar).grid()  # cria o botão no grid do frame e chama função

    def Executar(self):  # função diparada pelo botão
        # joga dentro da variavel da label o texto da variavel do  Entry
        self.label1_text.set('Olá ' + self.text1_text.get())


janela = Tk()
janela.title('030')
janela.geometry('200x200')

frame = MinhaFrame(janela).grid()  # cria frame com a classe e coloca dentro do grid

janela.mainloop()
