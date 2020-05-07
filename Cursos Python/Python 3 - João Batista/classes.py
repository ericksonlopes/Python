class Pessoa:
    def __int__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar(self):
        print(self.nome)

x = Pessoa
x.nome = 'erickson'
x.idade = 25

