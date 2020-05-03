class Pontos:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# classe para gerar recompensas na matriz
class Recompensa(Pontos):
    def __init__(self, x, y, nome):
        # retorna o método para acessar o x e y
        super(Recompensa, self).__init__(x, y)
        self.nome = nome


# classe que cria um robo para entrar na matriz/ herda a posição do ponto
class Robo(Pontos):
    # matriz de 0x0 até 10x10

    def move_up(self):
        if self.y < 10:
            self.y += 1
            print(self.y)
        else:
            print('Movimento Proibido')

    def move_down(self):
        if self.y > 0:
            self.y -= 1
        else:
            print('Movimento Proibido')

    def move_left(self):
        if self.x > 0:
            self.x -= 1
        else:
            print('Movimento Proibido')

    def move_right(self):
        if self.x < 10:
            self.x += 1
        else:
            print('Movimento Proibido')


def checar_recompensa(robot, lista_recompensa):
    for recompensa in lista_recompensa:
        if recompensa.x == robot.x and recompensa.y == robot.y:
            print('O robo achou a recompensa: ', recompensa.nome)


if __name__ == '__main__':
    r1 = Robo(5, 5)

    recompansa1 = Recompensa(6, 5, "moeda de ouro")

    while True:
        print(r1.x, r1.y)

        movimento = input('Movimento: ')

        if movimento == '1':
            r1.move_up()
        if movimento == '2':
            r1.move_down()
        if movimento == '3':
            r1.move_left()
        if movimento == '4':
            r1.move_right()
        else:
            print('Opção inválida')

        checar_recompensa(r1, [recompansa1])



