salario = float(input('Qual é o salário do funcionário: '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print(f'Quem ganhava RS${salario:.2f}, passa a aganhar {novo:.2f}')