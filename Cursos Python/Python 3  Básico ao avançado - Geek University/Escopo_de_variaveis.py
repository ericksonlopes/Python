"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
    - O escopo da variavel global é reconhecida por todo o programa.

2 - Variáveis locais
    - O escopo da variavel local é reconhecido apenas no bloco onde foram declaradas,
    seu escopo esta limitado ao bloco onde foi declarada.

Para declarar variaveis em Python?
nome_da_variavel = Valor_da_variavel

python [e uma linguagem de tipagem dinâmica. Isso significa que
ao declarar uma variavel, nós não colocamos o tipo de dado dela.
Este tipo é incerido ao tribuirmos o valor à mesma

Exemplo em C:
int numero = 42;

Exemplo em java
int numero = 42;
"""

numero = 42  # Variavel global
print(numero)
print(type(numero))

# Reatribuição
numero = 'Geek'
print(numero)
print(type(numero))

nao_existo = 'oi'
print(nao_existo)

numero = 42

if numero < 10:  # Abre um bloco com os dois pontos
    novo = numero + 10
    print(novo)
