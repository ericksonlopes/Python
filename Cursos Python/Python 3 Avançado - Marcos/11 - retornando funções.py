def pai(num):
    def filho1():
        print('Sou o filho 1, é igual a 10')

    def filho2():
        print('Sou o filho 2, não é igual a 10')

    try:
        assert num == 10
        return filho1()
    except AssertionError:
        return filho2()


pai(11)
pai(10)

