# -*- coding: utf-8 -*-
# importa a biblioteca por inteira
from tkinter import *
from tkinter import messagebox
from math import sqrt
import os

# variaveis para estilo e cores da janela
cor_fundo = 'white'
cor_letra = 'black'
fonte = 'Arial 12'


# Soma algarismo para o resultado
def soma_algarismo(dado_recebido):
    def soma_alga(dado):
        # transforma os números que chegam em formado de string em inteiros, e coloca dentro de uma lista
        lista_numeros = list(map(lambda trans_num: int(trans_num),
                                 # retira os caracteres que não são números, equivale a lista
                                 # verificando se o caractere é do tipo numérico
                                 filter(lambda retira_num: retira_num.isnumeric(), str(dado))))
        # retorna a soma de cada elemento da lista
        return sum(lista_numeros)

    # variável usada para verificação
    final = soma_alga(dado_recebido)
    # enquanto final não for menor que 10, passa novamente sobre a função de soma
    while final >= 10:
        # tem que ser passada por string pois o código só aceita assim
        final = soma_alga(str(final))
    # se a variável final for menor que 10, contendo uma casa, é retornado o valor pela função
    return final


# Cria o relátório em um arquivo de texto
def cria_arquivo_relatorio(valor_radio, numero=0):
    def cria_arquivo():
        try:
            # cria e abre o arquivo para sua manipulação
            with open(caminho_arquivo, 'w', encoding='UTF-8') as arquivo:
                # escreve o numero
                arquivo.write(f'Número: {numero}\n\n')
                # raiz do número
                arquivo.write(f'Raiz: {sqrt(numero)}\n\n')
                # soma algarismo
                arquivo.write(f'Soma algarismo: {soma_algarismo(numero)}\n\n')
                if valor_radio == 2:
                    arquivo.write(f'Tabuada da adição:\n')
                    [arquivo.write(f'{numero:^3} + {num:^3} = {numero + num:^3}\n') for num in range(11)]
                elif valor_radio == 1:
                    arquivo.write(f'Tabuada da subtração:\n')
                    [arquivo.write(f'{numero:^3} - {num:^3} = {abs(numero - num):^3}\n') for num in range(11)]
                elif valor_radio == 0:
                    arquivo.write(f'Tabuada da adição:\n')
                    [arquivo.write(f'{numero:^3} x {num:^3} = {numero * num:^3}\n') for num in range(11)]
                elif valor_radio == 3:
                    arquivo.write(f'Tabuada da adição:\n')
                    [arquivo.write(f'{numero:^3} / {num:^3} = {numero / num:^3}\n') for num in range(1, 11)]
                arquivo.write('\n')
                arquivo.write('Divisores:\n')
                [arquivo.write(f'{num}\n') for num in range(1, numero + 1) if numero % num == 0]

        # caso aconteça um erro
        except:
            messagebox.showinfo('Error', 'O Arquivo não pode ser criado')
        # se o arquivo for criado
        else:
            messagebox.showinfo('Criado', 'Relatório Criado com sucesso!')
    # converte o núemro para string
    numero = int(numero)
    valor_radio = int(valor_radio)

    # pega o caminho atual do código python, e adiciona um diretorio para os relatórios
    caminho_pasta = os.path.join(os.getcwd(), 'save_relatorios')
    caminho_arquivo = os.path.join(caminho_pasta, f'{str(numero)}.txt')

    # Caso a pasta não exista ele cria
    if not os.path.exists(caminho_pasta):
        # cria a pasta no diretória inserido
        os.mkdir(caminho_pasta)
        messagebox.showinfo('Pasta', 'Primeiro uso do aplicativo\n'
                                     'Por favor, execute novamente a ação')

    # if not os.path.exists(f'{caminho_pasta}/{str(numero)}.txt')
    fazer_quest = messagebox.askyesno('Criar', f'Deseja criar o relátorio com o número {str(numero)}')

    # se a resposta para criação do arquivo for True..
    if fazer_quest:
        # apenas números diferentes de 0
        if numero != 0:
            # se caso o arquivo não exista
            if not os.path.exists(caminho_arquivo):
                # executa a função que cria
                cria_arquivo()
            # Caso o arquivo ja exista exibe essa mensagem
            else:
                sbcv_quest = messagebox.askyesno('Informa', 'O arquivo ja existe, Deseja sobrescrever?')
                if sbcv_quest:
                    cria_arquivo()
        # caso o numero seja 0 o sistema exibe essa mensagem
        else:
            messagebox.showinfo('Informa', 'O programa não cria um relatório com o número 0')


