"""
Funções com parâmetros padrão (default parameters)

- Funções onde a passagem de parâmetro seja opcional;

"""
# # Exemplo de parametro opcinal
# print('Geek University')
# print()  # Opcional colocar parametro ou não]

# # Exemplo de funções onde a passagemd e paraâmetro é obrigatoria
#
#
# def quadrado(numero):
#     return numero ** 2
#
#
# print(quadrado(3))


# def exponencial(numero, potencia=2):
#     return numero ** potencia, print(potencia)
#
#
# print(exponencial(2, 3))    # 2 * 2 * 2 = 8
# print(exponencial(3, 2))    # 3 * 3 = 9
#
#
# print(exponencial(3))   # por padrão eleve ao quadrado(porencia=2)
# print(exponencial(3, 5))    # eleva á potência informada pelo usuário
#
# # Se o usuario informar 1 argumento sera elevado a 2(quadrado)
# # se passar 2 argumentos sera elevado pelo segundo argumento

# OBS: em python, os parâmetros com valor default(padrão) DEVEM sempre estar no final da declaração
#
# def teste(num=1, potencia):  Erro
# def teste(potencia, num1=1): Certo
# prit(teste(1))
#
# # Outros exemplos
#
#
# def soma(num1=1, num2=1):
#     return num1 + num2
#
#
# print(soma())
# print(soma(1))
# print(soma(1, 9))
#
# Exemplo mais complexo
#
#
# def mostra_iunformacao(nome='Geek', instrutor=False):
#     if nome == 'Geek' and instrutor:
#         return 'Bem-vindo instrutor Geek!'
#     elif nome == 'Geek':
#         return 'Eu pensei que você era o instrutor'
#     return f'Olá {nome}'
#
#
# print(mostra_iunformacao())
# print(mostra_iunformacao('matheus'))
# print(mostra_iunformacao(instrutor=True))  # eu não poderia simplesmente passar True, tem que chamar o parâmetro
# print(mostra_iunformacao(nome='Erickson'))

# Por quê utilizamos parâmetros com valor default?
#     - Nos permite ser mais flexíveis nas funções;
#     - Evita erros com parâmetros incorretos;
#     - nos permite trabalhar com exemploes mais legíveis de códigos;

# Quais tipos de dados podemos utilizar como valores default para parâmetros
#     - Qualquer tipo de dado:
#     - Núemros, string, boleanos, dicionarios, funções, funcoes e etc;

# exemplo
