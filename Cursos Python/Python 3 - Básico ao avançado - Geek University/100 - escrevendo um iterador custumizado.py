"""
Escrevendo um iterador costumizado
    range()
"""


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration


# con = Contador(1, 3)
#
# print(con.menor)
# print(con.maior)
#
# it = iter(con)

for n in Contador(1, 60):
    print(n)