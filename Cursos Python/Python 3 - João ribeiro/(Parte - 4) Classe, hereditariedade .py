# HEREDITATIEDADE
# é umas das caracteristicas da programação orientada a objeto
# Podemos criar classes que vão herdar métodos e propriedades de outras classes


# class Animal:
#
#     def __init__(self, especie):
#         self.especie = especie
#         self.caracterictica = 'As principais características dos seres vivos são a sua composição \n' \
#                               'química comum, a presença de células, o metabolismo, a capacidade de \n' \
#                               'reprodução e a evolução. \n'
#
#     def mostrarEspecie(self):
#         print('Eu sou um(a) ' + self.especie)
#         print(f'O que caracterica um(a) {self.especie} é: \n' + self.caracterictica)
#
#
# class Mamifero(Animal):
#     pass
#
#
# class Peixe(Animal):
#     pass
#
#
# cavalo = Animal('cavalo')
# cavalo.mostrarEspecie()
#
# sardinha = Animal('Sardinha')
# sardinha.mostrarEspecie()


# # adicionar __init__ á classe  filha  sobrepondo ao __init__ da mãe
# # classe mãe
# class Humano:
#     def __init__(self, n):
#         self.nome = n
#
#     def apresentar(self):
#         print('O nome é ' + self.nome)
#
#
# # classe filha
# class Homem(Humano):
#     def __init__(self, n, a):
#         super().__init__(n)
#         self.nome = n
#         self.apelido = a
#
#     def apresentar(self):
#         print(self.nome + ' ' + self.apelido)
#
#
# class Mulher(Humano):
#     def __init__(self, n, a, p):
#         super().__init__(n)
#         self.nome = n
#         self.apelido = a
#         self.profissao = p
#
#    # se caso essa cópia de código esteja desabilitada por ser uma herença ela herdara o def apresentar da class humano
#     def apresentar(self):
#         print(self.nome + ' ' + self.apelido + ' Profição: ' + self.profissao)
#
#
# classe_homem = Homem('Joao', 'Ribeiro')
# classe_homem.apresentar()
#
# classe_mulher = Mulher('Maria', 'Fernandes', 'Faxineira')
# classe_mulher.apresentar()


# hereditariedade
class humano:
    def falar():
        print()

    def saltar():
        print()

    def andar():
        print()


class homem(humano):
    def gritar():
        print('Gritei')


h = homem()

h.gritar()