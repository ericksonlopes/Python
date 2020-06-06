"""
Saindo de loops com break

Funciona da mesma forma que nas linguagens C ou Java.

Utilizamos o break para sair de loops de maneira projetada.
"""

# exemplo 1
for numero in range(1, 10):
    if numero == 6:
        break
    else:
        print(numero)
print("Sai do loop")

# exemplo 2
while True:
    comando = input('Digite "Sair" para sair: ' )
    if comando == 'Sair':
        break
