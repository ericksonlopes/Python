print('Analisar triangulo')

r = [float(input(f'Digite o valor {num}° do triângulo: ')) for num in range(1, 4)]

if r[0] < r[1] + r[2] and r[1] < r[0] + r[2] and r[2] < r[0] + r[1]:
    print('Os segmentos acima PODEM FORMAR triângulo')
else:
    print('Os segmentor acima NÃO PODEM FORMAR triângulo')