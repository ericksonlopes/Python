class Livro:
    def __init__(self, titulo, autor):
        # encapsulando a variavel titulo
        self.__titulo = titulo
        self.autor = autor

    # pegar o valor da variavel
    @property
    def titulo(self):
        return self.__titulo

    # inserir um valor na variavel
    @titulo.setter  # inserir valor na variavel
    def titulo(self, valor_inserir):
        self.__titulo = valor_inserir


Livro1 = Livro('Lupas', 'Carlos')

print(Livro1.titulo)  # esse titulo é o nome da função
Livro1.titulo = 'Novo item'  # adiciona a partir da  @titulo.setter

print(Livro1.titulo)
print(Livro1.autor)
