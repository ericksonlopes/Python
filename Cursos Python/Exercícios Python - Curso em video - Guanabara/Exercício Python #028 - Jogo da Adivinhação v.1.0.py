from random import randint
computador = randint(0, 5)

print('Você precisa pensar em um número de 0 e 5')

jogador = int(input('Em que número eu pensei? '))

if jogador == computador:
    print(f'Você acertou! {computador}')
else:
    print(f'Você perdeu o número era: {computador}')