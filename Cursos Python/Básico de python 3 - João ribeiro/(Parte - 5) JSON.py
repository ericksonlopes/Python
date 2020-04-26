# JSON
# Usado para guardar e transmitir dados
# JSON é fundamentalmente uma estrutura de texto escrita
# em JavaScript Object Notation

# Acesso a dados JSON
import json

# dados = '{"nome": "joão", "apelido": "Ribeiro"}'
#
# j = json.loads(dados)
#
# print(j)
# print(j['nome'])  # buscando por indice
# print(j['apelido'])  # buscando por indice

# # acesso a dados mais complexos de json para python
# import json
#
# dados = '[{"nome": "joão", "apelido": "Ribeiro"}, {"nome": "Maria", "apelido": "Fatorio"}]'
#
# j = json.loads(dados)
# print(j[1]['nome'])  # na segunda posição quero que pegue o nome
# print(j[0]['apelido'])  # na primeira posição peguei o apelido
#
# print([j[num]['nome'] for num in range(len(j))])  # faz uma lista com todos os dados dentro de nome de cada dicionario
# print([j[num]['apelido'] for num in range(len(j))])  # lista com apelidos

# # de pytohn para json
# import json
#
# dados = {"nome": "joão",
#          "apelido": "Ribeiro"}
#
# dados_para_json = json.dumps(dados)
# print(dados_para_json)

# # de python para json de forma mais complexa
# # usando listas com dicionarios dentro
# import json
#
# dados = [{"nome": "joão", "apelido": "Ribeiro"}, {"nome": "Maria", "apelido": "Fatorio"}]
#
# instancia_json = json.dumps(dados)
# print(instancia_json)

# # é possivel formatar a saida do resultado
# import json
#
# dados = {'nome': 'Rafael',
#          'idade': 30,
#          'filhos': ('fernando', 'ravael'),
#          'carros': [{'modelo': 'Ferrari', 'Velocidade': 250}]}
#
# # indent=4 - coloca TAB nas linhas para melhor visualização
# # separators=('.', '=') - troca os separadores ':' por '=' e ',' por '.'
# print(json.dumps(dados, indent=4, separators=('.', '=')))

# ordenando os dados
dados = {"nome": "joão", "apelido": "Ribeiro", 'idade': 30}

print(json.dumps(dados, indent=4, sort_keys=True))
