larg = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))

area = larg * alt
print(f'Sua parede tem a dimensão de {larg}X{alt} e sua area é de {area}m²')
tinta = area / 2
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta')
