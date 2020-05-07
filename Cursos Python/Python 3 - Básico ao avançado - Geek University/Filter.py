"""
Filter

filter() - > SErve para filtrar dados de uma determinada coleção
"""
# valores = 1, 2, 3, 4, 5, 6, 7
#
# media = sum(valores) / len(valores)
# print(media)

# # biblio para trabalhar com dados estatísticos
# import statistics
#
# # Dados coletado de algum sensor
# dados = [1, 3.5, 6, -0.1, 5]
#
# # calculando a média dos dados utilizando a função mean()
# media = statistics.mean(dados)
# print(f'{media}')
#
# # assim como a função map(), a filter() rebece dois parametros
# # sendo uma função e um iteravel
#
# res_cima = filter(lambda x: x > media, dados)
# res_baixo = filter(lambda x: x < media, dados)
# print(list(res_baixo), 'a baixo', list(res_cima), 'a cima')
#
# # após assim como na função map, após ser utilizado os dados de filter eles são excluidos da memoria

# paises = ['', 'Argentina', '', 'Brasil', 'Colombia', '']
# # res = filter(lambda pais: len(pais) > 0, paises)
# # res = filter(None, paises)  # se para cara pais o dado for vazio, remove
# res = filter(lambda pais: pais != '', paises)
# print(list(res))

# a diferença entre map() e filter() é :
# map() recebe dois parâmetro uma função e um iterável e
# retorna um objeto mapeando a função para cada elemento do iterável - retorna valores

# o filter() recebe dois parâmetro uma função e um iterável e
# retorna um objeto filtrando apenas os elementos de acordo com a função. - retorna True e False

# # exemplo mais complexo
#
# usuario = [
#     {"usarname": 'samuel', 'tweets': ['eu adoro bolo', 'eu adoro charles e lola']},
#     {"usarname": 'carlos', 'tweets': []},
#     {"usarname": 'nicole', 'tweets': ['eu adoro saco', 'eu adoro dinheiro']},
#     {"usarname": 'danilo', 'tweets': ['eu adoro pilulas']},
#     {"usarname": 'caukkan', 'tweets': []},
#     {"usarname": 'nilas', 'tweets': ['eu adoro skate', 'eu adoro dinheiro']},
#     {"usarname": 'njonas', 'tweets': ['eu adoro skate', 'eu adoro dinheiro']},
#     {"usarname": 'kolas', 'tweets': []},
#
# ]
#
# # filtrar os usuarios inativos do Twitter
# # print(usuario)
# inativos = list(filter(lambda inat: not len(inat['tweets']), usuario))  # nega a solução
# # inativos = list(filter(lambda inat: len(inat['tweets']) == 0, usuario))
# pouco_mov = list(filter(lambda pm: len(pm['tweets']) == 1, usuario))
# muita_mov = list(filter(lambda mm: len(mm['tweets']) > 1, usuario))
#
# print([inativos[num]['usarname'] for num in range(0, len(inativos))], 'inativo')
# print([pouco_mov[num]['usarname'] for num in range(0, len(pouco_mov))], 'pouca movimentação')
# print([muita_mov[num]['usarname'] for num in range(0, len(muita_mov))], 'Muita movimentação')

# combinar filter e map

nomes = ['Vanessa', 'Larissa', 'Loiza', 'Luiza', 'ana', 'jo']

# devemos criar uma lista contendo sua instrutora é  + o nome da instrutora,
# desde de que cada nome tenha menos de 5 caractere

lista = list(map(lambda nome: f'sua instrutora é  {nome}', filter(lambda nome: len(nome) <= 3, nomes)))

print(lista)
