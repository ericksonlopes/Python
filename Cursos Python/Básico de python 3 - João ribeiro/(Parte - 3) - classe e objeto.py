# # Classes e objetos
# #
# # Quase tudo no python é objeto , com propriedades e métodos.
# # Uma classe é como uma forma para criação de objetos
# class MinhaClasse:
#     nome = 'nome'
#
#
# print(MinhaClasse)


# # definição de uma classe e instanciação de objeto
# class Cliente:
#     nome = "João"
#     telefone = 11943604897
#
#
# novo = Cliente()
# print(novo.nome + ' telefone: ' + str(novo.telefone))


# todas as tem um método __init__ incluído
# o equivale ao construtor de uma classe em outras linguagens
# é um método executado automaticamente quando criamos um objeto


class Cliente:
    interno = [num for num in range(1, 5)], 'valor interno'

    def __init__(self, nome, apelido):
        self.nome = nome
        self.apelido = apelido

    def falar(self):
        print('Falei', self.nome)


# Buscar valor interno
print(Cliente.interno)

# instanciar função de uma classe
cliente1 = Cliente('Erickson', 'Lopes')
print(cliente1.nome, cliente1.apelido)

# instanciar função de uma classe
cliente2 = Cliente('Maria', 'Do Socorro')
print(cliente2.nome, cliente2.apelido)

# instancia outra função
cliente1.falar()