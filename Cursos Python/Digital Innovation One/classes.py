class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminuir_canal(self):
        if self.ligada:
            self.canal -= 1


televisao = Televisao()
print('A televisão esta: {}'.format(televisao.ligada))
televisao.power()
print('A televisão esta: {}'.format(televisao.ligada))

print('Canal selecionado: {}'.format(televisao.canal))
televisao.aumenta_canal()
print('Canal aumentado para o : {}'.format(televisao.canal))
televisao.diminuir_canal()
print('Cancal diminuido para: {}'.format(televisao.canal))
