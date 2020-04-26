def soma(a, b):
    return a + b


def funcao_dinamica(*args, **kwargs):
    # print(args)
    #
    # print(args[0])

    # imprimir cada item
    # for i in args:
    #     print(i)

    print(kwargs)

    print(kwargs['texto'])

    # imprimir cada valor de item
    # for i in kwargs:
    #     print(kwargs[i])


funcao_dinamica('124758', 2, 3, 4, 'a', texto='1, 2, 3', palavra='b')
