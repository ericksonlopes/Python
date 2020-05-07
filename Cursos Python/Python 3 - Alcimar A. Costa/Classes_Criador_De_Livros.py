from Classes import Livro as Livro

Cascavel = Livro('Comédia selvagem', 'Tiringa', 'Charles', '111.222.333', 2018)
Ai = Livro('Inteli. Arti', 'Prof: Erickson', 'MF', '11552.155', 2019)
Lei_fractal = Livro('juramento', 'Prof: esperiencie', 'truques_mat', '333.66.99', 2022)

livros = [Cascavel, Ai, Lei_fractal]

for item in livros:
    print(item, '\n')

# # Caso a função não fosse criada
# for ids, item in enumerate(livros):
#     print(f'ID: {ids}\nlivro: {item.titulo}')
#     print(f'Autor: {item.autor}')
#     print(f'Editora: {item.editora}')
#     print(f'Código: {item.isbn}, Ano: {item.ano}\n')

