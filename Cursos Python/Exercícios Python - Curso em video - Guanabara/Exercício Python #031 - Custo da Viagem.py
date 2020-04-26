distancia = float(input('Qual é a distância '))
print(f'Você está prestes a começar uma viagem de {distancia}km.')
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E preço da sua passagem será de RS${preco:.2f}')