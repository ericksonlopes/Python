# [print(item) for item in dir(str)]

# capitalize - Retorna uma sequência onde o primeiro caractere fica em maiúsculo ---------------------------------------
texto = 'o dia está lindo'
titulo = texto.capitalize()
print(titulo, '\n')

# casefold - Retorna uma string em que todos os caracteres são minúsculos  ---------------------------------------------
texto = 'eu quero Doce'
minusculo = texto.casefold()
print(minusculo, '\n')

# center - Retorna uma string alinhada ao centro da quantidade de espaço especificada ----------------------------------
texto = 'Banana'
centro = texto.center(10)
print(centro, '\n')

# count - Retorna o número de vezes que o valor aparece na string ------------------------------------------------------
texto = 'O número é equivalente ao número'
print(texto.count('o'), '\n')

# encode - codifica a sequência usando a codificação especificada, por padrão vem UTF-8 --------------------------------
texto = 'Para ser codificado'
texto.encode('UTF-8')
print(texto, '\n')

# endswith - Retorna True se a sequencia termina com o valor especificado ----------------------------------------------
texto = 'Hoje em dia esta facil'
verifica = texto.endswith('facil')
print(verifica, '\n')

# expandtabs - define o tamanho da guia para o número especificado de espaços em branco
txt = "H\te\tl\tl\to"
x = txt.expandtabs(5)
print(x, '\n')

# find - Retorna o index da primeira ocorrencia do número especificado -------------------------------------------------
texto = 'O dia está cada vez mais bonito'
localiza = texto.find('dia')
print(localiza, '\n')

# format - Formata os valores especificados e insere no espaço reservado da string -------------------------------------
texto = 'Hoje em dia esta muito {temperatura}'
print(texto.format(temperatura='calor'), '\n')

# : <
# Esquerda alinha o resultado (dentro do espaço disponível)
# :>
# Alinha à direita o resultado (dentro do espaço disponível)
# : ^
# Centro alinha o resultado (dentro do espaço disponível)
# : =
# Coloca o sinal na posição mais à esquerda
# : +

# Use um sinal de mais para indicar se o resultado é positivo ou negativo
# : -
# Tente
# Use um sinal de menos apenas para valores negativos
# :
# Tente
# Use um espaço para inserir um espaço extra antes dos números positivos e um sinal de menos antes dos números negativos
# :,
# Tente
# Use uma vírgula como separador de milhar
# : _
# Tente
# Use um sublinhado como separador de milhar
# : b
# Tente
# Formato binário
# : c
#
# Converte o valor no caractere unicode correspondente
# : d
# Tente
# Formato decimal
# : e
# Tente
# Formato científico, com letras minúsculas e
# : E
# Tente
# Formato científico, com E maiúsculo
# : f
# Tente
# Formato do número do ponto de correção
# : F
# Tente
# Corrija o formato do número do ponto, em formato maiúsculo (mostre inf e nan como INF e NAN)
# : g
#
# Formato geral
# : G
#
# Formato geral (usando E maiúsculo para anotações científicas)
# : o
# Tente
# Formato octal
# : x
# Tente
# Formato hexagonal, minúscula
# : X
# Tente
# Formato hexagonal, maiúscula
# : n
#
# Formato numérico
# :%
# Tente
# Formato percentual
# format_map -

# index - retorna o index da primeira ocorrência do valor especificado -------------------------------------------------
texto = 'O dia esta'
ocorrencia = texto.index('dia')  # gera erro se não encontrar
print(ocorrencia, '\n')

# isalnum - Retorna True se os valores forem alfanuméricos com números e letras (0-9)(a-z) não conta simbolos ----------
texto = 'dia235'
print(texto.isalnum(), '\n')

# isalpha - Retorna True se todos os caracteres estiverem no alfabeto --------------------------------------------------
texto = 'abc'
print(texto.isalpha(), '\n')

# isascii - Retorna verdadeiro se a codifiação for me UTF-8 ------------------------------------------------------------
texto = '片仮名'
print(texto.isascii(), '\n')

# isdecimal - Retorna True se todos os caracteres forem números para objetos unicode -----------------------------------
texto = '\u0033'
print(texto.isdecimal(), '\n')

# isdigit - Verifica se todos os caracteres são digitos, numeros de qualquer origem, inclusive expoentes----------------
texto = '³²54'
print(texto.isdigit(), '\n')

# isidentifier - Retorna True se a string for um indentificador válido, conter apenas (a-z),(0-9) e (_), não pode conter
# espaçes e começar por números-----------------------------------------------------------------------------------------
texto = 'demo 1'
print(texto.isidentifier(), '\n')

