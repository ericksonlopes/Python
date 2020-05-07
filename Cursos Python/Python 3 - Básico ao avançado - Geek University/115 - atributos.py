# -*- coding: utf-8 -*-
"""
Atributos - representa caracteristiscas do objeto

em python, definimos os atributos em 3 classes
    - instâncias;
    - classe;
    - dinâmico;
"""


# instâncias - atributos declarados dentro do método construtor

# OBS: método construtor: é um método especial utilizado para construção do objeto

# funções dentro de classes são métodos

# criando uma classe lampada com atributos publicos
class LampadaPublica:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


# criando uma classe lampada com atributos privados
class LampadaPrivada:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False


# # Exemplo
# lampada_publica = LampadaPublica(200, 'vermelha')
# print(lampada_publica.ligada)
#
# lampada_privada = LampadaPrivada(200, 'azul')
# # print(lampada_privada)
# print(lampada_privada._LampadaPrivada__ligada)  # uma forma de pegar o valor doa tributo privado (name mangling)

# # atributos de instância
#
# lampada_publica = LampadaPublica(200, 'vermelha')
# lampada_publica.ligada = True
#
# # atributor de Classes
# lampada_publica_2 = LampadaPublica(200, 'vermelha')

# # atributo de classe
#
# class Produto:
#
#     # Atributo de classe
#     imposto = 0.05
#
#     def __init__(self, valor):
#         self.valor = (valor * Produto.imposto)
#
#     def exibir_valor(self):
#         print(self.valor)
#
#
# produto = Produto(500.00)
#
# print(produto.imposto)
# produto.exibir_valor()


# contador em uma classe
class Produto:

    # Atributo de classe
    imposto = 0.05
    contador = 0

    def __init__(self, valor):
        self.id = Produto.contador + 1
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

    def exibir_valor(self):
        print(self.valor)
        print(self.id)


v1 = Produto(400)
v2 = Produto(4500)

v1.exibir_valor()
v2.exibir_valor()

# atributo dinâmico
v1.peso = 10

print(v1.peso)
print(v1.__dict__)

# deletar dinâmicamente um atributo
del v1.peso
print(v1.__dict__)

