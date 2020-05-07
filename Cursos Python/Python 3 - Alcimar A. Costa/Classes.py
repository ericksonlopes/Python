# # Cria classe e retorna o valor dentro dela
# class MinhaClasse:
#     i = 123
# x = MinhaClasse.i
# print(x)

# classe televisão
# class Televisao:
#     def __init__(self):
#         self.ligada = False
#         self.canal = 4
#
#
# tv = Televisao()
# print(tv.ligada)
# print(tv.canal)
#
# tv2 = Televisao()
# tv2.canal = 10
# print(tv2.canal)


# classe livros
class Livro:
    def __init__(self, titulo, autor, editora, isbn, ano):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.isbn = isbn
        self.ano = ano

    def __str__(self):
        return f'O livro {self.titulo} criado pelo autor {self.autor};\n' \
               f'Publicado pela editora {self.editora} no ano de {self.ano};\n' \
               f'código do livro {self.isbn}.'


if __name__ == '__main__':
    cascavel = Livro('Comédia selvagem', 'Tiringa', 'Charles', '111.222.333', 2018)

    print(cascavel)