# islower - Retorna True se todos os caracteres estiverem em minúsculos ------------------------------------------------
texto = 'kasjbflsa'
print(texto.islower(), '\n')

# isnumeric - Verifica se todos os caracteres são números --------------------------------------------------------------
texto = '123'
print(texto.isnumeric(), '\n')

# isprintable - Verifica se os caracteres são imprimiveis --------------------------------------------------------------
texto = 'sdkg 3 32 456sd4f /  f[]-'
print(texto.isprintable(), '\n')

# isspace - Verifica se os caracteres são espaços ----------------------------------------------------------------------
texto = '          '
print(texto.isspace(), '\n')

# istitle - Verifica se o primeiro caractere começa em maiusculo, simbolos e numeros são ignorados e pula para letra ---
texto = '1 Escola'
print(texto.istitle(), '\n')

# isupper - Retorna True se todos os caracteres estiverem em maiusculos, apenas caracteres letras (a-z) ----------------
texto = 'SKJDB 5445'
print(texto.isupper(), '\n')

# join - Pega os valores de um iterável e une em uma string, indentificar como ele deve separar ------------------------
lista_nome = ['Daniel', 'Silva', 'Pereira']
nome_completo = ' '.join(lista_nome)
print(nome_completo)

data = ['19', '05', '2019']
data_completa = '/'.join(data)
print(data_completa, '\n')

# ljust - deixará o alinhamento à esquerda, usando um caractere especificado (o espaço é o padrão)
# como o caractere de preenchimento. -----------------------------------------------------------------------------------
txt = "Banana"

x = txt.ljust(20)

print(x, "é minha fruta favorita", '\n')

# lower - Retorna todos os caracteres em minusculos --------------------------------------------------------------------
texto = 'SDFSDFD Dfff'
print(texto.lower(), '\n')

# lstrip - Remove os elementos a esquerda que por padrão é espaço ------------------------------------------------------
texto = '     banana     '
x = texto.lstrip()
print('skdbi', x, 'assad', '\n')

# partition - separa em uma tupla os elementos antes e depois da palavra especificada ----------------------------------
texto = 'Eu sonho em ser programador'
x = texto.partition('ser')
print(x, '\n')

# replace - troca a palavra especificada por outra ---------------------------------------------------------------------
texto = 'Eu gosto de bananas'
x = texto.replace('bananas', 'maça')
print(x, '\n')

# rfind - encontra a ultima ocorrencia do valor especificado, podendo alterar onde termina e começa --------------------
texto = 'Mi casa, su casa'
x = texto.rfind('casa')
print(x, '\n')

# rindex - faz o mesmo que o rfind() mas retorna erro ------------------------------------------------------------------
texto = 'Mi casa, su casa'
x = texto.rfind('casa')
print(x, '\n')

# rjust - criara um espaço e coloca a string alinhada a esquerda -------------------------------------------------------
texto = 'banana'
x = texto.rjust(20)
print(x, '\n')

# rpartition - procura a última ocorrência de uma sequência especificada e divide a sequência em uma tuple contendo ----
# três elementos.
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x, '\n')

# rsplit - divide uma string em uma lista, começando pela direita. -----------------------------------------------------
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x, '\n')

# rstrip - Remova os espaços à direita da string -----------------------------------------------------------------------
txt = "banana,,,,,ssaaww....."
x = txt.rstrip(",.asw")
print(x, '\n')

# split - Divide uma sequencia em uma lista em que cada palavra é um item da lista -------------------------------------
txt = "welcome to the jungle"
x = txt.split(' ')
print(x, '\n')

# splitlines - Divide o texto em que cada linha é um item da lista -----------------------------------------------------
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x, '\n')

# startswith - Retorna True se a sequencia começa com o valores especificado, caso contrário, False --------------------
texto = 'Margarida é linda'
x = texto.startswith('Margarida')
print(x, '\n')

# strip - Remove da sequencia o valor especificado ---------------------------------------------------------------------
txt = "     banana     "
x = txt.strip(' ')
print("of all fruits", x, "is my favorite", '\n')

# swapcase - Retorna uma sequencia onde todas as letras maiúsculas são minúsculas e vice-versa -------------------------
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x, '\n')

# title Coloque a primeira letra de cada palavra em maiúscula: ---------------------------------------------------------
txt = "Welcome to my world"
x = txt.title()
print(x, '\n')

# upper - Transforma a sequencia em maiuscula --------------------------------------------------------------------------
txt = "Hello my friends"

x = txt.upper()

print(x, '\n')
# zfill -  adiciona zeros (0) no início da string, até atingir o comprimento especificado ------------------------------
txt = "50"

x = txt.zfill(10)

print(x)
