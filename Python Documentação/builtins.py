for item in dir(__builtins__):
    print(item)

# abs - Retorna o númeor absoluto de um número -------------------------------------------------------------------------
print(abs(-5))
print(abs(5))
print(abs(2.555), '\n')

# all - Retorna Verdadeiro se todos os elementos do iterável forem verdadeiro ------------------------------------------
print(all([1, 2, False, 4, 8]))
print(all([1, 2, True, 4, 8]), '\n')

# any - Retorna Verdadeiro se qualquer elemento do iterável for verdadeiro ---------------------------------------------
print(any([0, 0, 0, []]))
print(any([0, 0, 0, [], 1]), '\n')

# ascii - retorna uma string contendo uma representação imprimível de um objeto ----------------------------------------
print(ascii('âãá'))
print(ascii('éê'), '\n')

# bin - Converte em uma sequência de caracteres binária prefixa com o '0b' ---------------------------------------------
print(bin(5))
print(bin(15), '\n')

# bool - ---------------------------------------------------------------------------------------------------------------
print(bool(0))
print(bool(1), '\n')

# breakpoint - Coloca Você no depurador - debug ------------------------------------------------------------------------
# breakpoint()

# bytearray - Retorna um objeto do tipo bytearray ----------------------------------------------------------------------
b = bytearray(2)
print(b, '\n')

# bytes - retona uma matriz de x bytes ---------------------------------------------------------------------------------
bt = bytes(4)
print(bt, '\n')


# callable - Verifica se é possivel chamar uma função ------------------------------------------------------------------
def x():
    a = 4


print(callable(x), '\n')

# chr - Obtenha o caractere que representa o unicode de x --------------------------------------------------------------
x = chr(97)
print(x, '\n')

# classmethod - Converte um método em um método de classe  -------------------------------------------------------------

# compile - Compila o texto como código --------------------------------------------------------------------------------
x = compile('print([num for num in range(10)])', 'test', 'eval')
exec(x)
print()

# complex - Converte os numero x e o numero imaginário y em um numero complexo: ----------------------------------------
x = complex(3, 5)
print(x, '\n')


# delattr - Exclua a propriedade de uma propriedade de um objeto -------------------------------------------------------
class Pessoa:
    nome = 'Erickson'
    anos = 18


delattr(Pessoa, 'anos')
fulano = Pessoa()
# print(fulano.anos)

# dict - Cria um dicionário --------------------------------------------------------------------------------------------
dicio = dict(name="John", age=36, country="Norway")
print(dicio, '\n')


# dir - Exibe o conteúdo de propriedades e métodos  de um objeto -------------------------------------------------------
class Saber:
    item = 0
    item_dois = 1


print(dir(Saber), '\n')

# divmod - Retorna uma tupla contendo o quoeciente e restante ----------------------------------------------------------
x = divmod(3, 2)  # 3 dividido por 2 é igual a 1, e sobre 1
print(x)  # resultado = (1, 1)

x = divmod(16, 4)
print(x, '\n')  # resultado = (4, 0)

# enumerate - pega uma coleção (exemplo, tupla) e retorna como um objeto enumerado -------------------------------------
x = ('x', 'y', 'z')
print(list(enumerate(x)), '\n')  # [(0, 'x'), (1, 'y'), (2, 'z')]

# eval - Avalia a expressão especificada; se ela for uma instrução python legal, será executada ------------------------
x = 'print(55)'
eval(x)

xpto = 35
y = 'print(xpto)'
eval(y)

print()

# exec - Executa um bloco de código válido em python -------------------------------------------------------------------
x = 'xpto2 = 24\nprint(xpto2)'
exec(x)

print()

# exit - finaliza o programa; só deve ser usada no interprete ----------------------------------------------------------
while x == 1:
    exit()

# filter - Retorna um iterádor onde os itens são filtrados por uma função para testar se o item é aceito ou não --------
anos = [15, 24, 18, 25, 45, 12, 10]

adultos = filter(lambda x: x >= 18, anos)

print(list(adultos))

print()

# float - Retorna um número em ponto flutuante -------------------------------------------------------------------------
x = 3
print(float(x), '\n')

