entrada = open('comparação/bacteria.fasta').read()
saida = open('bacteria.html', 'w')  # 'w' Cria se não existe

cont = {}

for i in ['A', 'T', 'C', 'G']:  # para cada um desses valores
    for j in ['A', 'T', 'C', 'G']:  # Combinação
        cont[i+j] = 0

entrada = entrada.replace('\n', '')

for k in range(len(entrada)-1):  # cruza o tamanho da entrada \ -1 pq a sequencia é par em par e o elemento é impar
    cont[entrada[k]+entrada[k+1]] += 1  # cont[entrada[k]+entrada[k+1]] == AA e o k muda a posição para o proximo

print(cont)
