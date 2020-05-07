"""
Definindo Funções

-Funções são pequenos trechos que realizam tarefas específicas;
-Pode ou não receber entrada e saída de dados;
-Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: se codar um função muito grande tente simplifica-la

já utilizamos varias funções desde que começamos o curso.
-print()
-len()
-Max()
...
"""

# exemplo de utilização de funções

# cores = ['Verde', 'Amarelo', 'Azul', 'Vermelho']

# utilizando a função integrada do python (built - in)
# print(cores)
# cores.append('x')

# DRY Don't Repeat Yourself - Não repita você mesmo/ Não repita seu código use funções

# como definir funções
"""
def nome_da_função(parametros_de_entrada):
    Bloco_da_função
    
nome da função -> sempre em minúsculo, e se for composto, separado por underline7
parâmetros de entrada -> opcionais, onde mais de um, cada um separado por vírgula, podendo ser opcionais ou nao
bloco da função - Onde ocorre o processamento da função
"""

# Definindo primeira função


def diz_oi():
    print('oi')


diz_oi()

"""
1 - Dentro das nossas funções podemos utilizar outras funções (nessa caso o print)
"""

# dizer oi 5 vezes

for v in range(5):
    diz_oi()

# Podemos criar variáveis com o tipo de uma função, e executar essa função através da variável