# format - formata um valor especificado em um formato especificado ----------------------------------------------------
x = format(72, 'b')
print(x)

# '<' - Esquerda alinha o resultado (dentro do espaço disponível)
# '>' - Alinha à direita o resultado (dentro do espaço disponível)
# '^' - O centro alinha o resultado (dentro do espaço disponível)
# '=' - Coloca o sinal na posição mais à esquerda
# '+' - Use um sinal de adição para indicar se o resultado é positivo ou negativo
# '-' - Use um sinal de menos apenas para valores negativos
# '' - Use um espaço à esquerda para números positivos
# ',' - Use vírgula como separador de milhar
# '_' - Use um sublinhado como separador de milhar
# 'b' - formato binário
# 'c' - converte o valor no caractere unicode correspondente
# 'd' - formato decimal
# 'e' - Formato científico, com letras minúsculas e
# 'E' - formato científico, com E maiúsculo
# 'f' - Formato do número do ponto de correção
# 'F' - Formato do número do ponto fixo, maiúscula
# 'g' - formato geral
# 'G' - formato geral (usando E maiúsculo para anotações científicas)
# 'o' - formato octal
# 'x' - formato hexadecimal, minúsculas
# 'X' - formato hexa maiúsculo
# 'n' - Formato numérico
# '%' - formato de porcentagem

# frozenset - retorna um objeto fronzenset imutável (como um objeto set, apenas imutável) ------------------------------
lista = [1, 5, 7, 'artigo']
x = frozenset(lista)
print(x, '\n')


# getattr - obter valor de uma propriedade do objeto -------------------------------------------------------------------
class Pessoa:
    corona = 'positivo'


print(getattr(Pessoa, 'corona'), '\n')

# globals - Exibe a tabela de símbolos globais como um dicionário ------------------------------------------------------
x = globals()
print(x, '\n')


# hasattr - Verifica se o objeto possui a propriedade especifica -------------------------------------------------------
class Pessoa:
    nome = 'Nome'
    anos = 18


print(hasattr(Pessoa, 'nome'))
print(hasattr(Pessoa, 'vida'), '\n')

# hash - Retorna o valor de hash de um objeto especificado -------------------------------------------------------------
print(hash(Pessoa))

# help - Executa o sistema de ajuda interno ----------------------------------------------------------------------------
print(help(float), '\n')

# hex - Converte um número para hexadecimal ----------------------------------------------------------------------------
x = hex(255)
print(x, '\n')

# id - Retorna um ID exclusivo para o objeto especificado
x = [1, 2, 4]
y = id(x)

print(y, '\n')

# input - Permite a entrada de dados do usuario pelo terminal
# x = input('Digite aqui')
# print(x)

# int - Converte um número para inteiro
print(int(3.45), '\n')  # 3

# isinstance - Retorna True se o objeto especificado for do tipo especificado, caso contrário, False -------------------
x = 2
print(isinstance(x, float))
print(isinstance(x, int), '\n')


# issubclass - Verifica se o objeto é uma subclasse --------------------------------------------------------------------
class Pessoa:
    nome = 'Erickson'


class Gente(Pessoa):
    nome = Pessoa.nome
    anos = 20


print(issubclass(Gente, Pessoa), '\n')  # se Gente é uma subclasse de Pessoa

# iter - Retorna um objeto iterador ------------------------------------------------------------------------------------
x = iter([1, 2, 3, 4])
print(next(x))  # 1 0
print(next(x))  # 2 1
print(next(x), '\n')  # 3 2

# len - Devolve o número de itens de uma lista -------------------------------------------------------------------------
x = [1, 2, 3]
print(len(x), '\n')  # 3

# list - Retorna uma lista ---------------------------------------------------------------------------------------------
x = list((1, 2, 3))
print(x, '\n')

# locals - retorna a tabela de símbolos local com o dicionário ---------------------------------------------------------
x = locals()
print(x)

# map - Executa a função para cada item do iterável --------------------------------------------------------------------
x = [1, 2, 3]
print(list(map(lambda n: n * 2, x)), '\n')

# max - Retorna o maior valor de um iterável ---------------------------------------------------------------------------
x = [10, 20, 50, 100]
print(max(x), '\n')

