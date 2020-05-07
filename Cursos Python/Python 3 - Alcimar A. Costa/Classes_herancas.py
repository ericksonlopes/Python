class ClassePai:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def __str__(self):
        if self.peso < 50:
            return f'O {self.nome} tem {self.peso} KG, leve'
        else:
            return f'O {self.nome} tem {self.peso} KG, pesado'


class ClasseFilha(ClassePai):
    def __init__(self, nome, peso, cabelo):
        super().__init__(nome, peso)
        self.cabelo = cabelo


# classe pai
pessoa = ClassePai('João', 50)
print(pessoa)

# classe filha
gente = ClasseFilha('Giulia', 40, 'Verde')
print('o cabelo é: ' + gente.cabelo)
