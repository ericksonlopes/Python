# Formatação de string
# a utilizar a função format() permite formatar partes da string
nome = 'João'
frase_final = 'Olá {}'
print(frase_final.format(nome))

# colocando duas casas decimais pós virgula
preco = 10
print('R$ {:.2f}'.format(preco))

# alterando ordem dos argumentos
nome1 = "Joap"
nome2 = 'Marius'
frase_final = 'foram identificados {1} e {0}'
print(frase_final.format(nome1, nome2))  # O format() cria uma tupla possibilitando alterar sua ordem

# definir indices com string
nome1 = "Joap"
nome2 = 'Marius'
frase_final = 'foram identificados {a} e {b}'
print(frase_final.format(a=nome1, b=nome2))  # O format() cria uma tupla possibilitando alterar sua ordem

