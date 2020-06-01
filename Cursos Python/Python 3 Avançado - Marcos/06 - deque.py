from collections import deque

# fila = deque(maxlen=4)
#
# fila.append(1)
# fila.append(2)
# fila.append(3)
# fila.append(4)
# fila.append(5)
#
# print(fila)

fila = deque()

fila.append(1)
fila.append(2)
fila.appendleft(3)

print(fila)