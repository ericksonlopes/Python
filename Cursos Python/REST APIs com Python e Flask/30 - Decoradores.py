import functools


def meu_decorador(funcao):
    @functools.wraps(funcao)
    def funcar_que_roda_funcao():
        print('Embrulhando função')
        funcao()
        print('fechando embrulho')
    return funcar_que_roda_funcao()


@meu_decorador
def minha_funcao():
    print('Eu sou uma função')


minha_funcao()
