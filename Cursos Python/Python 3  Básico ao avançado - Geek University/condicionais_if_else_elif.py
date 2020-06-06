"""
Etruturas condicionais
if (se) , else, elif
"""

idade = input('Informe sua idade:')
if idade < 18:
    if idade < 2:
        print('Menor de idade')
        print(f'Você tem {idade} ano')
    else:
        print('Menor de idade')
        print(f'Você tem {idade} anos')
elif idade >= 18:
    if idade > 117:
        print('Você tem todos os anos, você acaba de bater um recorde!')
    else:
        print(f'Você é maior de idade com seus {idade} anos!')


