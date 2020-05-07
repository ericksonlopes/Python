"""
Módulo collections - Counter

Collections -> High - performance Container DateTypes

counter -> Recebe um iteravel como prâmetro e cria um objeto do tipo collections counter que é parecido
com um dicionario, contendo como chave o elementeo da lista passada como parametro e como valor a quantidade
de ocorrencias desse elemento.
"""

# utulizando o counter

# importanto Counter
from collections import Counter

# # Exemplo 1
#
# # podemos utilizar qualquer iteravel, aqui utulizamos uma lista
# lista = [1, 1, 1, 1, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 55, 44, 88, 99, 74]
#
# # utilizando o Counter
# res = Counter(lista)
#
# print(type(res))
# print(res)  # Counter({4: 8, 1: 4, 5: 4, 2: 3, 6: 3, 55: 1, 44: 1, 88: 1, 99: 1, 74: 1})
# # Para cada elemento da lista o Counter criou uma chave com o número de ocorrencias(vezes aparecido) do valor.

# # Exemplo 2
# print(Counter("Geek University"))
# # Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# exemplo 3
texto = """Um wiki (/ˈwiki/) é um website no qual utilizadores modificam colaborativamente conteúdo e estrutura 
diretamente do web browser. Num wiki típico, texto é escrito com uma linguagem de marcação e frequentemente editado com
a ajuda de um editor de texto enriquecido.[1] Um wiki é executado por um software wiki, um tipo de sistema de gestão 
de conteúdo, mas diverge da maioria dos outros tais sistemas, inclusive software de blog, em que o conteúdo é criado
sem qualquer dono ou líder definido, e wikis possuem pouca estrutura inerente, que permite a estrutura ser melhorada
de acordo com as necessidades dos utilizadores.[2] Há dezenas de diferentes softwares de wiki em uso, tanto autónomos
quanto partes de outros softwares, como sistemas de rastreio de bugs. Alguns softwares de wiki são de código aberto,
enquanto outros são proprietários. Alguns permitem controlo sobre diferentes funções (níveis de acesso); 
por exemplo, direitos de edição podem permitir alteração, adição ou remoção de material. Outros podem permitir
acesso sem forçar controlo de acesso. Outras regras podem ser imposta para organizar conteúdo.[3]"""

palavras = texto.split()  # separar palavras
# print(palavras)

res = Counter(palavras)
print(res)

print(res.most_common(5))

for a, b in res.most_common(1):  # pegando a chave que indica o valor mais usado
    print(a)
    res = a

print(f'A palavra mais usada no texto foi : {res}')


