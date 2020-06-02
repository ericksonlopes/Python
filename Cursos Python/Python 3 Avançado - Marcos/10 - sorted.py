# lista = [2, 5, 6]
# print(sorted(lista))
#
# tupla = 'joao', 'zeca', 'marcos'
# print(sorted(tupla))
#
# dicio = {'z': 1, 'v': 5, 'n':7}
# print(sorted(dicio))


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return self.nome


def pelo_nome(pessoa):
    return pessoa.nome


def pela_idade(pessoa):
    return pessoa.idade


p1 = Pessoa('Marcos', 15)
p2 = Pessoa('Bea', 20)
p3 = Pessoa('Ana', 37)

pessoas = [p1, p2, p3]

# print(sorted(pessoas, key=pela_idade))


dicio = {'z': 1, 'v': 5, 'n': 7}
print(sorted(dicio))
