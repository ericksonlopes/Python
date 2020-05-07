"""
len, abs, sum, round

len - retorna o numero de itens do iteravel

sum - retona a soma de um iteravel e pode ser atribuido seu valor inicial

abs - retorna o valor negativo sem sinal

round - retorna o valor aredondado e pode ser atribuido seu valor de precisão(numeros pós cas)
"""
#
# print(len([1, 2, 3, 4, 5, 6]))  # revisando
#
# # por debaixo dos panos quando utilizamos a função len o tipo faz assim:
# # Dunder len
# print('geek university'.__len__())
#
# print(abs(-32))
# print(abs(32))
# print(abs(-3.64))

# print(sum([1, 1, 1]))
# print(sum([1, 1, 1], 4))  # com valor inicial

# exemplo round
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.2199999, 2))  # com valor de precisão
print(round(1.2121212, 2))  # com valor de precisão

