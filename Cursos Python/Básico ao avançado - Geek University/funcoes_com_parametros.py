"""
Funções com parâmetro

- funções que recebem dados para serem processados dentro da mesma:

todo programa geralmente tem = Entrada -> processamento - > saída

alguns:
    não possuem entrada;
    Não possuem saída;
    possem entrada mas não saída;
    não possuem entrada mas possuem saida;
    possuem entrada e saida;
"""

# # Refatorando uma função
# #
# #
# # def quadrado(numero):
# #     # return numero * numero
# #     return numero ** 2  # Numero elevado ao quadrado
# #
# #
# # print(quadrado(7))
# # print(quadrado(8))
# # print(quadrado(9))
# #
# # # ou
# # ret = quadrado(7)
# # print(ret)

# # Nomeando parâmetros
#
#
# def nome_completo(nome, sobrenome):     # nome/sobrenome são Parâmetros
#     return f'seu nome completo é {nome} {sobrenome}'
#
#
# print(nome_completo('Erickson', 'Lopes'))   # erickson/lopes são argumentos
#
# # A diferença entre parametros e argumentos
#
# # Parâmetros são variáveis declaradas na definição de uma função;
# # Artumentos são dados passados durante a execução de uma função;
#
# # A Ordem dos parâmetros importa
# name = 'Felicity'
# surname = 'Jones'
#
# # Argumentos nomeados (Keyword Arguments)
#
# # Caso utilizemos nomes dos parâmetros nos argumentos para informá-los podemos utilizar qualqer ordem
#
# print(nome_completo(nome='Angelina', sobrenome='Jolie'))
# print(nome_completo(nome=name, sobrenome=surname))
# print(nome_completo(sobrenome=surname, nome=name))

# # Erro comum na utilização do return
#
#
# def soma_impares(numeros):
#     total = 0
#     for num in numeros:
#         if num % 2 != 0:
#             total = total + num
#             # o return não pode ficar aqui, se caso o if de False ele volta para o for
#     return total    # o return tem que ficar for de lações que precisem que repetição
#
#
# lista = [1, 2, 3, 5, 6, 7]
# print(soma_impares(lista))


def soma(num1, num2):
    return num1 + num2


# def subtracao(n1, n2):
#     return n1 - n2
#
#
# def mat(num1, num2, fun=soma):  # por padrão se o usuario nao informar a função, ele utilizara a soma
#     return fun(num1, num2)
#
#
# print(mat(2, 3))  # por padrão é soma
# print(mat(2, 2, subtracao))  # informando que utilizaremos a subtracao como função

# escopo - evitar problemas e confusões

# # variáveis globais
# # variáveis locais
#
# instrutor = 'geek'  # Variável global
#
#
# def diz_oi():
#     instrutor = 'python'  # VAriável local se sobrepooe a global
#     return f'oi {instrutor}'
#
#
# print(diz_oi())

# # Atenção com variáveis globais(Se puder evite)
#
# total = 0
#
#
# def incrimentar():
#     global total  # chama a vaiavel global para dentro do bloco
#     total = total + 1  # Variavel nao reconhece a global pq ela busca a criação da variavel dentro da função
#     return total
#
#
# print(incrimentar())  # total foi para 1
# print(incrimentar())  # total foi para 2
# print(incrimentar())  # total foi para 3

# podemos ter funções que são declaradas dentro de funções, e tambem temos uma forma especial de escopo de variavel

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())