# memoryview - Retorna um objeto que exibe a memória de um objeto
x = memoryview(b'Hello')
print(x[0], '\n')

# min - Retorna o menor valor de um iterável ---------------------------------------------------------------------------
x = [10, 20, 450]
print(min(x), '\n')

# next - Retorna em sequencia de uso os elementos de um iterável -------------------------------------------------------
x = iter([1, 2, 3])
proximo = next(x)
print(proximo)
print(proximo, '\n')

# object - Cria um objeto vazio ----------------------------------------------------------------------------------------
x = object()
print(x, '\n')

# oct - Converte um elemento para octal --------------------------------------------------------------------------------
print(oct(12))
print(oct(25), '\n')

# open - Abre um objeto do tipo arquivo --------------------------------------------------------------------------------
x = open('arquivo.txt', 'w')
print('arquivo criado', '\n')

# "r" -Leia o valor padrão. Abre um arquivo para leitura, erro se o arquivo não existir
#
# "a" -Append-Abre um arquivo para anexar, cria o arquivo se ele não existir
#
# "w" -Write-Abre um arquivo para gravação, cria o arquivo se ele não existir
#
# "x" -Criar - cria o arquivo especificado, retorna um erro se o arquivo existir
#
# "t" - Valor padrão do texto. Modo de texto
#
# "b" - modo binário-binário (por exemplo, imagens)

# ord - Retorna o número representando o código unicode de um caractere especifico -------------------------------------
print(ord('c'), '\n')

# pow - Retorna o valor da potência de x para y ------------------------------------------------------------------------
print(pow(4, 3), '\n')  # 4*4*4

# quit - Finaliza a execução de um código, usar em exceções e no interprete --------------------------------------------
# quit()

# range - Gera uma sequencia de números que se inica por padrão em 0 ---------------------------------------------------
y = range(3)
print(y, '\n')

# reversed - Retorna um objeto iterador invertido ----------------------------------------------------------------------
y = ['a', 'b', 'c']
z = reversed(y)
print(list(z), '\n')

# round - Retorna uma função que aredondada um numero, e podemos colocar quantas casas pós virgula ---------------------
y = 2.57
print(round(y, 1), '\n')

# set - cria um objeto do tipo set imutável que não aceita duplicações -------------------------------------------------
y = [1, 2, 3, 1, 2, 4, 5]
print(set(y), '\n')


# setattr - Altera o valor de um objeto de uma classe ------------------------------------------------------------------
class Pessoa:
    ano = 2000


setattr(Pessoa, 'ano', 2020)
print(Pessoa.ano, '\n')

# slice Retorna um objeto de uma fatia ---------------------------------------------------------------------------------
a = ("a", "b", "c", "d", "e", "f", "g", "h")

y = slice(0, 8, 3)

print(a[y], '\n')

# sorted - ordena um iterável ------------------------------------------------------------------------------------------
a = [1, 2, 5, 4, 7, 9, 6]
print(sorted(a), '\n')

# str - Converte para string -------------------------------------------------------------------------------------------
t = 88

print(type(str(t)), '\n')

# sum - Soma todos os itens de um iterável -----------------------------------------------------------------------------
l = [1, 2, 3, 4]
print(sum(l), '\n')


# super - A função é usada para dar acesso a métodos e propriedades de uma classe de pais ou irmãos --------------------
class Parent:
    def __init__(self, txt):
        self.message = txt

    def printmessage(self):
        print(self.message)


class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)


h = Child("Hello, and welcome!")

h.printmessage()

# tuple - Converte para tupla ------------------------------------------------------------------------------------------
tupla = [1, 2, 4, 5, 6]
print(tuple(tupla), '\n')

# type - exibe o tipo de item ------------------------------------------------------------------------------------------
print(type(x), '\n')


# vars - A função retorna o atributo __dic__ de um objet ---------------------------------------------------------------
class Person:
    name = "John"
    age = 36
    country = "norway"


r = vars(Person)
print(r, '\n')

# zip - Faz um iterador que agrega cada um dos elementos por seus index ------------------------------------------------
x = [0, 2, 4, 6, 8]
y = [1, 3, 5, 7, 9]
z = zip(x, y)
print(list(z), '\n')