# função para centralizar a janela ao centro da tela, e determina o tamanho da página
def centralizar_janela(janela, altura, largura):
    # pega a altura do monitor usado
    altura_sistema = janela.winfo_screenheight()
    # pega a largura do monitor usado
    largura_sistema = janela.winfo_screenwidth()

    # calculo para saber a posição exata de x
    pos_x = int((largura_sistema / 2) - (largura / 2))
    # calculo apra saber a posição exata de y
    pos_y = int((altura_sistema / 2) - (altura / 2))

    # retorna a outra função que determina as proporções e alinhamento
    return janela.geometry(f"{altura}x{largura}+{pos_x}+{pos_y}")


# cria todos os widgets
def widgets(janela):
    def preenche_com_dados():
        # Pega o valor de dentro da spinbox(caixa_gira)
        numero = int(caixa_gira.get())

        # label raiz -> inserindo dados
        label_raiz['text'] = f'Raiz: {sqrt(numero)}'
        # label soma algarismo
        label_soma_alg['text'] = f'Soma do algarismo: {soma_algarismo(numero)}'

        # verifica o valor dentro da spinbox, se for igual a '' ele transforma o numero em 0
        if numero == '':
            numero = 1

        # limpa a lista_calculos
        lista_calculos.delete(0, END)
        # limpa lista_soma_res
        lista_soma_res.delete(0, END)
        # limpa lista divisores
        lista_divisores.delete(0, END)

        # adicionando itens nas Listbox
        # lista divisores
        [lista_divisores.insert(END, f'{num}') for num in range(1, numero + 1) if numero % num == 0]

        # lista calculos e soma_res
        if valor_rb.get() == 2:
            label_calculos['text'] = f'Operador: Adição'
            [lista_calculos.insert(END, f'{numero:^3} + {num:^3} = {numero + num:^3}') for num in range(1, 11)]
            [lista_soma_res.insert(END, f'{numero + num} > {(soma_algarismo(numero + num)):^3}') for num in
             range(1, 11)]

        elif valor_rb.get() == 1:
            label_calculos['text'] = f'Operador: Subtração'
            [lista_calculos.insert(END, f'{numero:^3} - {num:^3} = {abs(numero - num):^3}') for num in
             range(1, 11)]
            [lista_soma_res.insert(END, f'{abs(numero - num):^3} > {abs((soma_algarismo(numero - num))):^3}') for num
             in
             range(1, 11)]

        elif valor_rb.get() == 0:
            label_calculos['text'] = f'Operador: Multiplicação'
            [lista_calculos.insert(END, f'{numero:^3} x {num:^3} = {numero * num:^3}') for num in range(1, 11)]
            [lista_soma_res.insert(END, f'{numero * num:^3} > {(soma_algarismo(numero * num)):^3}') for num in
             range(1, 11)]

        elif valor_rb.get() == 3:
            label_calculos['text'] = f'Operador: Divisão'
            [lista_calculos.insert(END, f'{numero:^3} / {num:^3} = {numero / num:^3}') for num in range(1, 11)]
            [lista_soma_res.insert(END, f'{numero / num:^3} > {(soma_algarismo(numero / num)):^3}') for num in
             range(1, 11)]

    # Frame para organizar tudo em apenas um lugar ------------------------------------------------

    # variaveis var para armazenamento de dado
    valor_rb = IntVar()  # para radiobutton

    # faz a frame aparecer dentro da janela
    frm_conteudo = Frame(janela).grid()

    # Frame de widgets para pesquisa
    frm_pesquisa = Frame(frm_conteudo, bg=cor_fundo)
    btn_pesquisa = Button(frm_pesquisa, text='Buscar', font=fonte, command=preenche_com_dados)
    caixa_gira = Spinbox(frm_pesquisa, font=fonte, width=5, wrap=True, justify=CENTER,
                         from_=0, to=99999, command=preenche_com_dados)

    # posicionamento
    frm_pesquisa.grid(row=0, column=0, pady=15)
    btn_pesquisa.grid(row=0, column=0)
    caixa_gira.grid(row=1, column=0, pady=5)

    # Frame conteudo os widgets de resultados -----------------------------------------------------
    frm_resultados = LabelFrame(frm_conteudo, bg=cor_fundo)

    # labels de informação
    label_raiz = Label(frm_resultados, text='Raiz: ',
                       bg=cor_fundo, fg=cor_letra, font=fonte)
    label_soma_alg = Label(frm_resultados, text='Soma do algarismo: ',
                           bg=cor_fundo, fg=cor_letra, font=fonte)
    # labels das listas
    label_calculos = Label(frm_resultados, text='operador: ',
                           bg=cor_fundo, fg=cor_letra, justify=CENTER, font=fonte)
    label_soma_res = Label(frm_resultados, text='Soma resultado',
                           bg=cor_fundo, fg=cor_letra, justify=CENTER, font=fonte)
    label_divisores = Label(frm_resultados, text='divisores',
                            bg=cor_fundo, fg=cor_letra, justify=CENTER, font=fonte)
    # listas
    lista_calculos = Listbox(frm_resultados, width=28,
                             bg=cor_fundo, fg=cor_letra, justify=CENTER, font=fonte)
    lista_soma_res = Listbox(frm_resultados, width=27,
                             bg=cor_fundo, fg=cor_letra, justify=CENTER, font=fonte)
    lista_divisores = Listbox(frm_resultados, width=10,
                              bg=cor_fundo, fg=cor_letra, justify=CENTER, font=fonte)

    # posicionamento
    frm_resultados.grid(row=1, column=0, columnspan=2)
    label_raiz.grid(row=0, column=0, ipady=10)
    label_soma_alg.grid(row=0, column=1, columnspan=2)
    label_calculos.grid(row=1, column=0, pady=10)
    label_soma_res.grid(row=1, column=1)
    label_divisores.grid(row=1, column=2)
    lista_calculos.grid(row=2, column=0)
    lista_soma_res.grid(row=2, column=1)
    lista_divisores.grid(row=2, column=2)

    frm_operadores = Frame(frm_conteudo, bg=cor_fundo)
    # Label dos radiobuttons
    label_soma_r = Label(frm_operadores, text='+', bg=cor_fundo, fg=cor_letra, font=fonte)
    label_subtracao_r = Label(frm_operadores, text='-', bg=cor_fundo, fg=cor_letra, font=fonte)
    label_multiplica_r = Label(frm_operadores, text='*', bg=cor_fundo, fg=cor_letra, font=fonte)
    label_div_r = Label(frm_operadores, text='/', bg=cor_fundo, fg=cor_letra, font=fonte)
    # radiobuttons
    radio_soma = Radiobutton(frm_operadores, value=2, bg=cor_fundo, fg=cor_letra,
                             variable=valor_rb, command=lambda: preenche_com_dados())
    radio_subtracao = Radiobutton(frm_operadores, value=1, bg=cor_fundo, fg=cor_letra,
                                  variable=valor_rb, command=lambda: preenche_com_dados())
    radio_multiplica = Radiobutton(frm_operadores, value=0, bg=cor_fundo, fg=cor_letra,
                                   variable=valor_rb, command=lambda: preenche_com_dados())
    radio_div = Radiobutton(frm_operadores, value=3, bg=cor_fundo, fg=cor_letra,
                            variable=valor_rb, command=lambda: preenche_com_dados())

    # posicionamento
    frm_operadores.grid(row=0, column=1)
    # labels
    label_soma_r.grid(row=0, column=0)
    label_subtracao_r.grid(row=0, column=1)
    label_multiplica_r.grid(row=0, column=2)
    label_div_r.grid(row=0, column=3)
    # radios
    radio_soma.grid(row=1, column=0)
    radio_subtracao.grid(row=1, column=1)
    radio_multiplica.grid(row=1, column=2)
    radio_div.grid(row=1, column=3)

    # menu
    menu = Menu(janela)
    # adicionando menu dentro da janela
    relatorio = Menu(menu, tearoff=0)
    # cria uma label clicavel
    relatorio.add_command(label='Criar Relatório',
                          command=lambda: cria_arquivo_relatorio(valor_rb.get(), caixa_gira.get()))
    menu.add_cascade(label='Salvar relatório', menu=relatorio)
    # coloca na janela o menu pedido
    janela.config(menu=menu)

    # executa essa função para preencher
    preenche_com_dados()


if __name__ == '__main__':
    # cria_arquivo_relatorio()
    # # exibe uma mensagem dizendo que o arquivo foi criado
    # criado_quest = messagebox.askyesno('criado', 'Arquivo criado com sucesso\nDeseja Abrir o arquivo?')
    # if criado_quest:
    #     os.system(caminho_arquivo)
    pass
