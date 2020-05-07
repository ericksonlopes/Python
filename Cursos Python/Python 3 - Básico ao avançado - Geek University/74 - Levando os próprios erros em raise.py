"""
Levando os próprios erros em raise

raise - Lança exceções

OBS: raise não é uma função, é um palavra resevada como o raise

Para simplificar, pense que ele funciona como uma forma de revelar por nós um erro

Forma de utilizar:

raise Tipodeerro('Mensage de erro')
"""

# # raise ValueError("Valor incorreto")
#
# # exemplo real
# def colore(texto, cor):
#     if not type(texto) == str:
#         raise TypeError('Texto precisa ser uma string')
#     if not type(cor) == str:
#         raise TypeError('Cor precisa ser uma string')
#     print(texto, cor)


# exemplo real
def colore(texto, cor):
    cores = ('Azul', 'Verde', 'Amarelo')
    if not type(texto) == str:
        raise TypeError('Texto precisa ser uma string')
    if not type(cor) == str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError('Essa cor não existe dentro dos padrões')
    print(texto, cor)


colore('1', 'Roxo')