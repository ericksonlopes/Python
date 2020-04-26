velocidade = float(input('Qual é a velocidade atural do carro? '))

if velocidade > 80:
    print('Multado, velocidade acima do permitido!')
    multa = (velocidade-80) * 7
    print(f'O valor da multa será equivalente a RS${multa:.2f}')

print('Tenha um bom dia')