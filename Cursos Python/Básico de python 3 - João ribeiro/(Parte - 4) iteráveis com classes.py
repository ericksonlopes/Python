# iteradores (iterators)
# é um objeto que contém um conjunto de valores
# podemos percorer os valores  desse objeto
# lista = [num for num in range(10)]
# [num for num in lista]

# # iterator is iterable
# numeros = [num for num in range(1, 4)]
# it = iter(numeros)
# print(next(it))  # 1
# print(next(it))  # 2
# print(next(it))  # 3
#
# # string também são iteraveis
# palavra = 'Erickson'
# it = iter(palavra)
# print(next(it))  # E
# print(next(it))  # r
# print(next(it))  # i


# # criar um iterator
# class numeros:
#     # se a função for iter ele armazena o valor
#     def __iter__(self):
#         self.a = 0
#         return self
#
#     # se a função for next ele adiciona 2 ao valor de a, que nesse caso foi passado 0
#     def __next__(self):
#         self.a += 2
#         return self.a
#
#
# n = numeros()
# it = iter(n)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# Stop interation
class numeros:
    def __iter__(self):
        self.numero = 0
        return self

    def __next__(self):
        if self.numero < 10:  # Se o numero que começa em 0 for menor que 0, executa..
            self.numero += 1
            return self.numero
        else:   # caso contrario para o código
            raise StopIteration


num = numeros()
it = iter(num)

for numero in it:
    print(numero)

