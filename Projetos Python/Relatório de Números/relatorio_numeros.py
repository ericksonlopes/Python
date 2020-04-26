# -*- coding: utf-8 -*-
from funcoes_relatorio import *
from tkinter import *

# inicializa o tk nessa variavel
janela_principal = Tk()

# chama função que centraliza a janela e determina o tamanho
centralizar_janela(janela_principal, 600, 379)

# travar, redimencionamento
janela_principal.resizable(False, False)

# inserindo cor de fundo
janela_principal.config(bg=cor_fundo)

# Título da janela
janela_principal.title('RN - Relatório de Numeros')

# inseri os widgets preparados para página
widgets(janela_principal)

# chama a função de laço principal
janela_principal.mainloop()


