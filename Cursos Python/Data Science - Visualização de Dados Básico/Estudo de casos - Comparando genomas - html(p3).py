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

# html
i = 1
for k in cont:  # cada chave do dicionario sera armazenada em 'k'
    transparencia = cont[k]/max(cont.values())  # isto para deixar o maior valor mais colorido
    saida.write("<div style='width:100px; border:1px solid #111; height:100px; color:#fff"
                "float:left; background-color:rgba(0, 0, 0, "+str(transparencia)+")'>"+k+"</div>")

    if i % 4 == 0:  # todos os numeros divisiveis por 4
        saida.write("<div style='clear:both'></div>")  # força o html a fazer uma quebra de linha
    i += 1
saida.close()
