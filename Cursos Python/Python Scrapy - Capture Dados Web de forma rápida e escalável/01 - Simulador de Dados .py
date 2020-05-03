import random
import statistics

lista = []

while True:
    faces = random.randint(1, 6)
    if faces == 5:
        break
    else:
        lista.append(random.randint(1, faces))

print(lista)
print(lista, 'média ->', statistics.mean(lista))
