import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
    aleatorio = random.randint(0, 500)
    vetor.append(aleatorio)

plt.boxplot(vetor)
plt.title('Box plot')
plt.show()

