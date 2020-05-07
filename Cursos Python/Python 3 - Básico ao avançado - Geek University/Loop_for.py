"""
Loop for

Loop -> Estrutura de repetição.
For  -> Uma dessas estruturas.

C ou Java
for(int i = 0(inicializado); i < 10(limitador); i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop


Utilizamos loops para iterar sobre sequêcias ou sobre valores interáveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
"""
# Imprimindo na mesma linha
nome = 'Geek University'
for letra in nome:
    print(letra, end='')

nome = 'Geek university'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1
for letra in nome:
    print(letra)

print('\n')  # Pular uma linha

# Exemplo de for 2
for numero in lista:
    print(numero)

print('\n')  # Pular uma linha

# Exemplo de for 3
"""
range(valor_inicial, valor_final)
OBS: o valor final não é inclusive (não o 10)
1
2
3
4
5
6
7
8
9
10 - não
"""
for numeber in range(1, 10):
    print(numeber)

# Descobrindo valor do incice
"""
enumerate
(0(G), 1(e) 2(e) 3(k)...)
para casa sequencia do nosso interavel ele adiciona um indice (+1)

for _, letra in enumerate(nome): # podemos usar o underline para descartar o valor (_)
    print(indice, letra)
"""
nome = 'Geek university'  # variavel com o nome
for indice, letra in enumerate(nome):  # O enumerate retorna dois valores o que esta sendo armazenado nas duas variaveis
    print(indice, letra)  # imprimo o indice e letra um ao lado do outro

for valor in enumerate(nome):  # Não separa o indice do valor, imprime os dois em uma lista organizada
    print(valor)
    print(valor[0])  # imprime apenas os indices por estarem na primeira possição
    print(valor[1])  # imprime apenas os valores por estarem na segunda possição

# -----------------------------

qtd = int(input('Quantas vezes esse loop deve rodar? '))  # Entrada de dado
soma = 0
for n in range(1, qtd+1):  # Faz o loop quantas vezes foi informado pelo usuario (variavel qtd)
    print(f'Imprimindo {n}')  # saida de dado

for n in range(1, qtd+1):  # Faz o loop quantas vezes foi informado pelo usuario (variavel qtd)
    num = int(input(f'Informe o {n}/{qtd} valor: '))  # Pega o valor para ser somado
    soma = soma + num  # Soma o valor com o número armazenado na variavel soma
print(f'A soma é {soma}')  # Saida de dado




