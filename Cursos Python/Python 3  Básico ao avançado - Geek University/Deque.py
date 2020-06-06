"""
https://docs.python.org/pt-br/3.7/library/collections.html?highlight=collections#module-collections

Módulo collections - Deque
Podemos dizer que o deque é uma lista de alta performance
"""

from collections import deque

# criando deque
deq = deque('geek')
print(deq)

# adicionando elemento do deque
deq.append('y')  # os elementos são adicionados no final
print(deq)

deq.appendleft('k')  # os elementos são adicionados no começo
print(deq)

# removendo elementos e retornando o mesmo
deq.pop()  # Remove o ultimo elemento e o retorna
print(deq)

deq.popleft()  # Remove o primeiro elemento e o retorna
print(deq)

