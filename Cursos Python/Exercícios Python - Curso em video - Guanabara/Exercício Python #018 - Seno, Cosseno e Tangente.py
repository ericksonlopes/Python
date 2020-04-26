from math import radians, sin, cos, tan

angulo = float(input('Digite o angulo que voce desja: '))

seno = sin(radians(angulo))  # transferir o valor de angulo para radianos
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')

cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')

tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')