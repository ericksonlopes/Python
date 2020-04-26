# Regular Expressions
# usadas para fazer mais ou menos complexas
# construimos uma expressão que define o filtro de pesquisa

# import re
#
# texto = 'Está um lindo dia de Verão.'
# pesqueisa = re.search('^E', texto)  # Verifica se a string começa com 'E' espressão que começa '^'
# print(pesqueisa)

# import re
#
# telefone = '11943604897'
#
# pesquisa = re.search("[0-9]{11}", telefone)
# print(pesquisa)

# #  verificar se existe um certo elemento na lista
# import re
#
# nomes = 'joao, maria, carlos, josé'
#
# if re.search('maria', nomes):
#     print('sim')
# else:
#     print('não')

# devolver todos os resultados encontrados
import re

texto = 'Maria dos dores morre com 78 anos de vida, com doril morre'

resultados = re.findall('morre', texto)

print(resultados)

